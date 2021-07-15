from O365.excel import WorkBook
from datetime import datetime, time
from backend.sharepoint import SharepointConnector


class XlsxEditor():

    def __init__(self, current_user, root_folder):
        self.now = datetime.now()
        self.todaysRow = (None, None)
        self.todaysData = ''
        self.current_user = current_user

        # Busca arquivo com dados do ponto
        self.excelFile = next(root_folder.search('Banco_de_Horas.xlsx'))

        self.getWorkBook()

    def getWorkBook(self):
        # MUDAR --> Na estrutura de excel atual cada funcionário possui uma
        # tabela em um só arquivo
        wb = WorkBook(self.excelFile)
        self.ws = wb.get_worksheet(self.current_user.display_name)

        self.findTodaysRow()

        self.fetchTodaysData()

    def createWorkSheet(self) -> None:
        # Caso não haja arquivo criado para o funcionário
        pass

    def findTodaysRow(self) -> None:
        today_s = self.now.strftime('%d/%m/%y')
        # Retorna linha que representa o dia de hoje
        # IMPLEMENTAR -> se ainda não existir é criada
        rng = self.ws.get_range("B10:B1000")
        # Garante receber toda a coluna -?-
        datas = [data[0] for data in rng.text if data != ['']]
        for data in datas:
            if data == today_s:
                self.todaysRow = (datas.index(data) + 10, self.now.day)
                break
        # else:
        #     Adiciona linha à WorkSheet

    def updateData(self, event):
        # Confirma se linha atual representa o dia de hoje
        self.now = datetime.now()
        if self.todaysRow[1] != self.now.day:
            self.findTodaysRow()

        # Parâmetros para inserção dos dados
        column = {'entrada': "C", 'inicio_intervalo': "D",
                  'fim_intervalo': "E", 'saida': "F"}
        # Preenche dados para evento indicado
        cell = self.ws.get_range(f'{column[event]}{self.todaysRow[0]}')
        cell.values = self.now.strftime("%H:%M")
        cell.update()

    def fetchTodaysData(self):
        self.todaysData = [data for data in self.ws.get_range(
            f"C{self.todaysRow[0]}:F{self.todaysRow[0]}").text[0] if data != '']


if __name__ == "__main__":
    editor = XlsxEditor()
    print(editor.fetchTodaysData())
