from O365 import Account
import yaml


class SharepointConnector():
    def __init__(self):
        # Load the oauth_settings.yml file
        stream = open('oauth_settings.yml', 'r')
        settings = yaml.load(stream, yaml.SafeLoader)

        scopes = settings['scopes'].split(' ')
        client_id = settings['app_id']
        client_secret = settings['app_secret']
        tenant_id = settings['tenant_id']

        credentials = (client_id, client_secret)

        self.account = Account(credentials=credentials, scopes=scopes, tenant_id=tenant_id,
                               main_resource="site:SNLV")

        self.root_folder = None
        self.excelFile = None
        self.name = None
        self.connect()

    def connect(self) -> None:
        # here we get the storage instance that handles all the storage options.
        # to create instance we need to point the correct sharepoint site, which,
        # in this case, is not root, so needs to be specified
        site = self.account.sharepoint().get_site('snlv.sharepoint.com', '/sites/SNLV')
        my_drive = site.get_default_document_library()
        self.root_folder = my_drive.get_root_folder()
        # Get file with timeclock data
        self.excelFile = next(self.root_folder.search('Banco_de_Horas.xlsx'))
        self.name = self.account.get_current_user()


# For tests
if __name__ == "__main__":
    sharepoint = SharepointConnector()
    # print items in Documents folder
    for item in sharepoint.root_folder.get_items(limit=25):
        if item.is_folder:
            print(item)
            print(list(item.get_items(2)))
        else:
            print(item.mime_type)

    print(sharepoint.name)
