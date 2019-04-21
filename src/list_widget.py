import sys

from PySide2.QtWidgets import QApplication, QListWidget

if __name__ == '__main__':

    app = QApplication(sys.argv)

    # Let's make the QListWidget show this data
    data = ["ONE", "TWO", "THREE", "FOUR", "FIVE"]

    list_widget = QListWidget()
    list_widget.show()
    list_widget.addItems(data)

    sys.exit(app.exec_())
