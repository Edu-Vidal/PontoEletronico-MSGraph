from backend.sharepoint import SharepointConnector

from backend.services.xlsxEditor import XlsxEditor


class Manager(SharepointConnector):

    def __init__(self, excel=True, email=False):
        super().__init__()

        self.excel = self.excel() if excel else None
        # self.email = self.email() if email else None -> Example
        # ...

    def excel(self):
        return XlsxEditor(self.current_user, self.root_folder)
