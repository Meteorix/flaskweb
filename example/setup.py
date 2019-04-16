# coding=utf-8
# Created by Meteorix at 2019/4/16
from setuptools import setup


setup(
    name='example',
    version='0.0.1',
    author='meteorix',
    author_email='lxhustauto@gmail.com',
    description='Example web app built with flaskweb',
    py_modules=["wsgi", "views", "models"],
    include_package_data=True,
    install_requires=['flaskweb'],
)
