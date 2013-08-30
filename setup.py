from distutils.core import setup

setup(
    name='django-gami',
    version="0.1",
    url='http://www.technigami.com/django-gami/',
    author='Technigami',
    author_email='info@technigami.com',
    description=('Some tools to help automate common processes in django'),
    license='GPL',
    packages=['gami'],
    scripts=['gami/bin/gami.py'],
    install_requires=[
        'fabric',
        'nose',
        'colorama',
        'gitpython',
        'virtualenvwrapper',
    ]
)
