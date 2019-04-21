import sys

from PySide2.QtCore import QAbstractListModel, Qt
from PySide2.QtGui import QColor, QPixmap, QIcon
from PySide2.QtWidgets import QApplication, QListView, QComboBox, QTreeView, QTableView


class PalletListModel(QAbstractListModel):

    """
    It'll receive a list of colors and a parent
    """
    def __init__(self, colors=None, parent=None):
        QAbstractListModel.__init__(self, parent)

        if colors is None:
            colors = []
        self.__colors = colors

    def headerData(self, section, orientation, role=None):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return "Palette"
            else:
                return "Color {}".format(section)

    def data(self, index, role=None):
        # The data in a form suitable for editing in an editor. (QString)
        if role == Qt.EditRole:
            return self.__colors[index.row()].name()

        # The data displayed in the item's tooltip. (QString)
        if role == Qt.ToolTipRole:
            return "Hex code: " + self.__colors[index.row()].name()

        # The data to be rendered as a decoration in the form of an icon. (QColor, QIcon or QPixmap)
        if role == Qt.DecorationRole:
            row = index.row()
            value = self.__colors[row]

            pixmap = QPixmap(30, 30)
            pixmap.fill(value)

            icon = QIcon(pixmap)

            return icon

        # The key data to be rendered in the form of text. (QString)
        if role == Qt.DisplayRole:
            row = index.row()
            value = self.__colors[row]

            return value.name()

    # One dimensional data, thus ignoring parent argument
    def rowCount(self, parent=None):
        return len(self.__colors)

    def flags(self, index):
        """
        Let's make our model editable
        """
        return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def setData(self, index, value, role=Qt.EditRole):
        if role == Qt.EditRole:
            row = index.row()

            color = QColor(value)

            if color.isValid():
                self.__colors[row] = color
                self.dataChanged.emit(index, index)
                return True

        return False


if __name__ == '__main__':
    """
    Using a custom model for different views
    All views will show the same data
    """

    app = QApplication(sys.argv)

    # Let's create some views:
    list_view = QListView()
    list_view.show()

    tree_view = QTreeView()
    tree_view.show()

    comboBox = QComboBox()
    comboBox.show()

    table_view = QTableView()
    table_view.show()

    # Our colors
    red = QColor(255, 0, 0)
    green = QColor(0, 255, 0)
    blue = QColor(0, 0, 255)

    model = PalletListModel([red, green, blue])

    list_view.setModel(model)
    tree_view.setModel(model)
    comboBox.setModel(model)
    table_view.setModel(model)

    sys.exit(app.exec_())
