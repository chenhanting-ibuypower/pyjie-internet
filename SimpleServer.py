# -*- coding: utf-8 -*-

from wsgiref.simple_server import make_server

# The application interface is a callable object
def application ( # It accepts two arguments:
    # environ points to a dictionary containing CGI like environment
    # variables which is populated by the server for each
    # received request from the client
    environ,
    # start_response is a callback function supplied by the server
    # which takes the HTTP status and headers as arguments
    start_response
):

    method = 'Request method: %s' % environ['REQUEST_METHOD']
    fixed_string = "YuJie is studying."

    request_body = ""
    
    try:
        request_body_size = int(environ['CONTENT_LENGTH'])
        request_body = method + "\n" + fixed_string + "\n" + environ['wsgi.input'].read(request_body_size)
    except (TypeError, ValueError):
        request_body = "0"
    try:
        response_body = str(request_body)
    except:
        response_body = "error"
    # Build the response body possibly
    # using the supplied environ dictionary


    # HTTP response code and message
    status = '200 OK'

    # HTTP headers expected by the client
    # They must be wrapped as a list of tupled pairs:
    # [(Header name, Header value)].
    response_headers = [
        ('Content-Type', 'text/json'),
        ('Content-Length', str(len(response_body)))
    ]

    # Send them to the server using the supplied function
    start_response(status, response_headers)

    # Return the response body. Notice it is wrapped
    # in a list although it could be any iterable.
    return [response_body.encode()]

httpd = make_server('localhost', 8000, application)
httpd.serve_forever()

# https://stackoverflow.com/questions/35886782/assertionerror-write-argument-must-be-a-bytes-instance-when-running-wsgisoa
# https://segmentfault.com/a/1190000013450695

