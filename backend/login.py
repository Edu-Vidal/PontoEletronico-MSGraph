from O365 import Account
import yaml

# Load the oauth_settings.yml file
stream = open('oauth_settings.yml', 'r')
settings = yaml.load(stream, yaml.SafeLoader)
scopes = settings['scopes'].split(' ')
client_id = settings['app_id']
client_secret = settings['app_secret']
tenant_id = settings['tenant_id']

credentials = (client_id, client_secret)

# the default protocol will be Microsoft Graph
# the default authentication method will be "on behalf of a user"

account = Account(credentials, scopes=scopes, tenant_id=tenant_id)
if account.authenticate(redirect_uri=f"https://login.microsoftonline.com/{tenant_id}/oauth2/nativeclient"):
   print('Authenticated!')

# 'basic' adds: 'offline_access' and 'https://graph.microsoft.com/User.Read'
# 'message_all' adds: 'https://graph.microsoft.com/Mail.ReadWrite' and 'https://graph.microsoft.com/Mail.Send'
