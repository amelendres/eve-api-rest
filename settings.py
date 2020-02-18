import os

MONGO_URI = os.getenv('MONGO_URI')
PAGINATION = False
HATEOAS = False
DEBUG = True

URL_PREFIX= 'api'

DOMAIN = {
    'employe': {
        'schema': {
            'firstname': {
                'type': 'string',
                'required': True
            },
            'lastname': {
                'type': 'string',
                'required': True
            },
            'email': {
                'type': 'string',
                'regex': '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
            },
            'position': {
                'type': 'string'
            },
            'office': {
                'type': 'string'
            },
            'salary': {
                'type': 'float'
            },
            'weeklyWorkHours': {
                'type': 'integer'
            },
            'picture': {
                'type': 'media'
            },
            'company': {
                'type': 'string'
            }
        }
    },
    'accounts': {
        'schema': {
            'username': {'type': 'string', 'minlength': 5, 'maxlength': 20},
            'password': {'type': 'string', 'minlength': 5, 'maxlength': 20},
            'secret_key': {'type': 'string', 'minlength': 5, 'maxlength': 20},
            'roles': {'type': 'string', 'minlength': 10, 'maxlength': 50},
            'token': {'type': 'string', 'minlength': 10, 'maxlength': 50},
            'company': {'type': 'string'}
        }
    }
}

RESOURCE_METHODS = ['GET', 'POST']
ITEM_METHODS = ['GET','PUT', 'DELETE', 'PATCH']

X_DOMAINS= '*'
X_HEADERS = ['Content-Type','Authorization','If-Match']

#RETURN_MEDIA_AS_BASE64_STRING = False
RETURN_MEDIA_AS_URL = True




