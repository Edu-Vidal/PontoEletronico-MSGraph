from O365 import Account
import yaml
from backend.authenticate import Autenticador


class Connection:

    # Load the oauth_settings.yml file
    stream = open('oauth_settings.yml', 'r')
    settings = yaml.load(stream, yaml.SafeLoader)

    scopes = settings['scopes'].split(' ')
    client_id = settings['app_id']
    client_secret = settings['app_secret']
    tenant_id = settings['tenant_id']

    credentials = (client_id, client_secret)

    account = Account(credentials=credentials, scopes=scopes,
                      tenant_id=tenant_id, main_resource="site:SNLV")

    autenticado = True if account.is_authenticated else False

    @classmethod
    def authenticate(cls):
        if not cls.autenticado:
            Autenticador(cls.account)
            cls.autenticado = True

    class Check:
        @staticmethod
        def authentication(func):
            def wrapper(self, *args, **kwargs):
                if self.autenticado:
                    func(self, *args, **kwargs)
                else:
                    self.authenticate()
                    self.func(*args, **kwargs)
            return wrapper
