import os
import logging
from eve import Eve
from eve.auth import TokenAuth

#from settings_security import SETTINGS

company = "COMPANYA"

class TokenAuth(TokenAuth):
    def check_auth(self, token, allowed_roles, resource, method):
        """For the purpose of this example the implementation is as simple as
        possible. A 'real' token should probably contain a hash of the
        username/password combo, which should be then validated against the
        account data stored on the DB.
        """
        # use Eve's own db driver; no additional connections/resources are used
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

def add_signature(resource, response):
	response['SIGNATURE'] = "A %s from test" % resource

def log_every_get(resource, request, payload):
    # custom INFO-level message is sent to the log file
    app.logger.info('request: "%s" ' % request)

#app = Eve(auth=TokenAuth, settings=SETTINGS)
app = Eve()
app.on_insert_employe += add_company
app.on_fetched_item += add_signature
#app.on_post_GET += log_every_get

if __name__ == '__main__':

    # enable logging to 'app.log' file
    handler = logging.FileHandler('./log/app.log')

    # set a custom log format, and add request
    # metadata to each log line
    handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(filename)s:%(lineno)d] -- ip: %(clientip)s, '
        'url: %(url)s, method:%(method)s'))

    # the default log level is set to WARNING, so
    # we have to explicitly set the logging level
    # to INFO to get our custom message logged.
    app.logger.setLevel(logging.INFO)

    # append the handler to the default application logger
    app.logger.addHandler(handler)

    # let's go
    app.run(host='0.0.0.0')

