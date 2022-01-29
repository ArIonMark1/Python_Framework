from wsgiref.simple_server import make_server
from Geek_framework.BaseFramework.urls import routes
from Geek_framework.BaseFramework.base_framework.main import Application
from Geek_framework.BaseFramework.base_framework.front_controllers import fronts

if __name__ == '__main__':
    host = '127.0.0.1'
    port = 8888

    app = Application(routes, fronts)

    with make_server(host, port, app) as http:
        print(f'Server started with address {host} on port {port}...')
        http.serve_forever()
