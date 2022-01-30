import datetime
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


# ======= Front Controller =======

def check_token(request, environ):
    request['data'] = datetime.datetime.now()
    request['control_token'] = 'my_token'

    # print('==', environ['PATH_INFO'], '==>', 'action:', environ['REQUEST_METHOD'], environ['QUERY_STRING'])
    # pprint(environ)

    # if environ['REQUEST_METHOD'] == 'POST':
    #     print(f'Data in query string: {environ["QUERY_STRING"]}')
    #
    #     request_res = parse_input_data(environ["QUERY_STRING"])
    #     print(request_res)
    #
    #     user_data = environ["wsgi.input"]
    #     print(f'User data in request POST: {user_data}')
    request['action'] = environ['REQUEST_METHOD']


def some_secret(request, environ):
    request['name'] = 'WebFramework'


fronts = [check_token, some_secret]
