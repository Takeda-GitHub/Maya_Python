# -*- coding: utf-8 -*-
import maya.cmds as cmds
import maya.OpenMaya as OM

def  Flag_Check(attr,Flag):
	if attr == 1:
		Flag += int("1")
	return Flag

def Channel_Check(Obj,posX,rotX,sclX,list):
	if posX == 1:
		list.append(Obj+'.tx')
		list.append(Obj+'.ty')
		list.append(Obj+'.tz')
	if rotX == 1:
		list.append(Obj+'.rx')
		list.append(Obj+'.ry')
		list.append(Obj+'.rz')
	if sclX == 1:
		list.append(Obj+'.sx')
		list.append(Obj+'.sy')
		list.append(Obj+'.sz')
	return list

def RunBake(List,InFlame,OutFlame,Connections):
	cmds.bakeResults(List,sm=False,t=(InFlame,OutFlame),pok=True)
	cmds.delete(Connections)

def Bake_Set(self):
	Sel = cmds.ls( sl=True)
	Sel_FullPath = Path(Sel)
	Sel_Long = Sel_FullPath.fullPathName()
	Cone = cmds.curve(d = 1, p = [[-8.6754635314381261, -11.371846236362176, 8.721448300231371], [-0.19018254083754044, 12.628153763637824, 0.23616730963078481], [-0.19018254083754044, -11.371846236362176, 12.236166355956469], [-8.6754635314381261, -11.371846236362176, 8.721448300231371], [-0.19018254083754044, -11.371846236362176, 0.23616730963078481], [-0.19018254083754044, -11.371846236362176, 12.236166355956469], [-0.19018254083754044, 12.628153763637824, 0.23616730963078481], [8.2950984497630458, -11.371846236362176, 8.721448300231371], [-0.19018254083754044, -11.371846236362176, 12.236166355956469], [-0.19018254083754044, -11.371846236362176, 0.23616730963078481], [8.2950984497630458, -11.371846236362176, 8.721448300231371], [-0.19018254083754044, 12.628153763637824, 0.23616730963078481], [11.80981745916246, -11.371846236362176, 0.23616730963078481], [8.2950984497630458, -11.371846236362176, 8.721448300231371], [-0.19018254083754044, -11.371846236362176, 0.23616730963078481], [11.80981745916246, -11.371846236362176, 0.23616730963078481], [-0.19018254083754044, 12.628153763637824, 0.23616730963078481], [8.2950984497630458, -11.371846236362176, -8.2491136809698009], [11.80981745916246, -11.371846236362176, 0.23616730963078481], [-0.19018254083754044, -11.371846236362176, 0.23616730963078481], [8.2950984497630458, -11.371846236362176, -8.2491136809698009], [-0.19018254083754044, 12.628153763637824, 0.23616730963078481], [-0.19018254083754044, -11.371846236362176, -11.763830783020582], [8.2950984497630458, -11.371846236362176, -8.2491136809698009], [-0.19018254083754044, -11.371846236362176, 0.23616730963078481], [-0.19018254083754044, -11.371846236362176, -11.763830783020582], [-0.19018254083754044, 12.628153763637824, 0.23616730963078481], [-8.6754635314381261, -11.371846236362176, -8.2491136809698009], [-0.19018254083754044, -11.371846236362176, 0.23616730963078481], [-0.19018254083754044, -11.371846236362176, -11.763830783020582], [-8.6754635314381261, -11.371846236362176, -8.2491136809698009], [-0.19018254083754044, 12.628153763637824, 0.23616730963078481], [-12.190180633488907, -11.371846236362176, 0.23616730963078481], [-8.6754635314381261, -11.371846236362176, -8.2491136809698009], [-0.19018254083754044, -11.371846236362176, 0.23616730963078481], [-12.190180633488907, -11.371846236362176, 0.23616730963078481], [-0.19018254083754044, 12.628153763637824, 0.23616730963078481], [-8.6754635314381261, -11.371846236362176, 8.721448300231371], [-12.190180633488907, -11.371846236362176, 0.23616730963078481], [-0.19018254083754044, -11.371846236362176, 0.23616730963078481], [-8.6754635314381261, -11.371846236362176, 8.721448300231371]])
	cmds.addAttr(Cone,sn="TM", ln="TargetModel", dt="string" )
	cmds.setAttr(Cone+'.TargetModel',Sel_Long,type='string')

	Sel_Pos = cmds.xform(Sel, worldSpace=True,q=True,translation=True)
	Sel_Rot = cmds.xform(Sel, worldSpace=True,q=True,rotation=True)
	Sel_Scl = cmds.xform(Sel, worldSpace=True,q=True,scale=True)
	cmds.xform(Cone, translation=Sel_Pos,worldSpace=True,absolute=True )
	cmds.xform(Cone, rotation=Sel_Rot,worldSpace=True,absolute=True )
	cmds.xform(Cone, scale=Sel_Scl,worldSpace=True,absolute=True )
	Q_Pos = cmds.checkBox("Pos",q=True,v=True)
	Q_Rot = cmds.checkBox("Rot",q=True,v=True)
	Q_Scl = cmds.checkBox("Scale",q=True,v=True)
	Name_Set = ''
	Rename_Point = 0
	Rename_Orient = 0
	Rename_Scale = 0

	if Q_Pos == True:
		cmds.pointConstraint(Cone,Sel)
		Rename_Point = 1
	if Q_Rot == True:
		cmds.orientConstraint(Cone,Sel)
		Rename_Orient = 1
	if Q_Scl == True:
		cmds.scaleConstraint(Cone,Sel)
		Rename_Scale = 1

	if Rename_Scale == 1:
		Name_Set = Name_Set + 'Scl'
	if Rename_Orient == 1:
		Name_Set = Name_Set + 'Rot'
	if Rename_Point == 1:
		Name_Set = Name_Set + 'Pos'
	Rename_Cont = cmds.rename(Cone,"Global_"+Cone+"_"+Name_Set)
	cmds.setAttr(Rename_Cont+".overrideEnabled",1)
	cmds.setAttr(Rename_Cont+".overrideColor",6)



def makeWindow(Sel):
	if cmds.window("Global_Cont",exists=True):
		cmds.deleteUI("Global_Cont")

	Create_Window = cmds.window("Global_Cont",title="Global_Cont",s=False)
	cmds.frameLayout('Global_Plot_Menu',l= u'Global_Plot_Menu',cll=True)
	cmds.columnLayout(columnAttach=('left', 10), rowSpacing=5)
	cmds.text(l= u'・ベイクタイプ選択',align='left')
	cmds.checkBox("Pos",l=u"---------位置",value=True)
	cmds.checkBox("Rot",l=u"---------回転",value=True)
	cmds.checkBox("Scale",l=u"---------スケール",value=True)
	cmds.setParent('..')
	cmds.columnLayout( adjustableColumn = True)
	cmds.button("Bake",l=u"Bake!!",h=70,w=280,bgc=[0.5,0.5,0.5],c=Bake_Set)
	cmds.showWindow(Create_Window)

def Path(Item):
	List = OM.MSelectionList()
	List.add(Item)
	FullPath = OM.MDagPath()
	List.getDagPath(0,FullPath)
	return FullPath

def main():
    ####################################################################
    #初期設定
    ####################################################################
    In = cmds.playbackOptions(q=True,min=True)
    Out = cmds.playbackOptions(q=True,max=True)
    oSel = cmds.ls(sl=True,tr=True)
    oSel_str = map(str,oSel)
    oSel_Joint = ",".join(oSel_str)
    oSel_Array = oSel_Joint.split(",")
    bakeSet = []
    deleteSet = []
    Finsel = []

    if len(oSel)>0:
        for i in oSel_Array:
            Artr_Check = cmds.attributeQuery('TargetModel', node=i, exists=1)
            if Artr_Check ==False:
    			posX_Flag = int("0")
    			posY_Flag = int("0")
    			posZ_Flag = int("0")
    			rotX_Flag = int("0")
    			rotY_Flag = int("0")
    			rotZ_Flag = int("0")
    			sclX_Flag = int("0")
    			sclY_Flag = int("0")
    			sclZ_Flag = int("0")

    			posX = cmds.selectKey(i,at="translateX")
    			posY = cmds.selectKey(i,at="translateY")
    			posZ = cmds.selectKey(i,at="translateZ")

    			rotX = cmds.selectKey(i,at="rotateX")
    			rotY = cmds.selectKey(i,at="rotateY")
    			rotZ = cmds.selectKey(i,at="rotateZ")

    			sclX = cmds.selectKey(i,at="scaleX")
    			sclY = cmds.selectKey(i,at="scaleY")
    			sclZ = cmds.selectKey(i,at="scaleZ")

    	####################################################################
    	#アトリビュート確認
    	####################################################################
    			posX_Flag += Flag_Check(posX,posX_Flag)
    			posY_Flag += Flag_Check(posY,posY_Flag)
    			posZ_Flag += Flag_Check(posZ,posZ_Flag)
    			rotX_Flag += Flag_Check(rotX,rotX_Flag)
    			rotY_Flag += Flag_Check(rotY,rotY_Flag)
    			rotZ_Flag += Flag_Check(rotZ,rotZ_Flag)
    			sclX_Flag += Flag_Check(sclX,sclX_Flag)
    			sclY_Flag += Flag_Check(sclY,sclY_Flag)
    			sclZ_Flag += Flag_Check(sclZ,sclZ_Flag)
    			Rename_Point = 0
    			Rename_Orient = 0
    			Rename_Scale = 0

    	####################################################################
    	#選択にコンスト
    	####################################################################
    			if posX_Flag+posY_Flag+posZ_Flag+rotX_Flag+rotY_Flag+rotZ_Flag+sclX_Flag+sclY_Flag+sclZ_Flag == 0:
    				makeWindow(i)
    			else:
    				Sel_FullPath = Path(i)
    				Sel_Long = Sel_FullPath.fullPathName()
    				Cone = cmds.curve(d = 1, p = [[-8.6754635314381261, -11.371846236362176, 8.721448300231371], [-0.19018254083754044, 12.628153763637824, 0.23616730963078481], [-0.19018254083754044, -11.371846236362176, 12.236166355956469], [-8.6754635314381261, -11.371846236362176, 8.721448300231371], [-0.19018254083754044, -11.371846236362176, 0.23616730963078481], [-0.19018254083754044, -11.371846236362176, 12.236166355956469], [-0.19018254083754044, 12.628153763637824, 0.23616730963078481], [8.2950984497630458, -11.371846236362176, 8.721448300231371], [-0.19018254083754044, -11.371846236362176, 12.236166355956469], [-0.19018254083754044, -11.371846236362176, 0.23616730963078481], [8.2950984497630458, -11.371846236362176, 8.721448300231371], [-0.19018254083754044, 12.628153763637824, 0.23616730963078481], [11.80981745916246, -11.371846236362176, 0.23616730963078481], [8.2950984497630458, -11.371846236362176, 8.721448300231371], [-0.19018254083754044, -11.371846236362176, 0.23616730963078481], [11.80981745916246, -11.371846236362176, 0.23616730963078481], [-0.19018254083754044, 12.628153763637824, 0.23616730963078481], [8.2950984497630458, -11.371846236362176, -8.2491136809698009], [11.80981745916246, -11.371846236362176, 0.23616730963078481], [-0.19018254083754044, -11.371846236362176, 0.23616730963078481], [8.2950984497630458, -11.371846236362176, -8.2491136809698009], [-0.19018254083754044, 12.628153763637824, 0.23616730963078481], [-0.19018254083754044, -11.371846236362176, -11.763830783020582], [8.2950984497630458, -11.371846236362176, -8.2491136809698009], [-0.19018254083754044, -11.371846236362176, 0.23616730963078481], [-0.19018254083754044, -11.371846236362176, -11.763830783020582], [-0.19018254083754044, 12.628153763637824, 0.23616730963078481], [-8.6754635314381261, -11.371846236362176, -8.2491136809698009], [-0.19018254083754044, -11.371846236362176, 0.23616730963078481], [-0.19018254083754044, -11.371846236362176, -11.763830783020582], [-8.6754635314381261, -11.371846236362176, -8.2491136809698009], [-0.19018254083754044, 12.628153763637824, 0.23616730963078481], [-12.190180633488907, -11.371846236362176, 0.23616730963078481], [-8.6754635314381261, -11.371846236362176, -8.2491136809698009], [-0.19018254083754044, -11.371846236362176, 0.23616730963078481], [-12.190180633488907, -11.371846236362176, 0.23616730963078481], [-0.19018254083754044, 12.628153763637824, 0.23616730963078481], [-8.6754635314381261, -11.371846236362176, 8.721448300231371], [-12.190180633488907, -11.371846236362176, 0.23616730963078481], [-0.19018254083754044, -11.371846236362176, 0.23616730963078481], [-8.6754635314381261, -11.371846236362176, 8.721448300231371]])
    				cmds.addAttr(Cone,sn="TM", ln="TargetModel", dt="string" )
    				cmds.setAttr(Cone+'.TargetModel',Sel_Long,type='string')
    				if posX_Flag+posY_Flag+posZ_Flag > 2:
    					Point_Const = cmds.pointConstraint(i,Cone)
    					Rename_Point = 1
    				if rotX_Flag+rotY_Flag+rotZ_Flag > 2:
    					Orient_Const = cmds.orientConstraint(i,Cone)
    					Rename_Orient = 1
    				if sclX_Flag+sclY_Flag+sclZ_Flag > 2:
    					Scale_Const = cmds.scaleConstraint(i,Cone)
    					Rename_Scale = 1

    				Name_Set = ''
    				if Rename_Scale ==1:
    					Name_Set = Name_Set + 'S'
    				if Rename_Orient ==1:
    					Name_Set = Name_Set + 'R'
    				if Rename_Point ==1:
    					Name_Set = Name_Set + 'T'
    				ReName = cmds.rename(Cone,"Global_"+i+"_"+Name_Set)
    				At_list = []
    	####################################################################
    	#ベイク設定
    	####################################################################
    				Bake_list = Channel_Check(ReName,posX,rotX,sclX,At_list)
    				Connections = cmds.listRelatives(ReName,c=True,typ="constraint")
    	####################################################################
    	#ベイク関数
    	####################################################################
    				RunBake(Bake_list,In,Out,Connections)
    	####################################################################
    	#再コンスト
    	####################################################################
    				if Rename_Scale == 1 :
    					cmds.cutKey( i, attribute='scaleX', option="keys" )
    					cmds.cutKey( i, attribute='scaleY', option="keys" )
    					cmds.cutKey( i, attribute='scaleZ', option="keys" )
    					cmds.scaleConstraint(ReName,i)
    				if Rename_Orient == 1 :
    					cmds.orientConstraint(ReName,i)
    				if Rename_Point == 1 :
    					cmds.pointConstraint(ReName,i)
    				Sel_Pos = cmds.xform(i,worldSpace=True,q=True,translation=True)
    				cmds.xform(ReName, translation=Sel_Pos,worldSpace=True,absolute=True )
    				cmds.setAttr(ReName+".overrideEnabled",1)
    				cmds.setAttr(ReName+".overrideColor",6)
    				Finsel.append(ReName)
            else:
                target = cmds.getAttr ( '%s.TargetModel' % i )
                bakeSet.append(target)
                deleteSet.append(i)
        ###########################################################
        #グローバルを一括ペースト
        ###########################################################
        if len(bakeSet)>0:
            At_list = []
            for i in bakeSet:
                posX = cmds.selectKey(i,at="translateX")
                posY = cmds.selectKey(i,at="translateY")
                posZ = cmds.selectKey(i,at="translateZ")
                rotX = cmds.selectKey(i,at="rotateX")
                rotY = cmds.selectKey(i,at="rotateY")
                rotZ = cmds.selectKey(i,at="rotateZ")
                sclX = cmds.selectKey(i,at="scaleX")
                sclY = cmds.selectKey(i,at="scaleY")
                sclZ = cmds.selectKey(i,at="scaleZ")
                Bake_list = Channel_Check(i,posX,rotX,sclX,At_list)
            #Bakeしてワールドコントローラーを削除
            RunBake(Bake_list,In,Out,deleteSet)


    else:
    	cmds.confirmDialog(message = u'１つ以上選択して実行して下さい。',b= u'~終了~')
    if len(Finsel)>0:
        cmds.select(Finsel)


main()

