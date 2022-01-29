import os.path
from os.path import join
from pathlib import Path

from jinja2 import Template


def render_temp(template_name, name_folder=join(Path(__file__).parents[1], 'templates'), **kwargs):

    template_path = join(name_folder, template_name)

    with open(template_path, encoding='utf-8') as file:
        template = Template(file.read())

        return template.render(**kwargs)


if __name__ == '__main__':

    context = {'title': 'Main Page'}
    render_temp('index.html', context=context)
