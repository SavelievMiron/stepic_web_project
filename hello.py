#def application(environ, start_response):
#   start_response('200 OK',[('Content-type','text/plain')])
#  start_response(status, response_headers)
#    resp = environ['QUERY_STRING'].split("&")
#   resp = [item+"\r\n" for item in resp]
#   return resp
from cgi import parse_qs

def application(environ, start_response):

  query = parse_qs(environ['QUERY_STRING'], keep_blank_values=True)
  body = []
  for key, values in query.items():
    for item in values:
      body.append(key + "=" + item + "\r\n")
   
  status = '200 OK'
  headers = [
   ('Content-Type', 'text/plain')
  ]
  
  start_response(status, headers)
  return body
  
