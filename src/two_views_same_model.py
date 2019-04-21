import sys

from PySide2.QtCore import QStringListModel
from PySide2.QtWidgets import QApplication, QListView, QComboBox

if __name__ == '__main__':
    """
    Using a model to two different views
    """

    app = QApplication(sys.argv)

    # Let's make the QListWidget show this data
    data = ["ONE", "TWO", "THREE", "FOUR", "FIVE"]

    list_widget = QListView()
    list_widget.show()

    model = QStringListModel(data)

    # Setting the model to our QListView
    list_widget.setModel(model)

    # Another view
    comboBox = QComboBox()
    comboBox.show()

    # The new view uses the same model
    comboBox.setModel(model)

    sys.exit(app.exec_())
