from pprint import pprint
from wsgiref.simple_server import make_server
from Geek_framework.BaseFramework.urls import routes
from base_framework.front_controllers import check_token


class NotFoundPage:
    def __call__(self, request):
        return '404 ERROR', 'Page Not Found!!'


class Application:
    def __init__(self, routes):
        self.routes = routes

    def __call__(self, environ, start_response):

        # ---------------------------
        path = environ['PATH_INFO']

        if not path.endswith('/'):
            path = f'{path}/'

        if path in self.routes:
            controller = routes[path]
        else:
            controller = NotFoundPage()
        # ---- front controller -----
        request = {}
        check_token(request, environ)

        # ----- page controller -----
        code, body = controller(request)
        # ---------------------------
        response_headers = [('Content-Text', 'file/html')]
        start_response(code, response_headers)

        return [body.encode('utf-8')]


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 8888

    app = Application(routes)

    with make_server(host, port, app) as http:
        print(f'Server started with address {host} on port {port}...')
        http.serve_forever()
