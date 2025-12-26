import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:YOUR_PASSWORD@localhost:5432/studentDB"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = False
