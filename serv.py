from bottle import route, run, template


@route('/')
def index(name):
    return '<b>Hello world!'


run(host='localhost', port=8080)
