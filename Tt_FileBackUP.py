# -*- coding: utf-8 -*-
import maya.cmds as cmds
import sys
import os
import json
import codecs
from functools import partial
#######################################
import os.path
import shutil
import datetime
import xgenm as xg
#######################################

class Tt_FileBackUp:

    ExFrameLayout = ""
    Tt_windowName = "Tt_FileBackUp"
    In = cmds.playbackOptions(q=True,min=True)
    Out = cmds.playbackOptions(q=True,max=True)
    FilesPath = ""
    OutDirValue = ""
    OutDirButton = ""
    InDirValue = ""

    @classmethod
    def main(self,*args):

        if cmds.window(self.Tt_windowName ,exists=True):
            cmds.deleteUI(self.Tt_windowName ,window=True)

        MainWindow = cmds.window(self.Tt_windowName,t=self.Tt_windowName,w=450,resizeToFitChildren=True)
        cmds.columnLayout()
        self.ExFrameLayout = cmds.frameLayout(l="Export",backgroundColor=[0.8,0.2,0.3],w=450)
        cmds.rowLayout(nc=1)
        cmds.text(l=u"  ■書き出し")
        cmds.setParent("..")

        cmds.rowLayout(nc=3)
        self.OutDirValue = cmds.textField(w=410)
        self.Tt_Path = cmds.workspace(q=True,rootDirectory=True)

        cmds.textField( self.OutDirValue, edit=True,text=self.Tt_Path,enable=False)
        self.OutDirButton = cmds.button(l="...",w=30,enable=False)
        cmds.setParent("..")
        
        cmds.rowLayout(nc=3)
        self.CheckScene = cmds.checkBox(l=u"Sceneファイルも書き出す",v=True)
        self.CheckMemo = cmds.checkBox(l=u"メモファイルも書き出す",v=True,cc=self.ChangeBox)
        self.CheckXGen = cmds.checkBox(l=u"XGenファイルも書き出す",v=True)
        cmds.setParent("..")
        
        cmds.rowLayout(nc=1)
        cmds.text(l=u"  ■メモ (こちらに記載して下さい。)")
        cmds.setParent("..")
        
        cmds.rowLayout(nc=1)
        self.TectBox = cmds.scrollField( editable=True, wordWrap=True, text=u'',h=90,w=440 )
        cmds.setParent("..")
        
        cmds.rowLayout(nc=1)
        cmds.button(l="Export!!",w=440,h=40,backgroundColor=[0.8,0.2,0.3],c=self.BackUPPPPPP)
        cmds.setParent("..")

        cmds.showWindow(MainWindow)
        
    @classmethod
    def ChangeBox(self,*args):
        Valie = cmds.checkBox(self.CheckMemo,q=True,v=True)
        if Valie:
            cmds.scrollField(self.TectBox, e=True,enable=True)
        else:
            cmds.scrollField(self.TectBox, e=True,enable=False)

    @classmethod
    def BackUPPPPPP(self,*args):
        Flag = cmds.checkBox(self.CheckScene,q=True,v=True)
        FlagXgen = cmds.checkBox(self.CheckXGen,q=True,v=True)
        day = datetime.datetime.now()
        Time = day.strftime("%m-%d_%Hh%Mm%Ss")
        Scene_Name = cmds.file( query=True, sn=True).rpartition( "/" )[0] 
        Scene_Name_Only = cmds.file( query=True, sn=True , shn=True).partition( "." )[0]
        Scene_Exten = cmds.file( query=True, sn=True , shn=True).partition( "." )[-1]
            
        Path = Scene_Name + "/versionFolder/"
        if not os.path.exists(Path): 
            os.makedirs(Path)
        Path2 = Path + "/" + Time + "/"
        if not os.path.exists(Path2): 
            os.makedirs(Path2)

        if Flag:
            cmds.file(save=True, force=True)            
            Rename = str(Path2)+str(Scene_Name_Only)+"_"+str(Time)+"."+Scene_Exten
            Scene_Dir = cmds.file( query=True, sn=True)
            shutil.copyfile(Scene_Dir, Rename)
        
        if FlagXgen:
            Scene_Name = cmds.file( query=True, sn=True).rpartition( "/" )[0]
            XGenPath = Scene_Name.rpartition( "/" )[0] + "/xgen/"

            if not os.path.exists(XGenPath): 
                os.makedirs(XGenPath)

            Sel = cmds.ls(sl=True)[0]
            try:
                xg.exportPalette(str(Sel), str(XGenPath) + "Collection.xgen")
            except:
                print "NG"
            RenameXgen = str(Path2)+str(Scene_Name_Only)+"_"+str(Time)+".xgen"
            shutil.copyfile(str(XGenPath) + "Collection.xgen", RenameXgen)
        
        FlagMemo = cmds.checkBox(self.CheckMemo,q=True,v=True)
        if FlagMemo:
            f = open(Path2 + Scene_Name_Only + "_" + Time +".txt",'w')
            textVal = cmds.scrollField(self.TectBox,q=True,text=True)
            WriteText = textVal.splitlines()
            for i in WriteText:
                f.write(i)
                f.write("\r\n")
            f.close()

F_BackUp = Tt_FileBackUp
F_BackUp.main()