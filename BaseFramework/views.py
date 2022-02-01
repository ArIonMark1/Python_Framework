import datetime

from Geek_framework.BaseFramework.base_framework.template_conrtoller import render_temp


# ======= Page Controllers =======
def main_page(request):
    time = datetime.datetime.now()
    context = {'header': 'Index Page', 'content': 'Hello From beginning, this is the main page of my site.', 'time': time}

    return '200 OK', render_temp('index.html', context=context)


def about_page(request):
    context = {'header': 'About Page',
               'content': '-- Здесь можно посмотреть информацию сайта, в будущем возможно, здесь что то будет. --'}
    return '200 OK', render_temp('about.html', context=context)


def contacts_page(request):
    context = {'header': 'Contact Page',
               'descriptor': "-- Contact page of my site. --",
               'email': "Example123@gmail.com",
               'reg1': "+8 800 700-68-41",
               'reg2': "+7 499 922-47-10",
               'support': "support@geekbrains.ru --"}

    return '200 OK', render_temp('contacts.html', context=context)
