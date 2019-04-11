# coding=utf-8
# Created by Meteorix at 2019/4/11
from setuptools import setup, find_packages


def parse_requirements(filename):
    """ load requirements from a pip requirements file. (replacing from pip.req import parse_requirements)"""
    lines = (line.strip() for line in open(filename))
    return [line for line in lines if line and not line.startswith("#")]


reqs = parse_requirements('requirements.txt')


setup(
    name='flaskweb',
    version='0.0.1',
    author='meteorix',
    author_email='lxhustauto@gmail.com',
    description='complete web framework from dev to production',
    packages=find_packages(exclude=['exampleapp', 'migrations', 'uploads']),
    include_package_data=True,
    install_requires=reqs,
)