'''
Created on 6 february 2017

@author:  Cyril Jacquet
'''

from PyQt5.QtCore import QAbstractListModel, QVariant, QModelIndex, QSettings, QDateTime
from PyQt5.Qt import QUndoStack
from PyQt5.QtCore import Qt, QObject, pyqtSlot, QByteArray
from .. import cfg

class ProjectListModel(QAbstractListModel):

    TitleRole = Qt.UserRole
    PathRole = Qt.UserRole + 1
    LastOpenedDate = Qt.UserRole + 2


    def __init__(self, parent: QObject):
        super(ProjectListModel, self).__init__(parent)

        # inheriting classes will start at Qt.UserRole + 20

        self._root_node = ListItem()
        self._node_list = []
        self._undo_stack = QUndoStack(self)
        self.size_limit = 5

        cfg.data.projectHub().projectLoaded.connect(self.reset_model)
        self.reset_model()


    def rowCount(self, parent=None):

        if parent.column() > 0:
            return 0

        if not parent.isValid():
            parent_node = self._root_node

            return len(parent_node)
        else:
            parent_node = self.node_from_index(parent)
            return len(parent_node)

    # def headerData(self, section, orientation, role):
    #     if orientation == Qt.Horizontal and role == Qt.DisplayRole:
    #         return QVariant(self.headers[section])
    #     return QVariant()

    def index(self, row, column, parent):
        if not self.hasIndex(row, column, parent):
            return QModelIndex()

        node = self.node_from_index(parent)
        return self.createIndex(row, column, node.child_at_row(row))

    def data(self, index, role):

        row = index.row()
        col = index.column()

        if not index.isValid():
            return QVariant()

        node = self.node_from_index(index)

        if role == self.PathRole and col == 0:
            return node.path
        if role == self.LastOpenedDate and col == 0:
            return node.last_opened_date
        if role == self.TitleRole and col == 0:
            return node.title
        return QVariant()

    def node_from_index(self, index):
        return index.internalPointer() if index.isValid() else self._root_node



    def parent(self, child):
        if not child.isValid():
            return QModelIndex()

        node = self.node_from_index(child)

        if node is None:
            return QModelIndex()

        parent = node.parent
        if parent == self._root_node:
            return QModelIndex()

        if parent is None:
            return QModelIndex()

        # needed to know if
        grandparent = parent.parent
        if grandparent is None:
            return QModelIndex()
        row = grandparent.row_of_child(parent)

        assert row != - 1
        index = self.createIndex(row, 0, parent)
        parent.index = index
        return index


#------------------------------------------
#------------------Editing-----------------
#------------------------------------------

    def setData(self, index, value, role):

        limit = [role]

        # # title :
        # if index.isValid() & role == self.TitleRole & index.column() == 0:
        #
        #     node = self.node_from_index(index)
        #
        #     self.tree_db.set_title(node.id, value)
        #     node.title = value
        #
        #     self.dataChanged.emit(index, index, limit)
        #     return True

        return False

    def flags(self, index):
        default_flags = QAbstractListModel.flags(self, index)

        if index.isValid():
            return Qt.ItemIsEditable | Qt.ItemIsDragEnabled | \
                    Qt.ItemIsDropEnabled | default_flags

        else:
            return Qt.ItemIsDropEnabled | default_flags

    def reset_model(self):
        self.beginResetModel()

        del self._root_node
        self._root_node = ListItem()
        self._node_list = []

        settings = QSettings(self)
        settings.beginGroup("Welcome")
        array_size = settings.beginReadArray("recent_projects")
        # apply number limit
        if array_size > 5:
            array_size = self.size_limit
        # load:
        for i in range(array_size):
            settings.setArrayIndex(i)
            path = str(settings.value("path"))
            title = str(settings.value("title"))
            last_opened_date = settings.value("date", type=QDateTime)

            item = ListItem(self._root_node)
            item.title = title
            item.path = path
            item.last_opened_date = last_opened_date
            self._node_list.append(item)
            self._root_node.append_child(item)
        settings.endArray()
        settings.endGroup()

        self.endResetModel()

    def clear(self):
        self.beginResetModel()
        self._root_node = ListItem()
        self._node_list = []
        self.endResetModel()

    # def insertRow(self, row, parent):
    #     return self.insertRows(row, 1, parent)
    #
    #
    # def insertRows(self, row, count, parent):
    #     self.beginInsertRows(parent, row, (row + (count - 1)))
    #
    #     self.id_of_last_created_node = \
    #         cfg.data.database.get_tree(self._table_name).add_new_papers_by(self.node_from_index(parent).id, count)
    #     self.endInsertRows()
    #     return True
    #
    #
    # def removeRow(self, row, parentIndex):
    #     return self.removeRows(row, 1, parentIndex)
    #
    #
    # def removeRows(self, row, count, parentIndex):
    #     # TODO wrong
    #     self.beginRemoveRows(parentIndex, row, row)
    #     cfg.data.database.get_tree(self._table_name).remove_papers(self.node_from_index(parent).id, count)
    #     self.endRemoveRows()
    #
    #     return True




    def find_index_from_id(self, id_: int):
        for node in self._node_list:
            if node.id == id_:
                return node.index

        return None


# TODO : drag drop
#     def mimeData(self, list_of_QModelIndex):
#         custom_mime_data = QMimeData()
#         encoded_data = QByteArray()
#
#         stream = QDataStream(encoded_data, QIODevice.WriteOnly)
#
#         for index in list_of_QModelIndex:
#             if index.isValid():
#                 stream.writeQVariant(self.node_from_index(index).data)
#
#         custom_mime_data.setData("application/plume-creator-tree", encoded_data)
#
#         return custom_mime_data
#
#     def mimeTypes(self):
#         return ["application/plume-creator-tree"]
#
#     def dropMimeData(self, mimedata, action, row, column, parentIndex):
#         if action == Qt.IgnoreAction:
#             return True
#
#         if
#
#         return True

    def supportedDropActions(self):
        return Qt.CopyAction

    def insertRow(self, row, parent):
        return self.insertRows(row, 1, parent)

    def insertRows(self, row, count, parent):
        self.beginInsertRows(parent, row, (row + (count - 1)))
        self.endInsertRows()
        return True

    def removeRow(self, row, parentIndex):
        return self.removeRows(row, 1, parentIndex)

    def removeRows(self, row, count, parentIndex):
        self.beginRemoveRows(parentIndex, row, row)
        self.endRemoveRows()
        return True


    @property
    def undo_stack(self)->QUndoStack:
        return self._undo_stack

    def set_undo_stack_active(self):
        self._undo_stack.setActive(True)


# for access from QML :
    def roleNames(self):
        return {self.TitleRole: QByteArray().append("title"),
                # self.TitleRole: QByteArray().append("content"),
                self.PathRole: QByteArray().append("path"),
                self.LastOpenedDate: QByteArray().append("last_opened_date")
                }


class ListItem(object):

    def __init__(self, parent=None):
        super(ListItem, self).__init__()

        self.data = {}
        self.index = QModelIndex()
        self.parent_id = None
        self.children_id = None

        self._parent = None

        self.parent = parent
        self.children = []

        self.title = ""
        self.path = ""
        self.last_opened_date = ""


    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        if parent is not None:
            self._parent = parent
        else:
            self._parent = None

    def append_child(self, child):
        if child not in self.children:
            self.children.append(child)

    def child_at_row(self, row):
        return self.children[row]

    def row_of_child(self, child):
        for i, item in enumerate(self.children):
            if item == child:
                return i
        return -1

    def remove_child(self, row):
        value = self.children[row]
        self.children.remove(value)

        return True

    def row(self):
        if self._parent:
            return int(self._parent.children.index(self))
        return -1

    def __len__(self):
        return len(self.children)

