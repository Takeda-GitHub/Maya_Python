# -*- coding: utf-8 -*-
import maya.cmds as cmds
import maya.mel as mel	

def SelPoly_Hide():
	#選択をリストに格納
	oSel = cmds.ls(sl=True)
	#フラグ立て
	Check = 0
	#選択されていなかったら
	if oSel == []:
		return
	#キーボードステートをチェック
	mods = cmds.getModifiers()
	#コントロール押していたら、関数に飛んで終了
	if (mods & 4) > 0:
		if oSel[0] == "Poly_Hide_Set":
			Toggle(oSel)
			Clean()
			return
	#選択がセットで且つ、コントロール押していなかったら。
	if oSel[0] == "Poly_Hide_Set":
		Toggle(oSel)
		return
	#フェースを選択
	oSelFace = cmds.filterExpand(sm=34)
	#フェースじゃなかったら
	if oSelFace == None:
		return
	#フェースからオブジェクトを取得
	const =  oSelFace[0].rpartition(".")
	#ヒストリーを取得
	oList = cmds.listHistory(const[0])
	for i in oList:
		#穴開けるヒストリーがあったら、フラグを立てる
		if i == "Hide_Poly":
			Check = 1  
	#フラグが立っていたら
	if Check == 1:
		cmds.polyHole(assignHole=0)
	#なかったら
	else:
		mel.eval('ToggleHoleFaces;')
		FaceSet = cmds.sets(n="Poly_Hide_Set")
		cmds.polyHole(assignHole=1)
		cmds.rename("polyHoleFace1","Hide_Poly")
	
#単純に表示を切り替えているだけ
def Toggle(oSel):
	cmds.select(hierarchy=True)
	mel.eval('ToggleHoleFaces;')
	cmds.select(cl=True)

#ヒストリとセットを削除
def Clean():
	cmds.delete("Hide_Poly")
	cmds.delete("Poly_Hide_Set")



SelPoly_Hide()