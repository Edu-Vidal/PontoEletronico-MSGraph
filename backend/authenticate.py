import os
from threading import Timer
from flask import Flask, redirect, request
from flask_classful import FlaskView, route
import yaml
import webbrowser
# import logging

# Implementação de app Flask com classes através do "flask_classful"


class _WebAuth(FlaskView):
    # This is necessary for non-HTTPS localhost
    # Remove this if deploying to production
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

    # This is necessary because Azure does not guarantee
    # to return scopes in the same case and order as requested
    os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'
    os.environ['OAUTHLIB_IGNORE_SCOPE_CHANGE'] = '1'

    callback = "http://localhost:8000/steptwo"
    state = ''
    account = None

    @route('/')
    @route('/stepone')
    def auth_step_one(self):
        url, self.state = self.account.con.get_authorization_url(
            redirect_uri=self.callback
        )
        # Scopes
        # 'basic' adds: 'offline_access' and 'https://graph.microsoft.com/User.Read'
        # 'message_all' adds: 'https://graph.microsoft.com/Mail.ReadWrite' and 'https://graph.microsoft.com/Mail.Send'
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

    def checkBussinessAccount(self) -> bool:
        # Verifica se conta inserida pertence a alguma empresa
        pass

    def shutdown(self) -> None:
        func = request.environ.get('werkzeug.server.shutdown')
        if func is None:
            raise RuntimeError('Not running with the Werkzeug Server')
        func()


class Autenticador():
    def __init__(self, account):
        self.app = Flask('AuthApp')
        self.account = account

        _WebAuth.account = account

        self.autentique()

    def autentique(self):
        # Attaches an instance of WebAuth to app
        _WebAuth.register(self.app, route_base='/')

        # the default protocol will be Microsoft Graph
        # the default authentication method will be "on behalf of a user"

        if not self.account.is_authenticated:
            webbrowser.open_new_tab("http://localhost:8000/stepone")
            self.app.run(port=8000, threaded=True)


if __name__ == "__main__":
    Autenticador()
