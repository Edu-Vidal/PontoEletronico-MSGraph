from O365.excel import WorkBook
from datetime import datetime, time
from backend.sharepoint import SharepointConnector


class XlsxEditor(SharepointConnector):

    def __init__(self):
        super().__init__()
        # MUDAR --> Na estrutura de excel atual cada funcionário possui uma
        # tabela em um só arquivo
        wb = WorkBook(self.excelFile)
        self.ws = wb.get_worksheet(self.name.display_name)

        self.now = datetime.now()
        self.todaysRow = self.findTodaysRow()

    def createSheet(self) -> None:
        # Caso não haja arquivo criado para o funcionário
        pass

    def findTodaysRow(self) -> int:
        today_s = self.now.strftime('%d/%m/%y')
        # Retorna linha que representa o dia de hoje
        # IMPLEMENTAR -> se ainda não existir é criada
        rng = self.ws.get_range("B10:B1000")
        # Garante receber toda a coluna -?-
        datas = [data[0] for data in rng.text if data != ['']]
        for data in datas:
            if data == today_s:
                return datas.index(data)+10

    def updateData(self, event):
        # Parâmetros para inserção dos dados
        column = {'entrada': "C", 'inicio_intervalo': "D",
                  'fim_intervalo': "E", 'saida': "F"}
        # Preenche dados para evento indicado
        cell = self.ws.get_range(f'{column[event]}{self.todaysRow}')
        cell.values = self.now.strftime("%H:%M")
        cell.update()

    def fetchTodaysData(self):
        return [data for data in self.ws.get_range(f"C{self.todaysRow}:F{self.todaysRow}").text[0] if data != '']


if __name__ == "__main__":
    editor = XlsxEditor()
    print(editor.fetchTodaysData())
