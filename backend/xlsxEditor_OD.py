from O365.excel import WorkBook
from datetime import datetime, time
from SharepointConnection import excelFile


class XlsxEditor():

    def __init__(self):
        # MUDAR --> Na estrutura de excel atual cada funcionário possui uma
        # tabela em um só arquivo
        wb = WorkBook(excelFile)

    def rowFinder(self) -> int:
        # Retorna linha que representa o dia de hoje,
        # se ainda não existir é criada
        return

    def insertData(self, evento):
        # Retorna dados preenchidos hoje
        return None

    def writeExcel(self) -> None:
        for ws in self.wb.get_worksheets():
            cella1 = ws.get_range('A1')
            print(cella1.values)

        # self.wb.save(self.xlsxFilePath)
