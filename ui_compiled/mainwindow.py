# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow

from main_menu_ui import Ui_Dialog
from docx import Document
def debug_replace_notable(template_path, output_path,data):# no table
    doc=Document(template_path)
    for paragraph in doc.paragraphs:
        for key, value in data.items():
            if key in paragraph.text:
               for run in paragraph.runs:
                   run.text=run.text.replace(key, value)
    doc.save(output_path)
def debug_replace(template_path, output_path,data):
    doc=Document(template_path)
    for table in doc.tables:
            table.cell(0,1).text="hyyyi"

    doc.save(output_path)
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()

    data = {
        "date_placeholder":"1488"
    }

    debug_replace("C:\MHAD\zaya.docx","C:\MHAD\zayavka.docx",data)#zamenyaet no ne v tablice

    widget.show()
    sys.exit(app.exec())

