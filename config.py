import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or \
                 b'HA\xdb\xe0\x94X\xe4\xb7\xe1\xfb\x04j\x9a\x19\xc5\xb7'

    # MONGODB_SETTINGS = {'db': 'UTA_Enrollment',
    #                     'host': 'mongodb://localhost:27017/UTA_Enrollment'
    #                     }

    MONGODB_SETTINGS = { 'db': 'UTA_Enrollment' }