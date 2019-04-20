import sys

from PySide2.QtWidgets import QApplication, QListWidget

if __name__ == '__main__':

    app = QApplication(sys.argv)

    list_widget = QListWidget()
    list_widget.show()

    sys.exit(app.exec_())