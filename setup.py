from setuptools import setup, find_packages

setup(
    name = 'django-simpleblocks',
    version = '0.1-alpha',
    url = 'https://github.com/alfredo/django-simpleblocks',
    description = 'Simple managed blocks for the templates',
    author = 'Alfredo Ramirez',
    author_email = 'alfredo.django@gmail.com',
    license = 'BSD',
    packages = find_packages('src'),
    package_dir = {'':'src'},
    install_requires = ['setuptools'],
    )
