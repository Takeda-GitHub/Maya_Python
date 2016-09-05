import maya.cmds as cmds

class Tt_Rig_cont:

	@staticmethod
	def Tt_Rig_controller():
		WinName = 'Tt_Rig_controller'
		RigColor = 'ctrlColor'

		if cmds.window(WinName, exists = 1):
			cmds.deleteUI(WinName, window = 1)
	    
		Tt_Rig_cont.Tt_Rig_UI()
		cmds.window(WinName, edit = True,  topLeftCorner = (200, 200))
		cmds.showWindow(WinName)

	@staticmethod
	def Tt_Rig_UI():
		WinName = 'Tt_Rig_controller'
		Tt_Rig_Window = cmds.window(WinName, title = 'Tt_Rig_controller', resizeToFitChildren = 1,  sizeable = 0)
		mainLayout = cmds.columnLayout( adjustableColumn = 1, width = 300)
		color_palette = None
	    
		cmds.frameLayout(label = 'Rig_Controller')
		cmds.scrollLayout(childResizable = 1 , h = 250)
		cmds.gridLayout(numberOfColumns = 7 , cellWidthHeight = (90, 90), width = 100)
	    
		cmds.symbolButton(image = 'Tt_icons/RigButton01.PNG', command = Tt_Rig_cont.Tt_Rig_Button00)
		cmds.symbolButton(image = 'Tt_icons/RigButton02.PNG', command = Tt_Rig_cont.Tt_Rig_Button01)
		cmds.symbolButton(image = 'Tt_icons/RigButton03.PNG', command = Tt_Rig_cont.Tt_Rig_Button02)
		cmds.symbolButton(image = 'Tt_icons/RigButton04.PNG', command = Tt_Rig_cont.Tt_Rig_Button03)
		cmds.symbolButton(image = 'Tt_icons/RigButton05.PNG', command = Tt_Rig_cont.Tt_Rig_Button04)
		cmds.symbolButton(image = 'Tt_icons/RigButton06.PNG', command = Tt_Rig_cont.Tt_Rig_Button05)
		cmds.symbolButton(image = 'Tt_icons/RigButton07.PNG', command = Tt_Rig_cont.Tt_Rig_Button06)
		cmds.symbolButton(image = 'Tt_icons/RigButton08.PNG', command = Tt_Rig_cont.Tt_Rig_Button07)
		cmds.symbolButton(image = 'Tt_icons/RigButton09.PNG', command = Tt_Rig_cont.Tt_Rig_Button08)
		cmds.symbolButton(image = 'Tt_icons/RigButton10.PNG', command = Tt_Rig_cont.Tt_Rig_Button09)
		cmds.symbolButton(image = 'Tt_icons/RigButton11.PNG', command = Tt_Rig_cont.Tt_Rig_Button10)
		cmds.symbolButton(image = 'Tt_icons/RigButton12.PNG', command = Tt_Rig_cont.Tt_Rig_Button11)
		cmds.symbolButton(image = 'Tt_icons/RigButton13.PNG', command = Tt_Rig_cont.Tt_Rig_Button12)
		cmds.symbolButton(image = 'Tt_icons/RigButton14.PNG', command = Tt_Rig_cont.Tt_Rig_Button13)
		cmds.symbolButton(image = 'Tt_icons/RigButton15.PNG', command = Tt_Rig_cont.Tt_Rig_Button14)
		cmds.symbolButton(image = 'Tt_icons/RigButton16.PNG', command = Tt_Rig_cont.Tt_Rig_Button15)
		cmds.symbolButton(image = 'Tt_icons/RigButton17.PNG', command = Tt_Rig_cont.Tt_Rig_Button16)

		cmds.setParent(mainLayout)
		cmds.frameLayout(label = 'Scale')
		cmds.floatSliderGrp('ScaleSlider', label=u'Scale', field=True,\
	                          min=0.1, max=30.0, step=0.1, value=1.0)

		cmds.setParent(mainLayout)
		cmds.frameLayout(label	 = 'Color')
		columns = 32 / 2
		rows = 2
		cell_width = 40
		cell_height = 40
		color_palette = cmds.palettePort("color_set",dimensions=(columns, rows), 
										transparent=0,
										width=(columns*cell_width),
										height=(rows*cell_width),
										topDown=True,
										colorEditable=False);

		for index in range(1, 32):
			color_component = cmds.colorIndex(index, q=True)
			cmds.palettePort(color_palette,
							edit=True,
							rgbValue=(index, color_component[0], color_component[1], color_component[2]))

		cmds.palettePort(color_palette,
						edit=True,
						rgbValue=(0, 0.6, 0.6, 0.6))
	                       
		cmds.setParent(mainLayout)
		cmds.rowColumnLayout( numberOfRows=1 )
		Change_Color = cmds.button(label = 'Change_Color',w=320,backgroundColor=[0.7,0.7,0.7],c=Tt_Rig_cont.ChangeColor_Display)
		Defult_Color = cmds.button(label = 'Defult_Color',w=320,c=Tt_Rig_cont.DefultColor_Display)

		cmds.setParent(mainLayout)

		cmds.button(label = 'SRT_Match(First Sel >>> Second Sel)',c=Tt_Rig_cont.SRT)
		cmds.button(label = 'Freeze Transformations',c=Tt_Rig_cont.Freeze)

	@staticmethod
	def DefultColor_Display(self):
		sel = cmds.ls(selection=True,transforms=True)
		for i in sel:
			try:
				cmds.setAttr(i+".overrideEnabled", False)
			except:
				print "NotChangeColor"

	@staticmethod
	def ChangeColor_Display(self):
		sel = cmds.ls(selection=True,transforms=True)
		color = cmds.palettePort('color_set', q=True, setCurCell=True)
		for i in sel:
			try:
				cmds.setAttr(i+".overrideEnabled", True)
				cmds.setAttr(i+ '.overrideColor', color)
			except:
				print "NotChangeColor"
		return True



	@staticmethod
	def SRT(self):
		try:
			first_sel = cmds.ls( selection=True )[1]
			firstsel_wp = cmds.xform(first_sel, worldSpace=True,q=True,translation=True)
			firstsel_wr = cmds.xform(first_sel, worldSpace=True,q=True,rotation=True)
			second_sel = cmds.ls( selection=True )[0]
			cmds.xform(second_sel, translation=firstsel_wp,worldSpace=True,absolute=True )
			cmds.xform(second_sel, rotation=firstsel_wr,worldSpace=True,absolute=True )
		except:
			print "NotSel"

	@staticmethod
	def Freeze(self):
		try:
			sel = cmds.ls( selection=True )
			cmds.makeIdentity(sel, apply = True, t = True, r = True, s = True, n = False)
		except:
			print "NotSel"


	@staticmethod
	def Tt_Rig_Button00(self):
		Curve = cmds.curve(d = 1, p = [[16.0, 16.0, 16.0], [-16.0, 16.0, 16.0], [-16.0, 16.0, -16.0], [16.0, 16.0, -16.0], [16.0, 16.0, 16.0], [16.0, -16.0, 16.0], [16.0, -16.0, -16.0], [16.0, 16.0, -16.0], [16.0, -16.0, -16.0], [-16.0, -16.0, -16.0], [-16.0, 16.0, -16.0], [-16.0, -16.0, -16.0], [-16.0, -16.0, 16.0], [-16.0, 16.0, 16.0], [-16.0, -16.0, 16.0], [16.0, -16.0, 16.0]]) 
		Curve_Rename = cmds.rename(Curve,'Box')
		color = cmds.palettePort('color_set', q=True, setCurCell=True)
		if color > 0:
			cmds.setAttr(Curve_Rename + '.overrideEnabled', True)
			cmds.setAttr(Curve_Rename + '.overrideColor', color)
		scale = cmds.floatSliderGrp('ScaleSlider', q=True, value=True)
		cmds.xform(Curve_Rename, ws = True, s = [scale, scale, scale])
		cmds.makeIdentity(Curve_Rename	, apply = True, t = False, r = False, s = True, n = False)

	@staticmethod
	def Tt_Rig_Button01(self):
		Curve = cmds.curve(d = 1, p = [[0.0, 0.0, -16.000000000000004], [-4.1207577809114699, 0.0, -15.457491946190311], [-8.0055743388644203, 0.0, -13.852129119900209], [-11.322197883595862, 0.0, -11.302644917559764], [-13.860764440521024, 0.0, -7.9894789056518647], [-15.455786590118951, 0.0, -4.133711246304153], [-16.000000000000014, 0.0, 0.0], [-15.452565632404493, 0.0, 4.1465308796051339], [-13.848410800053488, 0.0, 8.0104201476330079], [-11.302462152454908, 0.0, 11.322338124193283], [-7.9934056996211451, 0.0, 13.859137909202303], [-4.1411047216403407, 0.0, 15.454813220625093], [0.0, 0.0, 16.000000000000004], [4.1320942996732093, 0.0, 15.455999465181385], [7.9993403826780982, 0.0, 13.85667968299173], [11.306017959094451, 0.0, 11.319609657794732], [13.853693139324708, 0.0, 8.0035360690668043], [15.455625331697908, 0.0, 4.1349361256190358], [16.000000000000014, 0.0, 0.0], [15.456630025764191, 0.0, -4.1273047165330716], [13.845803029455309, 0.0, -8.0138186604431105], [11.315840543696284, 0.0, -11.310929964220689], [8.001013178505465, 0.0, -13.855629021340148], [4.1449276377042699, 0.0, -15.453229716943605], [0.0, 0.0, -16.000000000000004], [0.0, 4.1128589052577071, -15.458531852898266], [0.0, 7.9975884933628878, -13.85740533930587], [0.0, 11.309756901462086, -11.316740666409549], [0.0, 13.859901930291056, -7.9915611895467595], [0.0, 15.445152605428566, -4.1644275098686716], [0.0, 16.000000000000004, 0.0], [0.0, -16.000000000000004, 0.0], [0.0, -15.457775943856658, -4.1186006044692993], [0.0, -13.846805139090781, -8.0125126857397859], [0.0, -11.307864581121342, -11.318192694876894], [0.0, -8.0067408299160654, -13.851234039835047], [0.0, -4.1165339641980205, -15.458048022209987], [0.0, 0.0, -16.000000000000014], [0.0, 0.0, 16.000000000000014], [0.0, -4.1181286595071782, 15.457838076589647], [0.0, -8.0185021993148613, 13.842209223679763], [0.0, -11.316904981336451, 11.309542762080202], [0.0, -13.863000364728078, 7.9840809071067564], [0.0, -15.444625056843165, 4.1657011248183453], [0.0, -16.000000000000004, 0.0], [4.1138343232165946, -15.458403436687785, 0.0], [8.0375090326388356, -13.82762476751426, 0.0], [11.287160738114133, -11.334079312371211, 0.0], [13.856406460551018, -8.0000000000000107, 0.0], [15.455720903316333, -4.1342101871053218, 0.0], [16.0, 0.0, 0.0], [15.460678851797899, 4.0965508295358308, 0.0], [13.866481853293946, 7.9756758501938112, 0.0], [11.326628010447113, 11.296871463842329, 0.0], [8.043648153839877, 13.822914054134234, 0.0], [4.1448453790158144, 15.453263789607988, 0.0], [0.0, 16.0, 0.0], [-4.0454000395817316, 15.467412981048914, 0.0], [-8.0224611111405419, 13.839171443792884, 0.0], [-11.287829499218216, 11.333566153927533, 0.0], [-13.833607792800755, 8.0297118022791238, 0.0], [-15.434334476147605, 4.1905447842982557, 0.0], [-16.0, 0.0, 0.0], [-15.462047296235257, -4.0861564620726787, 0.0], [-13.850754640000096, -8.0073655959447088, 0.0], [-11.255291084523227, -11.358533757669049, 0.0], [-8.015038275380487, -13.844867185998915, 0.0], [-4.1461778477027318, -15.452711863006423, 0.0], [0.0, -16.0, 0.0], [0.0, 16.000000000000004, 0.0], [0.0, 15.456591504922118, 4.1275973113776327], [0.0, 13.857412944147294, 7.9975701336515774], [0.0, 11.298017357172819, 11.325748735569276], [0.0, 8.0270223338758218, 13.835671494489926], [0.0, 4.1192288825866816, 15.45769322947333], [0.0, 0.0, 16.000000000000014], [0.0, 0.0, 0.0], [-16.0, 0.0, 0.0], [16.0, 0.0, 0.0]])
		Curve_Rename = cmds.rename(Curve,'Sphere')
		color = cmds.palettePort('color_set', q=True, setCurCell=True)
		if color > 0:
			cmds.setAttr(Curve_Rename + '.overrideEnabled', True)
			cmds.setAttr(Curve_Rename + '.overrideColor', color)
		scale = cmds.floatSliderGrp('ScaleSlider', q=True, value=True)
		cmds.xform(Curve_Rename, ws = True, s = [scale, scale, scale])
		cmds.makeIdentity(Curve_Rename	, apply = True, t = False, r = False, s = True, n = False)

	@staticmethod
	def Tt_Rig_Button02(self):
		Curve = cmds.curve(d = 1, p = [[0.0, 15.999755429001707, 0.0], [-15.999755429001707, -15.999755429001707, -15.999755429001707], [-15.999755429001707, -15.999755429001707, 15.999755429001707], [0.0, 15.999755429001707, 0.0], [-15.999755429001707, -15.999755429001707, 15.999755429001707], [15.999755429001707, -15.999755429001707, 15.999755429001707], [0.0, 15.999755429001707, 0.0], [15.999755429001707, -15.999755429001707, 15.999755429001707], [15.999755429001707, -15.999755429001707, -15.999755429001707], [0.0, 15.999755429001707, 0.0], [15.999755429001707, -15.999755429001707, -15.999755429001707], [-15.999755429001707, -15.999755429001707, -15.999755429001707]])
		Curve_Rename = cmds.rename(Curve,'Pyramid')
		color = cmds.palettePort('color_set', q=True, setCurCell=True)
		if color > 0:
			cmds.setAttr(Curve_Rename + '.overrideEnabled', True)
			cmds.setAttr(Curve_Rename + '.overrideColor', color)
		scale = cmds.floatSliderGrp('ScaleSlider', q=True, value=True)
		cmds.xform(Curve_Rename, ws = True, s = [scale, scale, scale])
		cmds.makeIdentity(Curve_Rename	, apply = True, t = False, r = False, s = True, n = False)

	@staticmethod
	def Tt_Rig_Button03(self):
		Curve = cmds.curve(d = 1, p = [[7.9997952514524657, 16.000032064532764, -13.856148105049], [-8.0000369483434923, 16.000032064532764, -13.856148105049], [-15.999627687042016, 16.000032064532764, 0.0], [-8.0000369483434923, 16.000032064532764, 13.856148105049], [7.9997952514524657, 16.000032064532764, 13.856148105049], [15.999627687042016, 16.000032064532764, 0.0], [7.9997952514524657, 16.000032064532764, -13.856148105049], [7.9997952514524657, -16.000032064532764, -13.856148105049], [-8.0000369483434923, -16.000032064532764, -13.856148105049], [-8.0000369483434923, 16.000032064532764, -13.856148105049], [-8.0000369483434923, -16.000032064532764, -13.856148105049], [-15.999627687042016, -16.000032064532764, 0.0], [-15.999627687042016, 16.000032064532764, 0.0], [-15.999627687042016, -16.000032064532764, 0.0], [-8.0000369483434923, -16.000032064532764, 13.856148105049], [-8.0000369483434923, 16.000032064532764, 13.856148105049], [-8.0000369483434923, -16.000032064532764, 13.856148105049], [7.9997952514524657, -16.000032064532764, 13.856148105049], [7.9997952514524657, 16.000032064532764, 13.856148105049], [7.9997952514524657, -16.000032064532764, 13.856148105049], [15.999627687042016, -16.000032064532764, 0.0], [15.999627687042016, 16.000032064532764, -9.8383029358253482e-05], [15.999627687042016, -16.000032064532764, 0.0], [7.9997952514524657, -16.000032064532764, -13.856148105049]])
		Curve_Rename = cmds.rename(Curve,'Prism')
		color = cmds.palettePort('color_set', q=True, setCurCell=True)
		if color > 0:
			cmds.setAttr(Curve_Rename + '.overrideEnabled', True)
			cmds.setAttr(Curve_Rename + '.overrideColor', color)
		scale = cmds.floatSliderGrp('ScaleSlider', q=True, value=True)
		cmds.xform(Curve_Rename, ws = True, s = [scale, scale, scale])
		cmds.makeIdentity(Curve_Rename	, apply = True, t = False, r = False, s = True, n = False)

	@staticmethod
	def Tt_Rig_Button04(self):
		Curve = cmds.curve(d = 1, p = [[0.0, 15.999668532723884, 0.0], [15.999668532723884, 0.0, 0.0], [0.0, 0.0, -15.999668532723884], [0.0, 15.999668532723884, 0.0], [0.0, 0.0, -15.999668532723884], [-15.999668532723884, 0.0, 0.0], [0.0, 15.999668532723884, 0.0], [-15.999668532723884, 0.0, 0.0], [0.0, 0.0, 15.999668532723884], [0.0, 15.999668532723884, 0.0], [0.0, 0.0, 15.999668532723884], [15.999668532723884, 0.0, 0.0], [0.0, -15.999668532723884, 0.0], [0.0, 0.0, -15.999668532723884], [0.0, -15.999668532723884, 0.0], [-15.999668532723884, 0.0, 0.0], [0.0, -15.999668532723884, 0.0], [0.0, 0.0, 15.999668532723884], [0.0, -15.999668532723884, 0.0]])
		Curve_Rename = cmds.rename(Curve,'Octahedron')
		color = cmds.palettePort('color_set', q=True, setCurCell=True)
		if color > 0:
			cmds.setAttr(Curve_Rename + '.overrideEnabled', True)
			cmds.setAttr(Curve_Rename + '.overrideColor', color)
		scale = cmds.floatSliderGrp('ScaleSlider', q=True, value=True)
		cmds.xform(Curve_Rename, ws = True, s = [scale, scale, scale])
		cmds.makeIdentity(Curve_Rename	, apply = True, t = False, r = False, s = True, n = False)

	@staticmethod
	def Tt_Rig_Button05(self):
		Curve = cmds.curve(d = 1, p = [[0.0, 0.0, -16.000155614386657], [-6.1229929289248366, 0.0, -14.78221684919226], [-11.313820044880201, 0.0, -11.313820044880201], [-14.78221684919226, 0.0, -6.1229929289248366], [-16.000155614386657, 0.0, 0.0], [-14.78221684919226, 0.0, 6.1229929289248366], [-11.313820044880201, 0.0, 11.313820044880201], [-6.1229929289248366, 0.0, 14.78221684919226], [0.0, 0.0, 16.000155614386657], [6.1229929289248366, 0.0, 14.78221684919226], [11.313820044880201, 0.0, 11.313820044880201], [14.78221684919226, 0.0, 6.1229929289248366], [16.000155614386657, 0.0, 0.0], [14.78221684919226, 0.0, -6.1229929289248366], [11.313820044880201, 0.0, -11.313820044880201], [6.1229929289248366, 0.0, -14.78221684919226], [0.0, 0.0, -16.000155614386657]])
		Curve_Rename = cmds.rename(Curve,'Circle')
		color = cmds.palettePort('color_set', q=True, setCurCell=True)
		if color > 0:
			cmds.setAttr(Curve_Rename + '.overrideEnabled', True)
			cmds.setAttr(Curve_Rename + '.overrideColor', color)
		scale = cmds.floatSliderGrp('ScaleSlider', q=True, value=True)
		cmds.xform(Curve_Rename, ws = True, s = [scale, scale, scale])
		cmds.makeIdentity(Curve_Rename	, apply = True, t = False, r = False, s = True, n = False)

	@staticmethod	    
	def Tt_Rig_Button06(self):
		Curve = cmds.curve(d = 1, p = [[-15.990000000000002, 0.0, -15.990000000000002], [-15.990000000000002, 0.0, 15.990000000000002], [15.990000000000002, 0.0, 15.990000000000002], [15.990000000000002, 0.0, -15.990000000000002], [-15.990000000000002, 0.0, -15.990000000000002]])
		Curve_Rename = cmds.rename(Curve,'Square')
		color = cmds.palettePort('color_set', q=True, setCurCell=True)
		if color > 0:
			cmds.setAttr(Curve_Rename + '.overrideEnabled', True)
			cmds.setAttr(Curve_Rename + '.overrideColor', color)
		scale = cmds.floatSliderGrp('ScaleSlider', q=True, value=True)
		cmds.xform(Curve_Rename, ws = True, s = [scale, scale, scale])
		cmds.makeIdentity(Curve_Rename	, apply = True, t = False, r = False, s = True, n = False)

	@staticmethod
	def Tt_Rig_Button07(self):
		Curve = cmds.curve(d = 1, p = [[0.0, 0.0, 23.026298905307815], [8.5063859234606696, 0.0, 18.42103912424626], [4.2531929617303348, 0.0, 18.42103912424626], [4.2531929617303348, 0.0, 18.42103912424626], [4.2531929617303348, 0.0, 18.42103912424626], [4.2531929617303348, 0.0, 18.42103912424626], [4.2519599462813469, 0.0, 15.891685731377999], [6.1743613908860713, 0.0, 14.888200802936126], [8.938345426909752, 0.0, 13.410820556091245], [11.396122420831603, 0.0, 11.39851488428549], [13.392327950339507, 0.0, 8.9666541704814087], [14.883436014207817, 0.0, 6.1832756836067224], [15.808866022825155, 0.0, 3.1428449624969645], [15.89102853178508, 0.0, 2.3086350095533357], [18.42103912424626, 0.0, 2.3026298905307825], [18.42103912424626, 0.0, 4.605259781061565], [23.026298905307815, 0.0, 0.0], [18.42103912424626, 0.0, -4.605259781061565], [18.42103912424626, 0.0, -2.3026298905307825], [15.923970595918588, 0.0, -2.3021927274410339], [15.809511136223751, 0.0, -3.1362950162414451], [14.8959953980933, 0.0, -6.1533246164526325], [13.402409600154497, 0.0, -8.9540812186847791], [11.412425935244839, 0.0, -11.379171756192978], [8.9686076369742533, 0.0, -13.390724781820229], [6.1742299056069418, 0.0, -14.888271083282024], [3.1525512748210365, 0.0, -15.806270039534574], [1.0031424782403122, 0.0, -15.918902617253663], [1.0029200943528929, 0.0, -18.42103912424626], [2.0058401887057857, 0.0, -18.42103912424626], [0.0, 0.0, -23.026298905307815], [-2.0058401887057857, 0.0, -18.42103912424626], [-1.0029200943528929, 0.0, -18.42103912424626], [-1.0029795533845798, 0.0, -15.918166491364808], [-3.1387886926894035, 0.0, -15.809265530530894], [-6.1624562988907963, 0.0, -14.893225332509951], [-8.9555299836332605, 0.0, -13.401457334551001], [-11.399040536125803, 0.0, -11.395481912210954], [-13.424281684079217, 0.0, -8.9131614277700191], [-14.894836915779306, 0.0, -6.1571436208348089], [-15.810391853202232, 0.0, -3.1273529466958028], [-15.906341638962481, 0.0, -2.2987595971615629], [-18.42103912424626, 0.0, -2.3026298905307825], [-18.42103912424626, 0.0, -4.605259781061565], [-23.026298905307815, 0.0, 0.0], [-18.42103912424626, 0.0, 4.605259781061565], [-18.42103912424626, 0.0, 2.3026298905307825], [-15.916523090020043, 0.0, 2.3047797771363507], [-15.808753039435363, 0.0, 3.1439921021046011], [-14.889597662297414, 0.0, 6.1717480508313081], [-13.39874308852335, 0.0, 8.9588373019872787], [-11.389334958518505, 0.0, 11.404085210649397], [-8.952034218499902, 0.0, 13.403503744548615], [-6.1665139421502406, 0.0, 14.891994459883922], [-4.2497026306738386, 0.0, 15.907741091389003], [-4.2531929617303348, 0.0, 18.42103912424626], [-8.5063859234606696, 0.0, 18.42103912424626], [0.0, 0.0, 23.026298905307815]])
		Curve_Rename = cmds.rename(Curve,'Arrow_Circle')
		color = cmds.palettePort('color_set', q=True, setCurCell=True)
		if color > 0:
			cmds.setAttr(Curve_Rename + '.overrideEnabled', True)
			cmds.setAttr(Curve_Rename + '.overrideColor', color)
		scale = cmds.floatSliderGrp('ScaleSlider', q=True, value=True)
		cmds.xform(Curve_Rename, ws = True, s = [scale, scale, scale])
		cmds.makeIdentity(Curve_Rename	, apply = True, t = False, r = False, s = True, n = False)

	@staticmethod
	def Tt_Rig_Button08(self):
		Curve = cmds.curve(d = 1, p = [[0.0, 0.0, 16.000001668145341], [-6.1411567412049965, 0.0, 5.3657405093437562], [-2.9625377116242788, 0.0, 5.333296704505174], [-2.9625377116242788, 0.0, -5.3655483874812919], [-6.1411567412049965, 0.0, -5.3655483874812919], [0.0, 0.0, -16.000001668145341], [6.1411567412049965, 0.0, -5.3655483874812919], [2.9625563040625811, 0.0, -5.3330983851632769], [2.9625563040625811, 0.0, 5.3657405093437562], [6.1411567412049965, 0.0, 5.3657405093437562], [0.0, 0.0, 16.000001668145341]])
		Curve_Rename = cmds.rename(Curve,'Double_Arrow')
		color = cmds.palettePort('color_set', q=True, setCurCell=True)
		if color > 0:
			cmds.setAttr(Curve_Rename + '.overrideEnabled', True)
			cmds.setAttr(Curve_Rename + '.overrideColor', color)
		scale = cmds.floatSliderGrp('ScaleSlider', q=True, value=True)
		cmds.xform(Curve_Rename, ws = True, s = [scale, scale, scale])
		cmds.makeIdentity(Curve_Rename	, apply = True, t = False, r = False, s = True, n = False)

	@staticmethod
	def Tt_Rig_Button09(self):
		Curve = cmds.curve(d = 1, p = [[0.0, 0.0, 16.0], [-6.1414866141732283, 0.0, 8.8888881889763773], [-2.9626645669291336, 0.0, 8.8564472440944879], [-2.9626645669291336, 0.0, 2.9625574803149606], [-8.8603275590551185, 0.0, 2.9625574803149606], [-8.8888881889763773, 0.0, 6.1411779527559061], [-16.0, 0.0, 0.0], [-8.8888881889763773, 0.0, -6.1411779527559061], [-8.856755905511811, 0.0, -2.9625574803149606], [-2.9626645669291336, 0.0, -2.9625574803149606], [-2.9626645669291336, 0.0, -8.8888881889763773], [-6.1414866141732283, 0.0, -8.8888881889763773], [0.0, 0.0, -16.0], [6.1410645669291339, 0.0, -8.8888881889763773], [2.9626897637795273, 0.0, -8.8852850393700784], [2.9626897637795273, 0.0, -2.9625574803149606], [8.8888881889763773, 0.0, -2.9625574803149606], [8.8888881889763773, 0.0, -6.1411779527559061], [16.0, 0.0, 0.0], [8.8888881889763773, 0.0, 6.1411779527559061], [8.8852724409448811, 0.0, 2.9625574803149606], [2.9626897637795273, 0.0, 2.9625574803149606], [2.9626897637795273, 0.0, 8.8600503937007868], [6.1410645669291339, 0.0, 8.8888881889763773], [0.0, 0.0, 16.0]])
		Curve_Rename = cmds.rename(Curve,'Quad_Arrow')
		color = cmds.palettePort('color_set', q=True, setCurCell=True)
		if color > 0:
			cmds.setAttr(Curve_Rename + '.overrideEnabled', True)
			cmds.setAttr(Curve_Rename + '.overrideColor', color)
		scale = cmds.floatSliderGrp('ScaleSlider', q=True, value=True)
		cmds.xform(Curve_Rename, ws = True, s = [scale, scale, scale])
		cmds.makeIdentity(Curve_Rename	, apply = True, t = False, r = False, s = True, n = False)

	@staticmethod
	def Tt_Rig_Button10(self):
		Curve = cmds.curve(d = 1, p = [[-2.4009185406449163, 0.0, -15.701629409832192], [-6.1229929289248366, 0.0, -14.78221684919226], [-11.313820044880201, 0.0, -11.313820044880201], [-14.78221684919226, 0.0, -6.1229929289248366], [-16.000155614386657, 0.0, 0.0], [-14.78221684919226, 0.0, 6.1229929289248366], [-11.313820044880201, 0.0, 11.313820044880201], [-6.1229929289248366, 0.0, 14.78221684919226], [0.0, 0.0, 16.000155614386657], [6.1229929289248366, 0.0, 14.78221684919226], [11.313820044880201, 0.0, 11.313820044880201], [14.78221684919226, 0.0, 6.1229929289248366], [16.000155614386657, 0.0, 0.0], [14.78221684919226, 0.0, -6.1229929289248366], [11.313820044880201, 0.0, -11.313820044880201], [8.6673016136207153, 0.0, -13.244781553953684], [10.330014013461584, 0.0, -16.14832901999192], [0.32890973536521306, 0.0, -14.262266815071186], [4.4484712581737451, 0.0, -5.2290108475947896], [5.863017911864298, 0.0, -8.107742372562571], [7.2183788311968735, 0.0, -7.2183788311968735], [9.4312613414687725, 0.0, -3.9065562335774922], [10.208322771163576, 0.0, 0.0], [9.4312613414687725, 0.0, 3.9065562335774922], [7.2183788311968735, 0.0, 7.2183788311968735], [3.9065562335774922, 0.0, 9.4312613414687725], [0.0, 0.0, 10.208322771163576], [-3.9065562335774922, 0.0, 9.4312613414687725], [-7.2183788311968735, 0.0, 7.2183788311968735], [-9.4312613414687725, 0.0, 3.9065562335774922], [-10.208322771163576, 0.0, 0.0], [-9.4312613414687725, 0.0, -3.9065562335774922], [-7.2183788311968735, 0.0, -7.2183788311968735], [-3.9065562335774922, 0.0, -9.4312613414687725], [-2.4009185406449163, 0.0, -9.7704547724034416], [-2.4009185406449163, 0.0, -15.701629409832192]])
		Curve_Rename = cmds.rename(Curve,'Circle_Arrow')
		color = cmds.palettePort('color_set', q=True, setCurCell=True)
		if color > 0:
			cmds.setAttr(Curve_Rename + '.overrideEnabled', True)
			cmds.setAttr(Curve_Rename + '.overrideColor', color)
		scale = cmds.floatSliderGrp('ScaleSlider', q=True, value=True)
		cmds.xform(Curve_Rename, ws = True, s = [scale, scale, scale])
		cmds.makeIdentity(Curve_Rename	, apply = True, t = False, r = False, s = True, n = False)

	@staticmethod
	def Tt_Rig_Button11(self):
		Curve = cmds.curve(d = 1, p = [[0.32890973536521306, 0.0, 14.262266815071184], [4.448471258173746, 0.0, 5.2290108475947887], [5.863017911864298, 0.0, 8.107742372562571], [7.2183788311968735, 0.0, 7.2183788311968735], [9.4312613414687725, 0.0, 3.9065562335774922], [10.208322771163576, 0.0, 0.0], [9.4312613414687725, 0.0, -3.9065562335774922], [7.2183788311968735, 0.0, -7.2183788311968735], [5.863017911864298, 0.0, -8.107742372562571], [4.448471258173746, 0.0, -5.2290108475947887], [0.32890973536521306, 0.0, -14.262266815071184], [10.330014013461586, 0.0, -16.14832901999192], [8.6673016136207135, 0.0, -13.244781553953684], [11.313820044880201, 0.0, -11.313820044880201], [14.78221684919226, 0.0, -6.1229929289248366], [16.000155614386657, 0.0, 0.0], [14.78221684919226, 0.0, 6.1229929289248366], [11.313820044880201, 0.0, 11.313820044880201], [8.6673016136207135, 0.0, 13.244781553953684], [10.330014013461586, 0.0, 16.14832901999192], [0.32890973536521306, 0.0, 14.262266815071184]])
		Curve_Rename = cmds.rename(Curve,'Half_Circle_Arrow')
		color = cmds.palettePort('color_set', q=True, setCurCell=True)
		if color > 0:
			cmds.setAttr(Curve_Rename + '.overrideEnabled', True)
			cmds.setAttr(Curve_Rename + '.overrideColor', color)
		scale = cmds.floatSliderGrp('ScaleSlider', q=True, value=True)
		cmds.xform(Curve_Rename, ws = True, s = [scale, scale, scale])
		cmds.makeIdentity(Curve_Rename	, apply = True, t = False, r = False, s = True, n = False)

	@staticmethod
	def Tt_Rig_Button12(self):
		Curve = cmds.curve(d = 1, p = [[10.837687409727408, 0.0, 4.8252493233554805], [5.6700820482251082, 0.0, 6.2972641194374495], [6.8040978113702382, 0.0, 7.5567166200749956], [5.0842828391652688, 0.0, 8.8062368620584994], [3.1422591870328498, 0.0, 9.6708811720575412], [1.0629040075191774, 0.0, 10.112862439506712], [-1.0629053207220829, 0.0, 10.112862439506712], [-3.1422606012513645, 0.0, 9.6708819801824077], [-5.0842844554149984, 0.0, 8.8062376701833642], [-6.8041010438696983, 0.0, 7.5567182363247252], [-9.0721341864096878, 0.0, 10.07562404572468], [-6.7790459405533321, 0.0, 11.741650226911151], [-4.1896809363559626, 0.0, 12.894509037534926], [-1.4172070606242415, 0.0, 13.483816316633993], [1.4172053433589031, 0.0, 13.483816316633993], [4.1896789160438006, 0.0, 12.894508229410055], [6.7790435161787368, 0.0, 11.741648610661423], [9.0721309539102286, 0.0, 10.075622429474947], [10.206147525180224, 0.0, 11.335075334174926], [10.837687409727408, 0.0, 4.8252493233554805]])
		Curve_Rename = cmds.rename(Curve,'R_Half_Circle_Arrow')
		color = cmds.palettePort('color_set', q=True, setCurCell=True)
		if color > 0:
			cmds.setAttr(Curve_Rename + '.overrideEnabled', True)
			cmds.setAttr(Curve_Rename + '.overrideColor', color)
		scale = cmds.floatSliderGrp('ScaleSlider', q=True, value=True)
		cmds.xform(Curve_Rename, ws = True, s = [scale, scale, scale])
		cmds.makeIdentity(Curve_Rename	, apply = True, t = False, r = False, s = True, n = False)

	@staticmethod
	def Tt_Rig_Button13(self):
		Curve = cmds.curve(d = 1, p = [[-10.837691450351734, 0.0, 4.8252497274179147], [-10.206150757679682, 0.0, 11.335076950424655], [-9.0721341864096878, 0.0, 10.07562404572468], [-6.7790459405533321, 0.0, 11.741650226911151], [-4.1896809363559626, 0.0, 12.894509037534926], [-1.4172070606242415, 0.0, 13.483816316633993], [1.4172053433589031, 0.0, 13.483816316633993], [4.1896789160438006, 0.0, 12.894508229410055], [6.7790435161787368, 0.0, 11.741648610661423], [9.0721309539102286, 0.0, 10.075622429474947], [6.8040978113702382, 0.0, 7.5567166200749956], [5.0842828391652688, 0.0, 8.8062368620584994], [3.1422591870328498, 0.0, 9.6708811720575412], [1.0629040075191774, 0.0, 10.112862439506712], [-1.0629053207220829, 0.0, 10.112862439506712], [-3.1422606012513645, 0.0, 9.6708819801824077], [-5.0842844554149984, 0.0, 8.8062376701833642], [-6.8041010438696983, 0.0, 7.5567182363247252], [-5.6700836644748387, 0.0, 6.2972649275623152], [-10.837691450351734, 0.0, 4.8252497274179147]])
		Curve_Rename = cmds.rename(Curve,'L_Half_Circle_Arrow')
		color = cmds.palettePort('color_set', q=True, setCurCell=True)
		if color > 0:
			cmds.setAttr(Curve_Rename + '.overrideEnabled', True)
			cmds.setAttr(Curve_Rename + '.overrideColor', color)
		scale = cmds.floatSliderGrp('ScaleSlider', q=True, value=True)
		cmds.xform(Curve_Rename, ws = True, s = [scale, scale, scale])
		cmds.makeIdentity(Curve_Rename	, apply = True, t = False, r = False, s = True, n = False)

	@staticmethod
	def Tt_Rig_Button14(self):
		Curve = cmds.curve(d = 1, p = [[0.0, -3.5504932327512507e-15, 15.99], [-6.3960000000000008, -2.1302959396507502e-15, 9.5940000000000012], [-3.1980000000000004, -2.1302959396507502e-15, 9.5940000000000012], [-3.1980000000000004, 0.0, 0.0], [3.1980000000000004, 0.0, 0.0], [3.1980000000000004, -2.1302959396507502e-15, 9.5940000000000012], [6.3960000000000008, -2.1302959396507502e-15, 9.5940000000000012], [0.0, -3.5504932327512507e-15, 15.99]])
		Curve_Rename = cmds.rename(Curve,'Single_Arrow')
		color = cmds.palettePort('color_set', q=True, setCurCell=True)
		if color > 0:
			cmds.setAttr(Curve_Rename + '.overrideEnabled', True)
			cmds.setAttr(Curve_Rename + '.overrideColor', color)
		scale = cmds.floatSliderGrp('ScaleSlider', q=True, value=True)
		cmds.xform(Curve_Rename, ws = True, s = [scale, scale, scale])
		cmds.makeIdentity(Curve_Rename	, apply = True, t = False, r = False, s = True, n = False)

	@staticmethod
	def Tt_Rig_Button15(self):
		Curve = cmds.curve(d = 1, p = [[-2.0837488086736507e-14, -1.1368964172363258, -15.958007537346161], [-6.3960000000000008, 0.20310418167114488, -9.6197905645275146], [-3.1980000000000004, 0.20310418167114488, -9.6197905645275146], [-3.1980000000000004, 0.62313568725586166, -6.4225789164394245], [-3.1980000000000004, 0.8754559158325218, -3.2140993473991109], [-3.1980000000000004, 0.95960738983154525, 1.8585436000170167e-05], [-3.1980000000000004, 0.87544981613159412, 3.2141365563950823], [-3.1980000000000004, 0.62311738815307849, 6.4226149054683148], [-3.1980000000000004, 0.2030736831665062, 9.6198259435728648], [-6.3960000000000008, 0.2030736831665062, 9.6198259435728648], [-2.0837478605896728e-14, -1.1369391151428201, 15.958039256490268], [6.3960000000000008, 0.2030736831665062, 9.6198259435728648], [3.1980000000000004, 0.2030736831665062, 9.6198259435728648], [3.1980000000000004, 0.62311738815307849, 6.4226149054683148], [3.1980000000000004, 0.87544981613159412, 3.2141365563950823], [3.1980000000000004, 0.95960738983154525, 1.8585436000170167e-05], [3.1980000000000004, 0.8754559158325218, -3.2140993473991109], [3.1980000000000004, 0.62313568725586166, -6.4225789164394245], [3.1980000000000004, 0.20310418167114488, -9.6197905645275146], [6.3960000000000008, 0.20310418167114488, -9.6197905645275146], [-2.0837488086736507e-14, -1.1368964172363258, -15.958007537346161]])
		Curve_Rename = cmds.rename(Curve,'Double_Arrow_Arch')
		color = cmds.palettePort('color_set', q=True, setCurCell=True)
		if color > 0:
			cmds.setAttr(Curve_Rename + '.overrideEnabled', True)
			cmds.setAttr(Curve_Rename + '.overrideColor', color)
		scale = cmds.floatSliderGrp('ScaleSlider', q=True, value=True)
		cmds.xform(Curve_Rename, ws = True, s = [scale, scale, scale])
		cmds.makeIdentity(Curve_Rename	, apply = True, t = False, r = False, s = True, n = False)

	@staticmethod
	def Tt_Rig_Button16(self):
		Curve = cmds.curve(d = 1, p = [[-4.9497470855712891, -7.0, 4.9497470855712891], [0.0, -7.0, 0.0], [0.0, -7.0, 6.9999995231628418], [-4.9497470855712891, -7.0, 4.9497470855712891], [-6.9999990463256836, -7.0, 0.0], [-4.9497470855712891, -7.0, -4.9497470855712891], [0.0, -7.0, -6.9999990463256836], [4.9497470855712891, -7.0, -4.9497470855712891], [7.0, -7.0, 0.0], [4.9497475624084473, -7.0, 4.9497475624084473], [0.0, -7.0, 6.9999995231628418], [0.0, 7.0, 0.0], [4.9497475624084473, -7.0, 4.9497475624084473], [0.0, -7.0, 0.0], [-6.9999990463256836, -7.0, 0.0], [0.0, 7.0, 0.0], [7.0, -7.0, 0.0], [0.0, -7.0, 0.0], [-4.9497470855712891, -7.0, -4.9497470855712891], [0.0, 7.0, 0.0], [4.9497470855712891, -7.0, -4.9497470855712891], [0.0, -7.0, 0.0], [0.0, -7.0, -6.9999990463256836], [0.0, 7.0, 0.0]]) 
		Curve_Rename = cmds.rename(Curve,'Cone')
		color = cmds.palettePort('color_set', q=True, setCurCell=True)
		if color > 0:
			cmds.setAttr(Curve_Rename + '.overrideEnabled', True)
			cmds.setAttr(Curve_Rename + '.overrideColor', color)
		scale = cmds.floatSliderGrp('ScaleSlider', q=True, value=True)
		cmds.xform(Curve_Rename, ws = True, s = [scale, scale, scale])
		cmds.makeIdentity(Curve_Rename	, apply = True, t = False, r = False, s = True, n = False)


if __name__ == "__main__":
    
    Tt_Rig_cont.Tt_Rig_controller()
    
  