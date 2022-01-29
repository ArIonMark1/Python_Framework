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
