# -*- coding: utf-8 -*-
import maya.cmds as cmds
from functools import partial
import re
import ast

def CreateLoc(oObj,ver):
	if ver == 0:
		Order = cmds.optionMenu( 'Order_List', q= True, sl= True) -1
		BakeAll = cmds.checkBox("FrameLock",q=True,value=True)
	else:
		Order = cmds.optionMenu( 'Check_Order_List', q= True, sl= True) -1
		BakeAll = cmds.checkBox("Check_FrameLock",q=True,value=True)
	timeIn = cmds.playbackOptions(q=True,min=True)
	timeout = cmds.playbackOptions(q=True,max=True)
	inframe = []
	outframe = []
	Flag = 0
	plotObj = []
	plotDummy = []
	obj_tmp = []
	delConst = []
	for i in oObj:	
		obj_tmp.append(i)
		#キー、オーダー、アトリビュート取得
		Original_Orders = cmds.listAttr( i,r=True, string="Original_Order*" )
		oObj_Order = cmds.getAttr(i+".rotateOrder")
		oKey_Rot = []
		if cmds.findKeyframe( i , c=True, at='rotateX' ) != None:
			oKey_Rot.append(cmds.findKeyframe( i , c=True, at='rotateX' ))
		if cmds.findKeyframe( i , c=True, at='rotateY' ) != None:
			oKey_Rot.append(cmds.findKeyframe( i , c=True, at='rotateY' ))
		if cmds.findKeyframe( i , c=True, at='rotateZ' ) != None:
			oKey_Rot.append(cmds.findKeyframe( i , c=True, at='rotateZ' ))
		if len(oKey_Rot) > 1:
			keys = cmds.keyframe(oKey_Rot[0],query=True)
			if len(keys) > 1:
			#ここからが実行文
				#アトリビュートの設定とオリジナルのキーを保存しておく
				if not cmds.objExists(i+".Original_Order"):
					cmds.addAttr(i,sn="Ori", ln="Original_Order", dt="string" )
					cmds.setAttr(i+".Original_Order",oObj_Order,type="string")
				if not cmds.objExists(i+".Original_Order_RotX"):
					cmds.addAttr(i,sn="RotX", ln="Original_Order_RotX", at= "double")
					cmds.setAttr(i+".Original_Order_RotX", e= True, k= True , cb=False)
					cmds.copyKey(i,at="rotateX",o="curve")
					cmds.pasteKey(i+'.Original_Order_RotX')
				if not cmds.objExists(i+".Original_Order_RotY"):
					cmds.addAttr(i,sn="RotY", ln="Original_Order_RotY", at= "double")
					cmds.setAttr(i+".Original_Order_RotY", e= True, k= True , cb=False)
					cmds.copyKey(i,at="rotateY",o="curve")
					cmds.pasteKey(i+'.Original_Order_RotY')
				if not cmds.objExists(i+".Original_Order_RotZ"):
					cmds.addAttr(i,sn="RotZ", ln="Original_Order_RotZ", at= "double")
					cmds.setAttr(i+".Original_Order_RotZ", e= True, k= True , cb=False)
					cmds.copyKey(i,at="rotateZ",o="curve")
					cmds.pasteKey(i+'.Original_Order_RotZ')

				#ロケータを作ってオーダーを変えてプロット
				oLoc = cmds.spaceLocator(n=i+"_TempObj")
				inframe.append(keys[0])
				outframe.append(keys[-1])
				PointCons = cmds.pointConstraint(i,oLoc,n="Dummy_point")
				OrientCons = cmds.orientConstraint(i,oLoc,n="Dummy_orient")
				cmds.setAttr(i+".rotateOrder",Order)
				Connections = cmds.listRelatives(oLoc,c=True,typ="constraint",fullPath=True)
				delConst.append(Connections)
				if BakeAll == True:
					plotObj.append(i+".rotateX")
					plotObj.append(i+".rotateY")
					plotObj.append(i+".rotateZ")
					dummy = oLoc[0]
					plotDummy.append(dummy+".rotateX")
					plotDummy.append(dummy+".rotateY")
					plotDummy.append(dummy+".rotateZ")
				else:
					cmds.bakeResults([oLoc[0]+".rotateX",oLoc[0]+".rotateY",oLoc[0]+".rotateZ"],sm=False,t=(keys[0],keys[-1]),pok=True)
					for d in Connections:
						cmds.select(d)
						cmds.delete()
					To_OrientCons = cmds.orientConstraint(oLoc,i,n="Dummy_orient")

					cmds.delete(i+"_rotateX")
					cmds.delete(i+"_rotateY")
					cmds.delete(i+"_rotateZ")
					cmds.bakeResults([i+".rotateX",i+".rotateY",i+".rotateZ"],sm=False,t=(keys[0],keys[-1]),pok=True)
					Connections = cmds.listRelatives(i,c=True,typ="constraint",fullPath=True)
					for c in Connections:
						cmds.select(c)
						cmds.delete()
					cmds.delete(oLoc)
					if len(plotDummy) > 0 :
						#配列済なので、sortedでソート実行
						S_in = sorted(inframe)
						S_out = sorted(outframe)
						Sort_in = set(S_in)
						Sort_out = set(S_out)
						Min_Frame = list(Sort_in)[0]
						Max_Frame = list(Sort_out)[-1]
						#Plot
						cmds.bakeResults(plotDummy,sm=False,t=(Min_Frame,Max_Frame),pok=True)
						for d in delConst:
							cmds.select(d)
							cmds.delete()
						if len(obj_tmp) != []:
							delConst = []
							for tmp in obj_tmp:
								OrientCons = cmds.orientConstraint(tmp+"_TempObj",tmp,n="Dummy_orient")
								Connections = cmds.listRelatives(tmp,c=True,typ="constraint",fullPath=True)
								delConst.append(Connections)
							cmds.bakeResults(plotObj,sm=False,t=(Min_Frame,Max_Frame),pok=True)
							for d in delConst:
								cmds.select(d)
								cmds.delete()
							for tmp in obj_tmp:
								cmds.delete(tmp+"_TempObj")
			else:
				cmds.warning(u'キーが２つ以上打たれていません。')
				DirectChange = cmds.confirmDialog( title='ChangeOrder',  m= u'キーが２つ以上打たれていません。そのままオーダーが変えますがよろしいでしょうか？', button=['Yes','No'], defaultButton='Yes', cancelButton='No', dismissString='No' )
				if DirectChange == "Yes":
					cmds.setAttr(i+".rotateOrder",Order)
				else:
					cmds.warning(u'終了しました。')
		else:
			cmds.warning(u'回転XYZの２つ以上キー設定がされてません')
			cmds.confirmDialog( title= 'ChangeOrder', m= u'回転XYZの２つ以上キー設定がされてません', icon= 'warning')
	if BakeAll == True:
		delConect = []
		Min_Frame = sorted(inframe)[0]
		Max_Frame = sorted(outframe)[-1]

		cmds.bakeResults(plotDummy,sm=False,t=(Min_Frame,Max_Frame),pok=True)
		for d in Connections:
			cmds.select(d)
			cmds.delete()
		for i in oObj:
			To_OrientCons = cmds.orientConstraint(i+"_TempObj",i,n="Dummy_orient")
			cmds.delete(i+"_rotateX")
			cmds.delete(i+"_rotateY")
			cmds.delete(i+"_rotateZ")
			delConect.append(cmds.listRelatives(i,c=True,typ="constraint",fullPath=True))
		cmds.bakeResults(plotObj,sm=False,t=(Min_Frame,Max_Frame),pok=True)
		for dc in delConect:
			cmds.select(dc)
			cmds.delete()
		delConect = []
		for tmp in oObj:
			OrientCons = cmds.orientConstraint(tmp+"_TempObj",tmp,n="Dummy_orient")
			Connections = cmds.listRelatives(tmp,c=True,typ="constraint",fullPath=True)
			delConect.append(Connections)
		cmds.bakeResults(plotObj,sm=False,t=(Min_Frame,Max_Frame),pok=True)
		for d in delConect:
			cmds.select(d)
			cmds.delete()
		for tmp in oObj:
			cmds.delete(tmp+"_TempObj")


def ChangeOrder_exe(ver):
	#選択を取得
	oObj = cmds.ls(sl=True,type="transform")
	#メニューからもらえるオーダーの値
	if not oObj == []:
		FirstObj = oObj[0].split("_")[-1]
		if FirstObj != "TempObj":
			CreateLoc(oObj,ver)
		else:
			oObj_Sel = cmds.getAttr(oObj[0]+".Original_Selection")
			date = ast.literal_eval(oObj_Sel)
			cmds.select(clear=True)
			for sel in range(0,len(date)):
				cmds.select(date[sel],add=True)
			cmds.delete(oObj)
			oObj = cmds.ls(sl=True)
			CreateLoc(oObj,ver)
		cmds.select(oObj)
		cmds.headsUpMessage( u'完了しました。', verticalOffset=20 )
	else:
		cmds.warning(u'選択して実行してください。')
		cmds.confirmDialog( title= 'ChangeOrder', m= u'選択して実行してください。', icon= 'warning')


def Bake_BeforeOrder(self):
	oObj = cmds.ls(sl=True,type="transform")
	for i in oObj:
		oObj_Order = cmds.getAttr(i+".Original_Order")
		cmds.setAttr(i+".rotateOrder",int(oObj_Order))
		cmds.delete(i+"_rotateX")
		cmds.delete(i+"_rotateY")
		cmds.delete(i+"_rotateZ")
		cmds.copyKey(i,at="Original_Order_RotX",o="curve")
		cmds.pasteKey(i+'.rotateX')
		cmds.copyKey(i,at="Original_Order_RotY",o="curve")
		cmds.pasteKey(i+'.rotateY')
		cmds.copyKey(i,at="Original_Order_RotZ",o="curve")
		cmds.pasteKey(i+'.rotateZ')
		cmds.deleteAttr(i+".Original_Order")
		cmds.deleteAttr(i+".Original_Order_RotX")
		cmds.deleteAttr(i+".Original_Order_RotY")
		cmds.deleteAttr(i+".Original_Order_RotZ")
	cmds.select(oObj)
	cmds.headsUpMessage( u'完了しました。', verticalOffset=20 )

def ChangeSelect(self):
	sel = []
	oObj = cmds.ls()
	for i in oObj:
		Artr_Check = cmds.attributeQuery('Original_Order', node=i, exists=1)
		if Artr_Check == True :
			sel.append(i)
	if sel == []:
		cmds.confirmDialog( title= 'ChangeOrder', m= u'存在しませんでした。', icon= 'warning')
	else:
		cmds.select(sel)
		print u"選択しました。"


def ParamChange(self):
	try:
		oObj = cmds.ls(sl=True,type="transform")
		FirstObj = oObj[0].split("_")[-1]
	except:
		cmds.warning(u'選択して実行してください。')
		cmds.confirmDialog( title= 'ChangeOrder', m= u'選択して実行してください。', icon= 'warning')
		return
	if FirstObj != "TempObj":
		oLoc = cmds.spaceLocator(n=oObj[0]+"_TempObj")[0]
		cmds.addAttr(oLoc,sn="OriSel", ln="Original_Selection", dt="string" )
		cmds.setAttr(oLoc+".Original_Selection",oObj,type="string")
		PointCons = cmds.pointConstraint(oObj[0],oLoc,n="Dummy_point")
		OrientCons = cmds.orientConstraint(oObj[0],oLoc,n="Dummy_orient")
	else:
		oLoc = cmds.ls(sl=True)[0]
	cmds.setToolTo( 'RotateSuperContext' )
	Rotate_Mode = cmds.manipRotateContext( 'Rotate', q= True, mode= True)
	cmds.manipRotateContext( 'Rotate', e= True, mode= 2)
	oOrder = cmds.optionMenu( 'Check_Order_List', q= True, sl= True)
	if oOrder == 1:
		cmds.setAttr(oLoc+".rotateOrder",0)
	elif oOrder == 2:
		cmds.setAttr(oLoc+".rotateOrder",1)
	elif oOrder == 3:
		cmds.setAttr(oLoc+".rotateOrder",2)
	elif oOrder == 4:
		cmds.setAttr(oLoc+".rotateOrder",3)
	elif oOrder == 5:
		cmds.setAttr(oLoc+".rotateOrder",4)
	elif oOrder == 6:
		cmds.setAttr(oLoc+".rotateOrder",5)

#HelpWindow
def HelpWindow_Page(self):
	Helpwindow = "ChangeOrder_Help"
	Help_WindowWidth_Size = 350
	Help_WindowHight_Size = 270
	if cmds.window(Helpwindow,exists=True):
		cmds.deleteUI(Helpwindow,window=True)
	Help_MakeWindow = cmds.window(Helpwindow,title=Helpwindow,sizeable=False,mxb=False,wh=[Help_WindowWidth_Size,Help_WindowHight_Size])
	cmds.columnLayout()
	cmds.separator(w = Help_WindowWidth_Size,h=20)
	cmds.text(label=u"                          ChangeOrderのHelpページ！！")
	cmds.separator(w = Help_WindowWidth_Size,h=30)
	cmds.text(label=u"●選択したオブジェクトのローテーションオーダーを")
	cmds.text(label=u"　アニメーションを崩さず変更するスクリプトです。")
	cmds.separator(w = Help_WindowWidth_Size,h=10)
	cmds.text(label=u"●【オーダー確認】ボタンで一時的にオーダー変更後の")
	cmds.text(label=u"状態を確認することができます。")
	cmds.separator(w = Help_WindowWidth_Size,h=10)
	cmds.text(label=u"●【フレームを保持しない】は、選択した物の総尺を取得し")
	cmds.text(label=u"　そのイン、アウトに合わせてベイクします。")
	cmds.separator(w = Help_WindowWidth_Size,h=10)
	cmds.text(label=u"●元に戻す際は、【プロット】タブを")
	cmds.text(label=u"　選択していただき、【オーダーを元に戻す】")
	cmds.text(label=u"　ボタンをクリックしてください。")
	cmds.showWindow(Help_MakeWindow)
	cmds.separator(w = Help_WindowWidth_Size,h=30)

def CheckOrder(self):
	BakeAll = cmds.checkBox("FrameLock",q=True,value=True)
	oObj=[]
	try:
		oObj = cmds.ls(sl=True,type="transform")[0]
	except:
		cmds.warning(u'選択して実行してください。')
		cmds.confirmDialog( title= 'ChangeOrder', m= u'選択して実行してください。', icon= 'warning')
		return
	Check_windowname = "ChangeOrder"
	Check_WindowWidth_Size = 230
	Check_WindowHight_Size = 300
	if cmds.window(Check_windowname,exists=True):
		cmds.deleteUI(Check_windowname,window=True)
	Check_window = cmds.window(Check_windowname,title=Check_windowname,sizeable=True,mxb=False,wh=[Check_WindowWidth_Size,Check_WindowHight_Size])

	cmds.frameLayout("CheckOrder",label="CheckOrder",bgc=[0.2,0.7,0.1])
	cmds.columnLayout(w=Check_WindowWidth_Size+3,bgc=[0.2,0.2,0.2])
	cmds.separator( height= 1)
	cmds.text(label=u"オーダーを確認できます。")
	cmds.text(label=u"プルダウンを変更して確認ください。")
	cmds.text(label=u"実行ボタンで、変更処理が走ります。")
	cmds.separator( height= 1)
	cmds.rowLayout("Check",numberOfColumns=3,columnWidth2=[100,40])

	cmds.optionMenu( 'Check_Order_List',changeCommand=ParamChange, w= 100,h=50)
	cmds.menuItem( l= '0.  xyz')
	cmds.menuItem( l= '1.     yzx')
	cmds.menuItem( l= '2.        zxy')
	cmds.menuItem( l= '3.  xzy')
	cmds.menuItem( l= '4.     yxz')
	cmds.menuItem( l= '5.        zyx')
	if len(oObj) > 1:
		oObj_Order = cmds.getAttr(oObj+".rotateOrder")
	else:
		oObj_Order = 0
	cmds.optionMenu( 'Check_Order_List', e= True, bgc= [0.1,0.5,0.7], ebg= False,sl=oObj_Order+1)
	cmds.button( 'exe', l= u'実行！', h= 40, w= 110,bgc=[1.0,0.0,0.0],c='ChangeOrder_exe(%d)' % (1))
	cmds.setParent("..")
	cmds.text(label=" ")
	cmds.checkBox("Check_FrameLock", label=u'フレームを保持しない' )
	cmds.text(label="")
	cmds.separator(w = Check_WindowWidth_Size , st = 'in')
	cmds.text(label=" ")
	cmds.button( 'back', l= u'戻る', h= 60, w= Check_WindowWidth_Size,bgc=[0.45,0.45,0.45],c=MainWindow)
	cmds.setParent("..")
	if BakeAll == True:
		cmds.checkBox("Check_FrameLock",e=True,value=True)
	cmds.showWindow(Check_window)


def MainWindow(V):
	print V
	try:
		Chcek_BakeAll = cmds.checkBox("Check_FrameLock",q=True,value=True)
	except:
		Chcek_BakeAll = []
	windowname = "ChangeOrder"
	WindowWidth_Size = 230
	WindowHight_Size = 300
	oObj = []

	if cmds.window(windowname,exists=True):
		cmds.deleteUI(windowname,window=True)
	Window = cmds.window(windowname,title=windowname,sizeable=True,mxb=False,wh=[WindowWidth_Size,WindowHight_Size])

	#Helpの為にメインメニューバーを追加します
	cmds.menuBarLayout()
	cmds.menu(label=u"Menu",tearOff=False)
	cmds.menuItem(label=Window+u"の解説",c=HelpWindow_Page)
	cmds.separator(w = WindowWidth_Size)
	cmds.setParent("..")

	cmds.columnLayout(w=WindowWidth_Size+3)
	tab = cmds.tabLayout(w=WindowWidth_Size)

	tab1_B = cmds.frameLayout("ChangeOrder",label="ChangeOrder",bgc=[1.0,0.3,0.2])
	cmds.columnLayout( columnAttach= ('left',2))
	cmds.rowLayout( 'Orders', numberOfColumns= 4, columnWidth2= [100,40])
	cmds.optionMenu( 'Order_List', w= 100,h=50)
	cmds.menuItem( l= '0.  xyz')
	cmds.menuItem( l= '1.     yzx')
	cmds.menuItem( l= '2.        zxy')
	cmds.menuItem( l= '3.  xzy')
	cmds.menuItem( l= '4.     yxz')
	cmds.menuItem( l= '5.        zyx')
	try:
		oObj = cmds.ls(sl=True,type="transform")[0]
		cmds.setToolTo("RotateSuperContext")
		cmds.manipRotateContext("Rotate",e=True,mode=2)
	except:
		pass
	if len(oObj) > 1:
		oObj_Order = cmds.getAttr(oObj+".rotateOrder")
	else:
		oObj_Order = 0

	cmds.optionMenu( 'Order_List', e= True, bgc= [0.5,0.2,0.2], ebg= False,sl=oObj_Order+1)
	cmds.button( 'exe', l= u'実行！', h= 40, w= 110,c='ChangeOrder_exe(%d)' % (0))
	cmds.separator( height= 1)
	cmds.setParent(tab1_B)
	Lock = cmds.checkBox("FrameLock", label=u'フレームを保持しない' )

	tab_2 = cmds.frameLayout("OrderCheck",label="OrderCheck",bgc=[0.2,0.4,0.6])
	cmds.columnLayout()
	cmds.text("")
	cmds.text(label=u"オーダー変更後の確認が行えます。")

	cmds.button( 'exe_test', l= u'オーダー確認', h= 35, w= 220,c=CheckOrder)
	cmds.separator( h= 15)

	cmds.setParent( tab )

	tab2_B = cmds.frameLayout("Plot",label=u"Plot処理",bgc=[0.9,0.1,0.1])
	cmds.columnLayout()
	cmds.separator( h= 15)
	cmds.button( 'remove', l= u'オーダーを元にもどす', h= 60, w= 220,c=Bake_BeforeOrder)
	cmds.separator( h= 15)
	cmds.button( 'order_sel', l= u'オーダー変えたやつを選択', h= 60, w= 220,c=ChangeSelect)

	cmds.tabLayout( tab , edit=True, tabLabel=((tab1_B, u'オーダー変更'), (tab2_B,u"プロット")) )
	if Chcek_BakeAll != []:
		if Chcek_BakeAll == True:
			cmds.checkBox("FrameLock",e=True,value=True)
	cmds.showWindow(Window)

def main():
	ver = 1.0
	MainWindow(V=ver)

main()