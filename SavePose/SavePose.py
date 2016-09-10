# -*- coding: utf-8 -*-
import maya.cmds as cmds
import codecs
import os.path
from functools import partial
import re

class savepose:
	radioB = ""
	TextValue = ""
	radio = ""
	flag = ""

	#saveFunction
	def savepose_cmd(self,*args):
		currentF = cmds.currentTime( query=True )
		text_get = self.TextValue
		flag = args[0]
		oSel = cmds.ls(sl=True,l=True,type='transform')
		radioCollections = cmds.radioCollection(self.radioB,q=True,select=True)
		radioQuery = cmds.radioButton(self.radio, q = True, sl = True)
		ScenePath = cmds.internalVar(uad = True) + 'SavePose'
		if oSel != []:
			if not os.path.exists(str(ScenePath)):
				os.makedirs(str(ScenePath))
			if flag == 0:
				text_split = "0"
			else:
				InputTime = cmds.textField(text_get, q=True, tx=True )
				Brank_Check = InputTime.strip()
				text_split = Brank_Check.split(",")
			for F in range(len(text_split)):
				if flag == 1:
					try:
						cmds.currentTime( text_split[F] )
					except:
						cmds.confirmDialog( title= 'SavePose', m= u'半角数字を入力してください。', icon= 'warning')
						cmds.warning(u'半角数字を入力してください。')
						return
				Select_Value = []
				ImportText = "import maya.cmds as cmds"
				Select_Value.append(ImportText)
				for i in oSel:
					list = cmds.listAttr(i, unlocked = True , visible = True , keyable = True, connectable = True, scalar = True, write = True, hd = True)
					for att in list:
						gettype = cmds.getAttr(i + "." + att,type=True)
						if gettype == "bool":
							getValue = cmds.getAttr(i + "." + att)
						else:
							getValue = cmds.getAttr(i + "." + att)
						AttrStr =  str(i) + "." + str(att)
						Value = "(\'" + str(AttrStr) + "\'," + str(getValue) + " , clamp = True)"
						Select_Value.append("cmds.setAttr" + Value)
				if flag == 0:
					if radioQuery == True:
						TextOpen = codecs.open(ScenePath+"\SavePose.py","w","utf-8")
					else:
						basicFilter = "*.py"
						Export_File = cmds.fileDialog2(dir=ScenePath,okCaption=u"書き出し！",ds=2,fm=0,caption=u"ポーズを保存",fileFilter=basicFilter, dialogStyle=2)
						if Export_File != None:
							TextOpen = open(Export_File[0], 'w')
					for val in Select_Value:
						TextOpen.write(val)
						TextOpen.write("\r\n")
					TextOpen.close()
				else:
					TextOpen = codecs.open(ScenePath+"\\"+ text_split[F] +".py","w","utf-8")
					for val in Select_Value:
						TextOpen.write(val)
						TextOpen.write("\r\n")
					TextOpen.close()
					
			if flag == 1:
				cmds.currentTime(currentF)
		else:
			cmds.warning(u'選択して実行してください。')
			cmds.confirmDialog( title= 'SavePose', m= u'選択して実行してください。', icon= 'warning')
			return

	#LoadFunction
	def RoadPove_cmd(self,*args):
		loadPath = cmds.internalVar(uad = True) + 'SavePose'
		radioCollections = cmds.radioCollection(self.radioB,q=True,select=True)
		radioQuery = cmds.radioButton(self.radio, q = True, sl = True)
		if radioQuery == True:
			ScenePath = cmds.internalVar(uad = True) + 'SavePose\SavePose.py'
		else:
			basicFilter = "*.py"
			Import_File = cmds.fileDialog2(dir=loadPath,okCaption=u"読み込み！",ds=2,fm=1,caption=u"ポーズを読み込み",fileFilter=basicFilter, dialogStyle=2)
			if Import_File != None:
				ScenePath = Import_File[0]

		script_code = []
		script_err = []
		for line in open(ScenePath, 'r').xreadlines():
			lines = line.rstrip()
			script_code.append(lines)
		for i in script_code:
			try:
				exec(i)
			except:
				print i+"は存在していない為、実行できませんでした。"
				script_err.append(i)

	#HelpWindow
	def HelpWindow_Page(self,*args):
		Helpwindow = "SavePose_Help"
		Help_WindowWidth_Size = 350
		Help_WindowHight_Size = 200
		if cmds.window(Helpwindow,exists=True):
			cmds.deleteUI(Helpwindow,window=True)
		Help_MakeWindow = cmds.window(Helpwindow,title=Helpwindow,sizeable=False,mxb=False,wh=[Help_WindowWidth_Size,Help_WindowHight_Size])
		cmds.columnLayout()
		cmds.separator(w = Help_WindowWidth_Size,h=20)
		cmds.text(label=u"                          SavePoseのHelpページ！！")
		cmds.separator(w = Help_WindowWidth_Size,h=30)
		cmds.text(label=u"●選択したノード保存するスクリプトです。")
		cmds.text(label=u"　複数可能で、ペーストは必ず、対になっているものに限ります。")
		cmds.separator(w = Help_WindowWidth_Size,h=10)
		cmds.text(label=u"●保存先はボタンを【ユーザー】に変える事で、変更可能です。")
		cmds.separator(w = Help_WindowWidth_Size,h=10)
		cmds.text(label=u"●タブを【連番に】変更すると、複数フレームを書き出せます。")
		cmds.text(label=u"　入力はカンマ「,」で区切っていただくと事で、出力がなされます。")
		cmds.text(label=u"　数字以外は入力しないで下さい。")
		cmds.showWindow(Help_MakeWindow)

	#folderOpen
	def folderOpen(self,*args):
		SystemPath = cmds.internalVar(uad = True) + 'SavePose/'
		if not os.path.exists(SystemPath):
			os.makedirs(SystemPath)
		SystemPath2 = SystemPath.replace("/", "\\\\")
		os.popen("explorer " + str(SystemPath2))
		#cmdがでるから、お休み
		#os.system('explorer ' + "\"" + SystemPath2 + "\"")
		
	def MenuMake(self,*args):
		Pose_window = "SavePose"
		WindowWidth_Size = 300
		WindowHight_Size = 140

		if cmds.window(Pose_window,exists=True):
			cmds.deleteUI(Pose_window,window=True)
		MakeWindow = cmds.window(Pose_window,title=Pose_window,sizeable=False,mxb=False,wh=[WindowWidth_Size,WindowHight_Size])

		#Helpの為にメインメニューバーを追加します
		cmds.menuBarLayout()
		cmds.menu(label=u"Menu",tearOff=False)
		cmds.menuItem(label=Pose_window+u"の解説",c=self.HelpWindow_Page)
		cmds.setParent("..")

		#複数フレーム対応の為、タブを生成
		cmds.columnLayout(w=WindowWidth_Size+3)
		tab = cmds.tabLayout(w=WindowWidth_Size)

		#続けてボタンなど配置
		tab1_B = cmds.columnLayout(w=WindowWidth_Size)
		cmds.rowLayout(numberOfColumns=2)
		self.radioB = cmds.radioCollection()
		self.radio = cmds.radioButton(label="システム")
		RadioB2 = cmds.radioButton(label="ユーザー")
		cmds.setParent( '..' )

		cmds.separator(w = WindowWidth_Size)

		cmds.rowColumnLayout(numberOfColumns=4 , columnWidth=[(1,15), (2, 120), (3, 15),(4, 120)])
		cmds.text(l = '')
		cmds.button(l = u'セーブ',c=partial(self.savepose_cmd, 0))
		cmds.text(l = '')
		cmds.button(l = u'ロード',c=self.RoadPove_cmd)
		cmds.setParent( '..' )

		cmds.separator(w = WindowWidth_Size)
		cmds.rowColumnLayout(numberOfColumns=2 , columnWidth=[(1,150), (2, 120)])
		cmds.text(l = '')
		cmds.button(l = u'システムフォルダを開く',c=self.folderOpen)

		cmds.setParent( tab )
		tab2_B = cmds.columnLayout(w=WindowWidth_Size)
		cmds.rowColumnLayout(numberOfColumns=4 , columnWidth=[(1,5),(2,150),(3,8),(4,100)])
		cmds.text(l = '')
		cmds.text(l = u'フレーム【カンマで区切って入力】')
		cmds.text(l = '')

		self.TextValue = cmds.textField()
		cmds.textField( self.TextValue, edit=True,text="0,100" )

		cmds.setParent( '..' )

		cmds.separator(w = WindowWidth_Size)
		cmds.rowColumnLayout(numberOfColumns=2 ,columnWidth=([1,65],[2,150]))
		cmds.text(l = '')
		cmds.button(l = u'セーブ',c=partial(self.savepose_cmd, 1))
		cmds.setParent( '..' )

		cmds.separator(w = WindowWidth_Size)
		cmds.rowColumnLayout(numberOfColumns=2 , columnWidth=[(1,65), (2, 150)])
		cmds.text(l = '')
		cmds.button(l = u'システムフォルダを開く',c=self.folderOpen)
		#各所設定
		cmds.radioCollection(self.radioB,e=True,select=self.radio)
		cmds.tabLayout( tab , edit=True, tabLabel=((tab1_B, u'フレーム'), (tab2_B,u"連番")) )


		cmds.showWindow(MakeWindow)

def main():
	classCommad = savepose()
	classCommad.MenuMake()



main()
