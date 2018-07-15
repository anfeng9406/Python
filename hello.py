def application(environ, start_response):
    start_response('200 ok',[('Content-Type','text/html')])
    return '<h1>Hello web!</h1>'

