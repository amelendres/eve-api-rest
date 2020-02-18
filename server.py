import os
import logging
from eve import Eve
from eve.auth import TokenAuth

company = "COMPANYA"

class TokenAuth(TokenAuth):
    def check_auth(self, token, allowed_roles, resource, method):
       
        accounts = app.data.driver.db["accounts"]
        account = accounts.find_one({"token": token})
        if account == None:
        	app.logger.info('ERROR: Autenticate with token "%s" ' % token)
        else:
        	company = logged_account["company"]
        
        return logged_account



def add_company(items):
    for document in items:
    	document['company']=company

def log_every_get(resource, request, payload):
    app.logger.info('request: "%s" ' % request)

app = Eve()
app.on_insert_employe += add_company
#app.on_post_GET += log_every_get

if __name__ == '__main__':

    handler = logging.FileHandler('./log/app.log')

    handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(filename)s:%(lineno)d] -- ip: %(clientip)s, '
        'url: %(url)s, method:%(method)s'))

    app.logger.setLevel(logging.INFO)

    app.logger.addHandler(handler)

    app.run(host='0.0.0.0')

