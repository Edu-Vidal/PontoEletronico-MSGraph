import os
from O365 import Account
from flask import Flask, redirect, request
from flask_classful import FlaskView, route
import yaml
# import logging

# This is necessary for non-HTTPS localhost
# Remove this if deploying to production
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

# This is necessary because Azure does not guarantee
# to return scopes in the same case and order as requested
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'
os.environ['OAUTHLIB_IGNORE_SCOPE_CHANGE'] = '1'

# Load the oauth_settings.yml file
stream = open('oauth_settings.yml', 'r')
settings = yaml.load(stream, yaml.SafeLoader)
scopes = settings['scopes'].split(' ')
client_id = settings['app_id']
client_secret = settings['app_secret']
tenant_id = settings['tenant_id']

credentials = (client_id, client_secret)

app = Flask(__name__)


class LoginApp(FlaskView):
    account = Account(credentials, tenant_id=tenant_id)
    callback = "http://localhost:8000/steptwo"
    state = ''

    @route('/')
    @route('/stepone')
    def auth_step_one(self):
        url, self.state = self.account.con.get_authorization_url(
            requested_scopes=scopes,
            redirect_uri=self.callback
        )
        return redirect(url)

    @route('/steptwo')
    def auth_step_two_callback(self):
        result = self.account.con.request_token(request.url,
                                                state=self.state,
                                                redirect_uri=self.callback)
        # if result is True, then authentication was succesful
        #  and the auth token is stored in the token backend
        if result:
            self.shutdown()
            return "<h3>Autenticação Completa</h3>"
        else:
            return "<h3>Autenticação mal sucedida, cheque seus dados</h3>"

    def shutdown(self) -> None:
        func = request.environ.get('werkzeug.server.shutdown')
        if func is None:
            raise RuntimeError('Not running with the Werkzeug Server')
        func()


LoginApp.register(app, route_base='/')

# the default protocol will be Microsoft Graph
# the default authentication method will be "on behalf of a user"

account = LoginApp.account
if not account.is_authenticated:
    app.run(port=8000)

# Scopes
# 'basic' adds: 'offline_access' and 'https://graph.microsoft.com/User.Read'
# 'message_all' adds: 'https://graph.microsoft.com/Mail.ReadWrite' and 'https://graph.microsoft.com/Mail.Send'
