import sys

from PySide2 import QtCore
from PySide2.QtWidgets import QApplication, QListWidget, QComboBox

if __name__ == '__main__':
    """
    Two views using each one a instance of our data
    """

    app = QApplication(sys.argv)

    # Let's make the QListWidget show this data
    data = ["ONE", "TWO", "THREE", "FOUR", "FIVE"]

    list_widget = QListWidget()
    list_widget.show()
    list_widget.addItems(data)

    # Let's make elements on QListWidget editable
    for index in range(list_widget.count()):
        item = list_widget.item(index)
        item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)

    # A comboBox showing the same data
    comboBox = QComboBox()
    comboBox.show()
    comboBox.addItems(data)

    sys.exit(app.exec_())
