from distutils.core import setup

setup(name='django-simpleblocks',
      version='0.1-alpha',
      description='Simple blocks for your templates',
      author='Alfredo Ramirez Aguirre',
      author_email='aguirre.alfred07@gmail.com',
      url='http://github.com/alfredo/',
      packages=['simpleblocks', 'simpleblocks.templatetags'],
      classifiers=['Development Status :: 0.1 Alpha',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
      )
