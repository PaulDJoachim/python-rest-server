import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
  SQLALCHEMY_DATABASE_URI = "postgresql://postgres:5236987410@localhost:5432/cars_api"
  SQLALCHEMY_TRACK_MODIFICATIONS = False