import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'D8\xb4\x9c4\t\xac\x7f\xd9|F/"Y(F'

    MONGODB_SETTINGS = { 'db' : 'UTA_Enrollment' }
    
