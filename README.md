Написать свой wsgi фреймворк использую паттерны page controller и front controller. Описание работы фреймворка:
возможность отвечать на get запросы пользователя (код ответа + html страница)
для разных url - адресов отвечать разными страницами page controller - возможность без изменения фреймворка добавить
view для обработки нового адреса front controller - возможность без изменения фреймворка вносить изменения в обработку
всех запросов

Реализовать рендеринг страниц с помощью шаблонизатора jinja2. Документацию по этой библиотеке можно найти в
дополнительных материалах

Complete == Добавить любый полезный функционал в фреймворк, например обработку наличия (отсутствия) слеша в конце
адреса, ...

Complete == Добавить для демонстрации 2 любые разные страницы (например главная и about или любые другие)

Сдать дз в виде ссылки на репозиторий

Проект запускается с файла manage.py.

###### #########################################################

Тренируем умения:

- Разделять get и post запрос внутри wsgi-фреймворка
- Получать и декодировать параметры post запроса

-------------------------------------------------
Задание:

- Добавить в свой wsgi-фреймворк возможность обработки post-запроса
- Добавить в свой wsgi-фреймворк возможность получения данных из post запроса
- Дополнительно можно добавить возможность получения данных из get запроса
- В проект добавить страницу контактов на которой пользователь может отправить нам сообщение (пользователь вводит тему
  сообщения, его текст, свой email)
- После отправки реализовать сохранение сообщения в файл, либо вывести сообщение в терминал (базу данных пока не
  используем)

Данные из POST запроса можно посмотреть в дирректории post_requests в файле request.txt

