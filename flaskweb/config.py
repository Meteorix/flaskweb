# coding=utf-8
# Created by Meteorix at 2019/4/10
import os
import logging
basedir = os.getcwd()


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SECRET_KEY = 'some thing secret'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOGGING_LEVEL = logging.INFO
    LOGGING_FILE = os.path.join(basedir, "app.log")


class DebugConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    LOGGING_LEVEL = logging.DEBUG


configs = {
    "base": Config,
    "debug": DebugConfig,
}
