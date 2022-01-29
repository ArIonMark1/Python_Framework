import datetime


# ======= Front Controller =======

def check_token(request, environ):
    request['data'] = datetime.datetime.now()

    print(environ['PATH_INFO'], 'action:', environ['REQUEST_METHOD'])
    request['action'] = environ['REQUEST_METHOD']


def some_secret(request, environ):
    request['name'] = 'WebFramework'


fronts = [check_token, some_secret]
