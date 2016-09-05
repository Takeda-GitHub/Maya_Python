import maya.cmds as cmds

#選択する関数
def Set(Name):
	#リストで用意(タプル、ディクショナリはNG？)
	oHako1 = []
	#選んだグループ名を記載したボタンを選択して、階層を一括選択
	cmds.select(Name,hierarchy=True)
	#選択したもののリスト取得(lambdaで一括やった方が早い？)
	oSel = cmds.ls(sl=True)
	#今回はロケーターだけ選択
	locators = cmds.ls(oSel,type=('locator'),l=True)
	#フルパスが欲しいので、親を選択
	loc_parents = cmds.listRelatives(*locators, p=True,f=True)

	#配列に格納して、選択
	for i in loc_parents:
		oHako1.append(i)
	cmds.select(oHako1)


oGSel = cmds.ls(sl=True)
WinName = 'Selector'
if cmds.window(WinName, exists = 1):
			cmds.deleteUI(WinName, window = 1)

Window = cmds.window(WinName, title = 'Selector', resizeToFitChildren = 1,  sizeable = 0)
mainLayout = cmds.columnLayout( adjustableColumn = 1, width = 300)
cmds.frameLayout(label = 'Selector')
#選択したグループ分ボタン作成
for i in oGSel: 
	cmds.button(label = i, c='Set("%s")'%i)
cmds.showWindow(WinName)