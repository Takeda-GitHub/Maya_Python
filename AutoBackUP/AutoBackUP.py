import maya.cmds as cmds
import os.path
import shutil
import datetime

def BackUPP():
	day = datetime.datetime.now()
	Time = day.strftime("%m-%d_%Hh%Mm%Ss")

	ScenePath = cmds.file( query=True, lastTempFile=True).rpartition( "/" )[0] 
	Scene_Name = cmds.file( query=True, sn=True)
	Scene_Name_Only = cmds.file( query=True, sn=True , shn=True)

	Path = ScenePath + "/ver/"
	if not os.path.exists(Path): 
		os.makedirs(Path)

	Rename = str(Path)+str(Scene_Name_Only)+"_"+str(Time)+".ma"
	shutil.copyfile(Scene_Name, Rename)


def Auto():
	cmds.file( save=True)
	BackUPP()