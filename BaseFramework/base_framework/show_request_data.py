import os
from chardet import detect


# -----------------------------------------
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


# -----------------------------------------

def control_request(environ):
    request_method = environ['REQUEST_METHOD']
    content_length = environ['CONTENT_LENGTH']

    print(f'Длина переданых данных: {content_length}')
    #
    if request_method == 'POST':

        byte_data = environ['wsgi.input'].read(int(content_length))
        encod = detect(byte_data)['encoding']
        #
        # **********************************************
        path = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(path, 'post_requests\\request.txt')
        # **********************************************
        #
        # ............................................................
        with open(path, 'w', encoding='utf-8') as f:
            data_string = byte_data.decode(encod)
            data_string = parse_input_data(data_string)
            f.write(f' User data: {data_string}')
        # ............................................................

        # ###############################################################

        print(f'Data in query string: {environ["QUERY_STRING"]}')
        request_res = parse_input_data(environ["QUERY_STRING"])

        print(f'Data in query string: {request_res}')

        return request_method

    elif request_method == 'GET':

        return request_method
    else:

        return f'Сайт поддерживает только GET и POST запросы!!! Был вызван: {request_method}'

# -----------------------------------------
