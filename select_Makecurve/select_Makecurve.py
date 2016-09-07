import maya.cmds as cmds
Sel = cmds.ls(sl=True)
SelPos_Array = []

if len(Sel)>0:
	
	for i in Sel:
		Pos = cmds.xform(i, q=True, ws=True, t=True)
		SelPos_Array.append(Pos)
	Curve = cmds.curve(d = 3, p = SelPos_Array)
	Curve_Rename = cmds.rename(Curve,'Obj_Path')
	cmds.setAttr(Curve_Rename+".overrideEnabled",1)
	cmds.setAttr(Curve_Rename+".overrideColor",13)
else:
	pass