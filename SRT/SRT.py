###############################################################################
# Name: 
#   Set_SRT
#
###############################################################################
 
from PySide import QtCore
from PySide import QtGui
 
from shiboken import wrapInstance
 
import maya.cmds as cmds
import maya.OpenMayaUI as omui
 
def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QtGui.QWidget)
     
class Set_SRT(QtGui.QDialog):
     
    def __init__(self, parent=maya_main_window()):
        super(Set_SRT, self).__init__(parent)
         
        self.setWindowTitle("SETSRT")
        self.setWindowFlags(QtCore.Qt.Tool)
         
        # Delete UI on close to avoid winEvent error
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
         
        self.create_layout()
        self.create_connections()
         
    def create_layout(self):
        self.Pos_btn = QtGui.QPushButton("Pos_Set")
        self.Rot_btn = QtGui.QPushButton("Rot_Set")
        self.Scale_btn = QtGui.QPushButton("Scale_Set")
         
        main_layout = QtGui.QVBoxLayout()
        main_layout.setContentsMargins(2, 2, 2, 2)
        main_layout.setSpacing(2)
        main_layout.addWidget(self.Pos_btn)
        main_layout.addWidget(self.Rot_btn)
        main_layout.addWidget(self.Scale_btn)
        main_layout.addStretch()
         
        self.setLayout(main_layout)
         
    def create_connections(self):
        self.Pos_btn.clicked.connect(Set_SRT.set_position)
        self.Rot_btn.clicked.connect(Set_SRT.set_rotation)
        self.Scale_btn.clicked.connect(Set_SRT.set_scales)
         
    @classmethod
    def set_position(cls):
        first_sel = cmds.ls( selection=True )[1]
        firstsel_w = cmds.xform(first_sel, worldSpace=True,q=True,translation=True)
        second_sel = cmds.ls( selection=True )[0]
        cmds.xform(second_sel, translation=firstsel_w,worldSpace=True,absolute=True )
         
    @classmethod
    def set_rotation(cls):
        first_sel = cmds.ls( selection=True )[1]
        firstsel_w = cmds.xform(first_sel, worldSpace=True,q=True,rotation=True)
        second_sel = cmds.ls( selection=True )[0]
        cmds.xform(second_sel, rotation=firstsel_w,worldSpace=True,absolute=True )
         
    @classmethod
    def set_scales(cls):
        first_sel = cmds.ls( selection=True )[1]
        firstsel_w = cmds.xform(first_sel, worldSpace=True,q=True,scale=True)
        second_sel = cmds.ls( selection=True )[0]
        cmds.xform(second_sel, scale=firstsel_w,worldSpace=True,absolute=True )
         
         
if __name__ == "__main__":
     
 
    try:
        ui.close()
    except:
        pass
     
    ui = Set_SRT()
    ui.show()