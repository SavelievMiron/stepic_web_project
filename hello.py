def application(environ, start_response):
  start_response('200 OK',[('Content-Type','text/plain')])
  start_response(status, response_headers)
  resp = environ['QUERY_STRING'].split("&")
  resp = [item+"\r\n" for item in resp]
  return resp

