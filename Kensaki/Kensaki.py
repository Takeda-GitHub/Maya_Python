import maya.cmds as cmds

def WepIk_Control():
	In = cmds.playbackOptions(q=True,min=True)
	Out = cmds.playbackOptions(q=True,max=True)
	
	oSel = cmds.ls(sl=True)
	oPos_Rot = oSel[1]
	oWep = oSel[2]
	oLoc = cmds.spaceLocator(n="Kensaki")[0]
	oLoc_temp = cmds.spaceLocator(n="Kensaki_World")[0]
	oLoc_parent = cmds.spaceLocator(n="Kensaki_Pos")[0]
	
	cmds.pointConstraint(oPos_Rot,oLoc_parent)
	cmds.orientConstraint(oWep,oLoc_parent)
	Be_list = []
	Be_list.append(oLoc_parent+'.tx')
	Be_list.append(oLoc_parent+'.ty')
	Be_list.append(oLoc_parent+'.tz')
	cmds.bakeResults(Be_list,sm=True,t=(In,Out),pok=True,sb="1",dic=True,sac=False)
	cmds.parent(oLoc,oLoc_parent)
	oVer = cmds.xform(oSel[0], q=True, ws=True, t=True)
	X = oVer[0]
	Y = oVer[1]
	Z = oVer[2]
	cmds.setAttr(oLoc_temp+".translateX",X)
	cmds.setAttr(oLoc_temp+".translateY",Y)
	cmds.setAttr(oLoc_temp+".translateZ",Z)
	cmds.pointConstraint(oLoc_temp,oLoc)
	cmds.delete(oLoc_temp)


	cmds.select(cl=True)

	oBone = cmds.joint(p=(0,0,0),n="handjoint")
	oWepBone = cmds.joint(p=(50,0,0),n="weaponjoint")
	
	cmds.pointConstraint(oWep,oBone)
	point = cmds.pointConstraint(oLoc,oWepBone)
	cmds.delete(point)
	oIk = cmds.ikHandle(n="ikHandle_weapon",sol="ikRPsolver",startJoint=oBone)

	
	Dummy_1 = cmds.spaceLocator(n="dummy_UPV1")
	Dummy_2 = cmds.spaceLocator(n="dummy_UPV2")
	cmds.parent(Dummy_2,Dummy_1)

	cmds.pointConstraint(oWep,Dummy_1)
	cmds.select(cl=True)
	cmds.orientConstraint(oWep,Dummy_1)
	
	cmds.setAttr("dummy_UPV2.translateY",60)

	
	oLoc_wep = cmds.spaceLocator(n="weapon_root")

	Pos_Cont = cmds.sphere(n="weapon_POS",r= 6,nsp=2,s=2)[0]
	cmds.setAttr(Pos_Cont+".overrideEnabled", 1)
	cmds.setAttr(Pos_Cont+".overrideColor", 13)
	cmds.setAttr(Pos_Cont+".showManipDefault", 1)

	cmds.setAttr(Pos_Cont+"Shape.overrideEnabled", 1)
	cmds.setAttr(Pos_Cont+"Shape.overrideShading", 0)
	cmds.setAttr(Pos_Cont+"Shape.overrideColor", 13)

	oCone = cmds.cone(n="weapon_UPV",r=7,hr=2,s=4,nsp=2)[0]
	cmds.setAttr(oCone+".overrideEnabled",1)
	cmds.setAttr(oCone+".overrideColor",6)
	cmds.setAttr(oCone+".showManipDefault", 1)
	
	cmds.parent(Pos_Cont,oLoc_wep)
	cmds.parent(oCone,oLoc_wep)
	cmds.pointConstraint(oPos_Rot,oLoc_wep)
	
 	Del_Pos = cmds.pointConstraint(Dummy_2,oCone)
	Del_Pos2 = cmds.pointConstraint(oLoc,Pos_Cont)
 
 	cmds.pointConstraint(Pos_Cont,oIk[0])
	cmds.poleVectorConstraint(oCone,oIk[0])


	At_list = []
	At_list.append(oCone+'.tx')
	At_list.append(oCone+'.ty')
	At_list.append(oCone+'.tz')
	At_list.append(Pos_Cont+'.tx')
	At_list.append(Pos_Cont+'.ty')
	At_list.append(Pos_Cont+'.tz')
	
	cmds.bakeResults(At_list,sm=True,t=(In,Out),pok=True,sb="1",dic=True,sac=False)

	oHand_wep = cmds.spaceLocator(n="cnv_hand")

	cmds.parent(oHand_wep,oBone)
	point2 = cmds.pointConstraint(oWep,oHand_wep)	
	ori2 = cmds.orientConstraint(oWep,oHand_wep)
	
	cmds.delete(point2,ori2)

 	ori3 = cmds.orientConstraint(oHand_wep,oWep)
	cmds.select(cl=True)
	cmds.delete(Del_Pos,Del_Pos2)
	cmds.group(oLoc_parent,oLoc_wep,oBone,oIk[0],Dummy_1,n="Kensaki")

WepIk_Control()