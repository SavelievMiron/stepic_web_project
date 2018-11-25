#def app(environ, start_response):
#  start_response('200 OK',[('Content-Type','text/plain')])
#  start_response(status, response_headers)
#  body = [(i + '\n') for i in environ['QUERY_STRING'].split('&')]
#  return body

def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [bytes('\r\n'.join(environ['QUERY_STRING'].split('&')),encoding="utf8")]
