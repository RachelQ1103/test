
import socket
import time
import urllib.parse
import json


def index():
    html = b'HTTP/1.x 200 OK\r\nContent-Type: text/html\r\n\r\n<h1>Hello World</h1><img src="doge.gif"/>'
    return html


def time_response(query):
    html = 'HTTP/1.x 200 OK\r\nContent-Type: text/html\r\n\r\n<h1>Time: {}</h1><hr>{}'.format(time.time(), query)
    return html.encode('utf-8')
'''
    html = b'HTTP/1.x 200 OK\r\n\
    Content-Type: text/html\r\n\r\n
    <h1>Hello World</h1>
    <img src="doge.gif"/>'
https://www.baidu.com
/s?wd=python&rsv_pq=d0033cef0008b5c0
'''


def image():
    with open('doge.gif', 'rb') as f:
        header = b'HTTP/1.x 200 OK\r\nContent-Type: image/gif\r\n\r\n'
        img = header + f.read()
        return img

def save(msgs):
    with open('db.db', 'w') as f:
        f.write(json.dumps(msgs))


def load():
    try:
        with open('db.db', 'r') as f:
            return json.loads(f.read())
    except:
        return []

messages = load()
def message(query):
    print("msg query", query)
    if len(query) > 0:
        k, v = query.split('=')
        if k == 'neirong':
            v = urllib.parse.unquote(v)
            messages.append(v)
            save(messages)
    msg = '<br>'.join(messages)

    form = '''
    <meta charset="utf-8">
    <link rel="stylesheet" type="text/css" href="http://cdn.bootcss.com/bootstrap/4.0.0-alpha.2/css/bootstrap.css">

    <form action="/message" method="GET">
    <textarea name="neirong">请留言</textarea>
    <button class="btn btn-primary" type="button">猛击留言</button>
    </form>
    '''
    html = 'HTTP/1.x 200 OK\r\nContent-Type: text/html\r\n\r\n<h1>Hello World</h1>留言列表{}<hr>{}'.format(msg, form)
    return html.encode('utf-8')


def response_for_path(path):
    query = ''
    if '?' in path:
        path, query = path.split('?')
    r = {
        '/': index(),
        '/doge.gif': image(),
        '/time': time_response(query),
        '/message': message(query),
    }
    page404 = b'HTTP/1.x 404 NOT FOUNT\r\n\r\n<h1>NOT FOUND</h1>'
    return r.get(path, page404)


host = ''
port = 3000

s = socket.socket()
s.bind((host, port))


while True:
    s.listen(5)
    connection, address = s.accept()
    request = connection.recv(1024)
    request = request.decode('utf-8')
    print("debug, ", request)
    path = request.split()[1]

    print('ip and request, {}\n{}'.format(address, request))

    response = response_for_path(path)

    print('response, ', path, response)
    connection.sendall(response)

    connection.close()
