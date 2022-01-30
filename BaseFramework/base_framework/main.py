import os
import sys
from pprint import pprint


def parse_input_data(data: str):
    res = {}
    if data:
        # делим данные через &
        params = data.split('&')
        print('data split: ', params)
        for item in params:
            # делим ключ и значение через =
            k, v = item.split('=')
            res[k] = v
    return res


def control_request(environ):
    request_method = environ['REQUEST_METHOD']
    content_length = environ['CONTENT_LENGTH']
    pprint(environ)
    print(content_length)
    # ###############################################################
    if request_method == 'POST' and int(content_length):
        data = environ['wsgi.input'].read(int(content_length))
        print(data)

        path = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(path, 'post_requests\\request.txt')

        # ............................................................
        with open(path, 'w', encoding='utf-8') as f:
            f.write(f' User data: {str(data.decode("utf-8"))}')
        # ............................................................

        # ###############################################################

        print(f'Data in query string: {environ["QUERY_STRING"]}')

        request_res = parse_input_data(environ["QUERY_STRING"])
        user_data = environ["wsgi.input"]
        print(f'User data in request POST: {user_data}')
        print(f'Data in query string: {request_res}')
        return request_method
    return request_method


class NotFoundPage:
    def __call__(self, request):
        return '404 ERROR', 'Page Not Found!!'


class Application:
    def __init__(self, routes, fronts):
        self.routes = routes
        self.fronts = fronts

    def __call__(self, environ, start_response):

        # ---------------------------
        path = environ['PATH_INFO']

        if not path.endswith('/'):
            path = f'{path}/'

        if path in self.routes:
            controller = self.routes[path]
            # .............................................
            return_request_data = control_request(environ)
            print(f'Page: == {environ["PATH_INFO"]} ==> Method: {return_request_data}')
            # .............................................
        else:
            controller = NotFoundPage()
        # ---- front controller -----
        request = {}
        for front_controller in self.fronts:
            front_controller(request, environ)

        # ----- page controller -----
        code, body = controller(request)
        # ---------------------------

        response_headers = [('Content-Text', 'file/html')]
        start_response(code, response_headers)

        return [body.encode('utf-8')]
