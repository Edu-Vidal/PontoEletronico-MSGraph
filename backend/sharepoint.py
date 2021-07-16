from backend.connection import Connection


class SharepointConnector(Connection):
    def __init__(self):
        Connection.authenticate()

        self.root_folder = None
        self.current_user = None
        self.name = None

        self.connectSharepoint()

    def connectSharepoint(self) -> None:
        # here we get the storage instance that handles all the storage options.
        # to create instance we need to point the correct sharepoint site, which,
        # in this case, is not root, so needs to be specified
        site = self.account.sharepoint().get_site('snlv.sharepoint.com', '/sites/SNLV')
        my_drive = site.get_default_document_library()

        # Get instance of DriveItem for Sharepoint's root folder
        self.root_folder = my_drive.get_root_folder()

        # Get current user's Name instance
        self.current_user = self.account.get_current_user()
        self.name = self.current_user.display_name

    # class Check:
    #     @staticmethod
    #     def sharepointConnection(func):
    #         def wrapper(self, *args, **kwargs):
    #             if self.autenticado:
    #                 func(self, *args, **kwargs)
    #             else:
    #                 self.connectSharepoint()
    #                 func(self, *args, **kwargs)
    #         return wrapper


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
