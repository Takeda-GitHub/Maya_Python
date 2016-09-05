# -*- coding: utf-8 -*-

import maya.cmds as cmds
import maya.mel as mel


def SetSpeed(item):
	if item == "realtime":
		cmds.playbackOptions( edit=True , ps=1.0)
	elif item == "2x":
		cmds.playbackOptions( edit=True , ps=2.0)
	elif item == "1/2x":
		cmds.playbackOptions( edit=True , ps=0.5)

def step_backward(grp_panel_no_a):

    curr = cmds.currentTime( query=True )
    min = cmds.playbackOptions(query=True,minTime=True)
    max = cmds.playbackOptions(query=True,maxTime=True)

    if curr > min:
        cmds.currentTime(curr - 1,edit=True)
    else:
        cmds.currentTime(curr,edit=True)

def step_forward(grp_panel_no_a):

    curr = cmds.currentTime( query=True )
    min = cmds.playbackOptions(query=True,minTime=True)
    max = cmds.playbackOptions(query=True,maxTime=True)

    if curr < max:
        cmds.currentTime(curr + 1,edit=True)
    else:
        cmds.currentTime(curr,edit=True)

def play_forward(grp_panel_no_a):
    if cmds.symbolButton('play_forward'+ grp_panel_no_a,q=True,image=True) == 'timeplay.xpm':
        cmds.symbolButton('play_forward'+ grp_panel_no_a,edit=True,image='timestop.xpm')
    elif cmds.symbolButton('play_forward'+ grp_panel_no_a,q=True,image=True) == 'timestop.xpm':
        cmds.symbolButton('play_forward'+ grp_panel_no_a,edit=True,image='timeplay.xpm')
    mel.eval('playButtonForward;')


def select_objfrom_curve(*args):
    if not cmds.keyframe( query=True, selected=True, name=True):
        print 'No Curve is selected'
    else:
        selected_list = cmds.ls( selection=True )
        selected_f_curve = cmds.keyframe( query=True, selected=True, name=True)[0]
        selected_connect = cmds.listConnections(selected_f_curve,plugs=True)[0]

        if cmds.nodeType(selected_connect) == 'character':
            selected_obj = cmds.listConnections( selected_connect, type='transform')[0]
        else:
            selected_att = cmds.listConnections(selected_f_curve,plugs=True)[0]
            selected_obj = selected_att.split(".")[0]

        cmds.select(clear=True)

        if selected_obj in selected_list:
            selected_list.remove(selected_obj)
            cmds.select(clear=True)
            cmds.select(selected_obj,r=True)
            cmds.selectKey(selected_f_curve,add=True)
            for o_obj in selected_list:
                cmds.select(o_obj, add=True)
        else:
            cmds.select(selected_obj ,r=True)
            cmds.selectKey(selected_f_curve,add=True)

def select_objfrom_curve2( dragControl, x, y, modifiers ):
    if modifiers == 0:
        try:
            selected_f_curve = cmds.keyframe( query=True, selected=True, name=True)
            cmds.select(clear=True)
            for o_curve in selected_f_curve:
                selected_connect = cmds.listConnections(o_curve,plugs=True)[0]

                if cmds.nodeType(selected_connect) == 'character':
                    selected_obj = cmds.listConnections( selected_connect, type='transform')[0]
                else:
                    selected_att = cmds.listConnections(o_curve,plugs=True)[0]
                    selected_obj = selected_att.split(".")[0]

                cmds.select(selected_obj,add=True)
                cmds.selectKey(selected_f_curve,add=True)
        except:
            print 'Animation Key is Not Selected'

def select_curve_tx(*args):
    if not cmds.ls( sl=True ):
        print 'Nothing is selected'
    else:
        first_selected = cmds.ls( sl=True )[0]
        cmds.selectKey(first_selected,replace=True,attribute='translateX')

def filter_tx( dragControl, x, y, modifiers ):
    print "dragControl" + dragControl
    if not cmds.ls( sl=True ):
        print 'Nothing is selected'
    else:
        if modifiers == 0:
            first_selected = cmds.ls( sl=True )
            for i in range(len(first_selected)):
                if i == 0:
                    cmds.selectKey(first_selected[i],replace=True,attribute='translateX')
                else:
                    cmds.selectKey(first_selected[i],add=True,attribute='translateX')
        elif modifiers == 1:
            outline_ed_name = "graphEditor" + dragControl.split("|").pop()[len('b_c_tx'):] + 'OutlineEd'
            mel.eval('string $outlineed_name = "%s"' % outline_ed_name)
            c_tx = cmds.button(dragControl.split("|").pop(),q=1,bgc=True)
            if(c_tx==[0.30000762951094834, 0.0, 0.0]):
                cmds.button(dragControl.split("|").pop(),edit=1,bgc=[1.0,0.0,0.0])
                mel.eval('filterUISelectAttributesCheckbox translateX 1 $outlineed_name;')
            elif(c_tx==[1.0,0.0,0.0]):
                cmds.button(dragControl.split("|").pop(),edit=1,bgc=[0.3,0.0,0.0])
                mel.eval('filterUISelectAttributesCheckbox translateX 0 $outlineed_name;')

def filter_tx2(*args):
    pass

def select_curve_ty(*args):
    if not cmds.ls( sl=True ):
        print 'Nothing is selected'
    else:
        first_selected = cmds.ls( sl=True )[0]
        cmds.selectKey(first_selected,replace=True,attribute='translateY')

def filter_ty( dragControl, x, y, modifiers ):
    if not cmds.ls( sl=True ):
        print 'Nothing is selected'
    else:
        if modifiers == 0:
            first_selected = cmds.ls( sl=True )
            for i in range(len(first_selected)):
                if i == 0:
                    cmds.selectKey(first_selected[i],replace=True,attribute='translateY')
                else:
                    cmds.selectKey(first_selected[i],add=True,attribute='translateY')
        elif modifiers == 1:
            outline_ed_name = "graphEditor" + dragControl.split("|").pop()[len('b_c_ty'):] + 'OutlineEd'
            mel.eval('string $outlineed_name = "%s"' % outline_ed_name)
            c_ty = cmds.button(dragControl.split("|").pop(),q=1,bgc=True)
            if(c_ty==[0.0,0.30000762951094834,0.0]):
                cmds.button(dragControl.split("|").pop(),edit=1,bgc=[0.0,1.0,0.0])
                mel.eval('filterUISelectAttributesCheckbox translateY 1 $outlineed_name;')
            elif(c_ty==[0.0,1.0,0.0]):
                cmds.button(dragControl.split("|").pop(),edit=1,bgc=[0.0,0.3,0.0])
                mel.eval('filterUISelectAttributesCheckbox translateY 0 $outlineed_name;')

def filter_ty2(*args):
    pass

def select_curve_tz(*args):
    if not cmds.ls( sl=True ):
        print 'Nothing is selected'
    else:
        first_selected = cmds.ls( sl=True )[0]
        cmds.selectKey(first_selected,replace=True,attribute='translateZ')

def filter_tz( dragControl, x, y, modifiers ):
    if not cmds.ls( sl=True ):
        print 'Nothing is selected'
    else:
        if modifiers == 0:
            first_selected = cmds.ls( sl=True )
            for i in range(len(first_selected)):
                if i == 0:
                    cmds.selectKey(first_selected[i],replace=True,attribute='translateZ')
                else:
                    cmds.selectKey(first_selected[i],add=True,attribute='translateZ')
        elif modifiers == 1:
            outline_ed_name = "graphEditor" + dragControl.split("|").pop()[len('b_c_tz'):] + 'OutlineEd'
            mel.eval('string $outlineed_name = "%s"' % outline_ed_name)
            c_tz = cmds.button(dragControl.split("|").pop(),q=1,bgc=True)
            if(c_tz==[0.0,0.0,0.30000762951094834]):
                cmds.button(dragControl.split("|").pop(),edit=1,bgc=[0.0,0.0,1.0])
                mel.eval('filterUISelectAttributesCheckbox translateZ 1 $outlineed_name;')
            elif(c_tz==[0.0,0.0,1.0]):
                cmds.button(dragControl.split("|").pop(),edit=1,bgc=[0.0,0.0,0.3])
                mel.eval('filterUISelectAttributesCheckbox translateZ 0 $outlineed_name;')

def filter_tz2(*args):
    pass

def select_curve_rx(*args):
    if not cmds.ls( sl=True ):
        print 'Nothing is selected'
    else:
        first_selected = cmds.ls( sl=True )[0]
        cmds.selectKey(first_selected,replace=True,attribute='rotateX')

def filter_rx( dragControl, x, y, modifiers ):
    if not cmds.ls( sl=True ):
        print 'Nothing is selected'
    else:
        if modifiers == 0:
            first_selected = cmds.ls( sl=True )
            for i in range(len(first_selected)):
                if i == 0:
                    cmds.selectKey(first_selected[i],replace=True,attribute='rotateX')
                else:
                    cmds.selectKey(first_selected[i],add=True,attribute='rotateX')
        elif modifiers == 1:
            outline_ed_name = "graphEditor" + dragControl.split("|").pop()[len('b_c_rx'):] + 'OutlineEd'
            mel.eval('string $outlineed_name = "%s"' % outline_ed_name)
            c_rx = cmds.button(dragControl.split("|").pop(),q=1,bgc=True)
            if(c_rx==[0.30000762951094834, 0.0, 0.0]):
                cmds.button(dragControl.split("|").pop(),edit=1,bgc=[1.0,0.0,0.0])
                mel.eval('filterUISelectAttributesCheckbox rotateX 1 $outlineed_name;')
            elif(c_rx==[1.0,0.0,0.0]):
                cmds.button(dragControl.split("|").pop(),edit=1,bgc=[0.3,0.0,0.0])
                mel.eval('filterUISelectAttributesCheckbox rotateX 0 $outlineed_name;')

def filter_rx2(*args):
    pass

def select_curve_ry(*args):
    if not cmds.ls( sl=True ):
        print 'Nothing is selected'
    else:
        first_selected = cmds.ls( sl=True )[0]
        cmds.selectKey(first_selected,replace=True,attribute='rotateY')

def filter_ry( dragControl, x, y, modifiers ):
    if not cmds.ls( sl=True ):
        print 'Nothing is selected'
    else:
        if modifiers == 0:
            first_selected = cmds.ls( sl=True )
            for i in range(len(first_selected)):
                if i == 0:
                    cmds.selectKey(first_selected[i],replace=True,attribute='rotateY')
                else:
                    cmds.selectKey(first_selected[i],add=True,attribute='rotateY')
        elif modifiers == 1:
            outline_ed_name = "graphEditor" + dragControl.split("|").pop()[len('b_c_ry'):] + 'OutlineEd'
            mel.eval('string $outlineed_name = "%s"' % outline_ed_name)
            c_ry = cmds.button(dragControl.split("|").pop(),q=1,bgc=True)
            if(c_ry==[0.0,0.30000762951094834,0.0]):
                cmds.button(dragControl.split("|").pop(),edit=1,bgc=[0.0,1.0,0.0])
                mel.eval('filterUISelectAttributesCheckbox rotateY 1 $outlineed_name;')
            elif(c_ry==[0.0,1.0,0.0]):
                cmds.button(dragControl.split("|").pop(),edit=1,bgc=[0.0,0.3,0.0])
                mel.eval('filterUISelectAttributesCheckbox rotateY 0 $outlineed_name;')

def filter_ry2(*args):
    pass

def select_curve_rz(*args):
    if not cmds.ls( sl=True ):
        print 'Nothing is selected'
    else:
        first_selected = cmds.ls( sl=True )[0]
        cmds.selectKey(first_selected,replace=True,attribute='rotateZ')

def filter_rz( dragControl, x, y, modifiers ):
    if not cmds.ls( sl=True ):
        print 'Nothing is selected'
    else:
        if modifiers == 0:
            first_selected = cmds.ls( sl=True )
            for i in range(len(first_selected)):
                if i == 0:
                    cmds.selectKey(first_selected[i],replace=True,attribute='rotateZ')
                else:
                    cmds.selectKey(first_selected[i],add=True,attribute='rotateZ')
        elif modifiers == 1:
            outline_ed_name = "graphEditor" + dragControl.split("|").pop()[len('b_c_rz'):] + 'OutlineEd'
            mel.eval('string $outlineed_name = "%s"' % outline_ed_name)
            c_rz = cmds.button(dragControl.split("|").pop(),q=1,bgc=True)
            if(c_rz==[0.0,0.0,0.30000762951094834]):
                cmds.button(dragControl.split("|").pop(),edit=1,bgc=[0.0,0.0,1.0])
                mel.eval('filterUISelectAttributesCheckbox rotateZ 1 $outlineed_name;')
            elif(c_rz==[0.0,0.0,1.0]):
                cmds.button(dragControl.split("|").pop(),edit=1,bgc=[0.0,0.0,0.3])
                mel.eval('filterUISelectAttributesCheckbox rotateZ 0 $outlineed_name;')

def filter_rz2(*args):
    pass

def select_curve_sx(*args):
    if not cmds.ls( sl=True ):
        print 'Nothing is selected'
    else:
        first_selected = cmds.ls( sl=True )[0]
        cmds.selectKey(first_selected,replace=True,attribute='scaleX')

def filter_sx( dragControl, x, y, modifiers ):
    if not cmds.ls( sl=True ):
        print 'Nothing is selected'
    else:
        if modifiers == 0:
            first_selected = cmds.ls( sl=True )
            for i in range(len(first_selected)):
                if i == 0:
                    cmds.selectKey(first_selected[i],replace=True,attribute='scaleX')
                else:
                    cmds.selectKey(first_selected[i],add=True,attribute='scaleX')
        elif modifiers == 1:
            outline_ed_name = "graphEditor" + dragControl.split("|").pop()[len('b_c_sx'):] + 'OutlineEd'
            mel.eval('string $outlineed_name = "%s"' % outline_ed_name)
            c_sx = cmds.button(dragControl.split("|").pop(),q=1,bgc=True)
            if(c_sx==[0.30000762951094834, 0.0, 0.0]):
                cmds.button(dragControl.split("|").pop(),edit=1,bgc=[1.0,0.0,0.0])
                mel.eval('filterUISelectAttributesCheckbox scaleX 1 $outlineed_name;')
            elif(c_sx==[1.0,0.0,0.0]):
                cmds.button(dragControl.split("|").pop(),edit=1,bgc=[0.3,0.0,0.0])
                mel.eval('filterUISelectAttributesCheckbox scaleX 0 $outlineed_name;')

def filter_sx2(*args):
    pass

def select_curve_sy(*args):
    if not cmds.ls( sl=True ):
        print 'Nothing is selected'
    else:
        first_selected = cmds.ls( sl=True )[0]
        cmds.selectKey(first_selected,replace=True,attribute='scaleY')

def filter_sy( dragControl, x, y, modifiers ):
    if not cmds.ls( sl=True ):
        print 'Nothing is selected'
    else:
        if modifiers == 0:
            first_selected = cmds.ls( sl=True )
            for i in range(len(first_selected)):
                if i == 0:
                    cmds.selectKey(first_selected[i],replace=True,attribute='scaleY')
                else:
                    cmds.selectKey(first_selected[i],add=True,attribute='scaleY')
        elif modifiers == 1:
            outline_ed_name = "graphEditor" + dragControl.split("|").pop()[len('b_c_sy'):] + 'OutlineEd'
            mel.eval('string $outlineed_name = "%s"' % outline_ed_name)
            c_sy = cmds.button(dragControl.split("|").pop(),q=1,bgc=True)
            if(c_sy==[0.0,0.30000762951094834,0.0]):
                cmds.button(dragControl.split("|").pop(),edit=1,bgc=[0.0,1.0,0.0])
                mel.eval('filterUISelectAttributesCheckbox scaleY 1 $outlineed_name;')
            elif(c_sy==[0.0,1.0,0.0]):
                cmds.button(dragControl.split("|").pop(),edit=1,bgc=[0.0,0.3,0.0])
                mel.eval('filterUISelectAttributesCheckbox scaleY 0 $outlineed_name;')

def filter_sy2(*args):
    pass

def select_curve_sz(*args):
    if not cmds.ls( sl=True ):
        print 'Nothing is selected'
    else:
        first_selected = cmds.ls( sl=True )[0]
        cmds.selectKey(first_selected,replace=True,attribute='scaleZ')

def filter_sz( dragControl, x, y, modifiers ):
    if not cmds.ls( sl=True ):
        print 'Nothing is selected'
    else:
        if modifiers == 0:
            first_selected = cmds.ls( sl=True )
            for i in range(len(first_selected)):
                if i == 0:
                    cmds.selectKey(first_selected[i],replace=True,attribute='scaleZ')
                else:
                    cmds.selectKey(first_selected[i],add=True,attribute='scaleZ')
        elif modifiers == 1:
            outline_ed_name = "graphEditor" + dragControl.split("|").pop()[len('b_c_sz'):] + 'OutlineEd'
            mel.eval('string $outlineed_name = "%s"' % outline_ed_name)
            c_sz = cmds.button(dragControl.split("|").pop(),q=1,bgc=True)
            if(c_sz==[0.0,0.0,0.30000762951094834]):
                cmds.button(dragControl.split("|").pop(),edit=1,bgc=[0.0,0.0,1.0])
                mel.eval('filterUISelectAttributesCheckbox scaleZ 1 $outlineed_name;')
            elif(c_sz==[0.0,0.0,1.0]):
                cmds.button(dragControl.split("|").pop(),edit=1,bgc=[0.0,0.0,0.3])
                mel.eval('filterUISelectAttributesCheckbox scaleZ 0 $outlineed_name;')

def filter_sz2(*args):
    pass

def select_curve_v(*args):
    if not cmds.ls( sl=True ):
        print 'Nothing is selected'
    else:
        first_selected = cmds.ls( sl=True )[0]
        cmds.selectKey(first_selected,replace=True,attribute='visibility')

def filter_v( dragControl, x, y, modifiers ):
    if not cmds.ls( sl=True ):
        print 'Nothing is selected'
    else:
        if modifiers == 0:
            first_selected = cmds.ls( sl=True )
            for i in range(len(first_selected)):
                if i == 0:
                    cmds.selectKey(first_selected[i],replace=True,attribute='visibility')
                else:
                    cmds.selectKey(first_selected[i],add=True,attribute='visibility')
        elif modifiers == 1:
            outline_ed_name = "graphEditor" + dragControl.split("|").pop()[len('b_c_v'):] + 'OutlineEd'
            mel.eval('string $outlineed_name = "%s"' % outline_ed_name)
            c_v = cmds.button(dragControl.split("|").pop(),q=1,bgc=True)
            if(c_v==[0.30000762951094834, 0.30000762951094834, 0.30000762951094834]):
                cmds.button(dragControl.split("|").pop(),edit=1,bgc=[0.8,0.8,0.8])
                mel.eval('filterUISelectAttributesCheckbox visibility 1 $outlineed_name;')
            elif(c_v==[0.8,0.8,0.8]):
                cmds.button(dragControl.split("|").pop(),edit=1,bgc=[0.3,0.3,0.3])
                mel.eval('filterUISelectAttributesCheckbox visibility 0 $outlineed_name;')

def filter_v2(*args):
    pass

def o_prev_cmd(*args):
    n_prevCmd = int(cmds.findKeyframe(timeSlider=True, which='previous' ))
    cmds.currentTime(n_prevCmd, edit=True )

def o_key_prev_cmd( dragControl, x, y, modifiers ):
    if modifiers == 0:
        try:
            selected_f_curve = cmds.keyframe( query=True, selected=True, name=True)[0]
            selected_f_curve_key = cmds.keyframe( query=True, selected=True)[0]

            cmds.selectKey(selected_f_curve)
            selected_f_curve_keys = cmds.keyframe( query=True, selected=True)

            o_index = 0
            for o_frame in selected_f_curve_keys:
                if selected_f_curve_key <= o_frame:
                    break
                o_index = o_index + 1

            b_frame = selected_f_curve_keys[o_index - 1]

#            cmds.selectKey(selected_f_curve_obj, time=(b_frame,b_frame), attribute=selected_f_curve_att )
            cmds.selectKey(selected_f_curve, time=(b_frame,b_frame),r=True,keyframe=True)

        except:
            print 'Animation Key is Not Selected'

    elif modifiers == 1:
        try:
            selected_f_curve = cmds.keyframe( query=True, selected=True, name=True)[0]
            cmds.selectKey(selected_f_curve)

            selected_f_curve_keys = cmds.keyframe( query=True, selected=True)

            o_current_time = int(cmds.currentTime( query=True ))

            o_index = 0
            for o_frame in selected_f_curve_keys:
                if o_current_time <= o_frame:
                    break
                o_index = o_index + 1

            b_frame = selected_f_curve_keys[o_index - 1]

#            cmds.selectKey(selected_f_curve_obj, time=(b_frame,b_frame), attribute=selected_f_curve_att )
            cmds.selectKey(selected_f_curve, time=(b_frame,b_frame),r=True,keyframe=True)
        except:
            print 'Animation Key is Not Selected'

def o_key_prev_cmd2(*args):
    pass

def o_next_cmd(*args):
    n_nextCmd = int(cmds.findKeyframe(timeSlider=True, which='next' ))
    cmds.currentTime(n_nextCmd, edit=True )

def o_key_next_cmd( dragControl, x, y, modifiers ):
    if modifiers == 0:
        try:
            selected_f_curve = cmds.keyframe( query=True, selected=True, name=True)[0]
            selected_f_curve_key = cmds.keyframe( query=True, selected=True)[0]

            cmds.selectKey(selected_f_curve)
            selected_f_curve_keys = cmds.keyframe( query=True, selected=True)

            for o_frame in selected_f_curve_keys:
                if selected_f_curve_key < o_frame:
                    break
#            cmds.selectKey(selected_f_curve_obj, time=(o_frame,o_frame), attribute=selected_f_curve_att )
            cmds.selectKey(selected_f_curve, time=(o_frame,o_frame),r=True,keyframe=True)

        except:
            print 'Animation Key is Not Selected'

    elif modifiers == 1:
        try:
            selected_f_curve = cmds.keyframe( query=True, selected=True, name=True)[0]
            cmds.selectKey(selected_f_curve)

            selected_f_curve_keys = cmds.keyframe( query=True, selected=True)

            o_current_time = int(cmds.currentTime( query=True ))

            for o_frame in selected_f_curve_keys:
                if o_current_time < o_frame:
                    break

#            cmds.selectKey(selected_f_curve_obj, time=(o_frame,o_frame), attribute=selected_f_curve_att )
            cmds.selectKey(selected_f_curve, time=(o_frame,o_frame),r=True,keyframe=True)

        except:
            print 'Animation Key is Not Selected'

def o_key_next_cmd2(*args):
    pass




def RetimeHelper(*args):
	cur = cmds.currentTime( query=True )
	TimeSet = cmds.currentUnit(q=True,time=True)

	if TimeSet == "ntscf":
		No = 60.0
	else:
		No = 30.0

	Set = cur / No
	cmds.retimeHelper(edit=True , frame=Set)

def Cycle_On(*args):
	try:
		mel.eval('setInfinity -pri cycle;')
		mel.eval('setInfinity -poi cycle;')
	except:
            print 'Not Selected'
def Cycle_Off(*args):
	try:
		mel.eval('setInfinity -pri linear;')
		mel.eval('setInfinity -poi linear;')
	except:
            print 'Not Selected'
def mirror_x(*args):
        try:
            selected_curve_key = cmds.keyframe( query=True, selected=True)

            n_start = selected_curve_key[0]
            k_count = -1
            for o_key in selected_curve_key:
                k_count = k_count + 1
            n_end = selected_curve_key[k_count]

            cmds.scaleKey(scaleSpecifiedKeys=True,newStartTime=n_end,newStartFloat=n_end,newEndTime=n_start,newEndFloat=n_start )
            mel.eval('doBuffer snapshot')
            mel.eval('doBuffer swap')

        except:
            print 'Animation Key is Not Selected'

def mirror_y( dragControl, x, y, modifiers ):
    if modifiers == 0:
        try:
            mel.eval('doBuffer snapshot')
            mel.eval('doBuffer swap')
            cmds.scaleKey(scaleSpecifiedKeys=True,timeScale=1,timePivot=0,floatScale=1,floatPivot=0,valueScale=-1,valuePivot=0)
        except:
            print 'Animation Key is Not Selected'

def mirror_y2(*args):
    pass

def custom_graph_editor(*args):
    invis_panel = cmds.getPanel(invisiblePanels=True)

    graphpanels = cmds.getPanel(scriptType='graphEditor')
    graphpanels.remove('graphEditor1')

    for o_graphp in graphpanels:
        if o_graphp in invis_panel:
            cmds.deleteUI(o_graphp,panel=True)

    grp_panel_no_a = str( len(cmds.getPanel( scriptType='graphEditor' )) + 1 )

    if cmds.window('custom_graphEditor'+ grp_panel_no_a, exists=True):
        n_graphpanels = cmds.getPanel(scriptType='graphEditor')
        biggest_p = 1
        for o_panel in n_graphpanels:
            if int( o_panel[len('graphEditor'):]) > biggest_p:
                biggest_p = int( o_panel[len('graphEditor'):])
        grp_panel_no_a = str( biggest_p + 1 )

    try:
        win1 = cmds.window('custom_graphEditor'+ grp_panel_no_a, title='New CustomGraphEditor'+ grp_panel_no_a,resizeToFitChildren=True, widthHeight=(1100, 450))
    except:
        grp_panel_no_a = str( int(grp_panel_no_a) + 1 )
        win1 = cmds.window('custom_graphEditor'+ grp_panel_no_a, title='New CustomGraphEditor'+ grp_panel_no_a,resizeToFitChildren=True, widthHeight=(1100, 450))

    pane1 = cmds.paneLayout(configuration='horizontal2', paneSize=[2,1,1], parent=win1)
    graphmenu = 'graphEditor' + grp_panel_no_a
    cmds.scriptedPanel(graphmenu, label=graphmenu ,type='graphEditor', parent=pane1)
    cmds.setParent('..')

    current_minimum_frame = cmds.playbackOptions(query=True, minTime=True)
    current_maxmum_frame = cmds.playbackOptions(query=True, maxTime=True)

    outline_ed_name = "graphEditor" + grp_panel_no_a + 'OutlineEd'
    mel.eval('string $outlineed_name = "%s"' % outline_ed_name)

    graph_ed_name = "graphEditor" + grp_panel_no_a + 'GraphEd'
    mel.eval('string $o_graph_ed_name = "%s"' % graph_ed_name)
    mel.eval('animCurveEditor -edit -displayInfinities true $o_graph_ed_name;')

    mel.eval('filterUISelectAttributesCheckbox translateX 0 $outlineed_name;')
    mel.eval('filterUISelectAttributesCheckbox translateY 0 $outlineed_name;')
    mel.eval('filterUISelectAttributesCheckbox translateZ 0 $outlineed_name;')
    mel.eval('filterUISelectAttributesCheckbox rotateX 0 $outlineed_name;')
    mel.eval('filterUISelectAttributesCheckbox rotateY 0 $outlineed_name;')
    mel.eval('filterUISelectAttributesCheckbox rotateZ 0 $outlineed_name;')
    mel.eval('filterUISelectAttributesCheckbox scaleX 0 $outlineed_name;')
    mel.eval('filterUISelectAttributesCheckbox scaleY 0 $outlineed_name;')
    mel.eval('filterUISelectAttributesCheckbox scaleZ 0 $outlineed_name;')
    mel.eval('filterUISelectAttributesCheckbox visibility 0 $outlineed_name;')

    cmds.columnLayout( adjustableColumn=True )
    cmds.rowLayout(numberOfColumns=19,adjustableColumn=19)

    cmds.text('t')
    cmds.button('b_c_tx'+ grp_panel_no_a,label='X',bgc=[0.3,0.0,0.0],annotation='TranslateX',
        command=select_curve_tx,dragCallback=filter_tx,dropCallback=filter_tx2)
    cmds.button('b_c_ty'+ grp_panel_no_a,label='Y',bgc=[0.0,0.3,0.0],annotation='TranslateY',
        command=select_curve_ty,dragCallback=filter_ty,dropCallback=filter_ty2)
    cmds.button('b_c_tz'+ grp_panel_no_a,label='Z',bgc=[0.0,0.0,0.3],annotation='TranslateZ',
        command=select_curve_tz,dragCallback=filter_tz,dropCallback=filter_tz2)
    cmds.text('  r')
    cmds.button('b_c_rx'+ grp_panel_no_a,label='X',bgc=[0.3,0.0,0.0],annotation='RotateX',
        command=select_curve_rx,dragCallback=filter_rx,dropCallback=filter_rx2)
    cmds.button('b_c_ry'+ grp_panel_no_a,label='Y',bgc=[0.0,0.3,0.0],annotation='RotateY',
        command=select_curve_ry,dragCallback=filter_ry,dropCallback=filter_ry2)
    cmds.button('b_c_rz'+ grp_panel_no_a,label='Z',bgc=[0.0,0.0,0.3],annotation='RotateZ',
        command=select_curve_rz,dragCallback=filter_rz,dropCallback=filter_rz2)
    cmds.text('  s')
    cmds.button('b_c_sx'+ grp_panel_no_a,label='X',bgc=[0.3,0.0,0.0],annotation='ScaleX',
        command=select_curve_sx,dragCallback=filter_sx,dropCallback=filter_sx2)
    cmds.button('b_c_sy'+ grp_panel_no_a,label='Y',bgc=[0.0,0.3,0.0],annotation='ScaleY',
        command=select_curve_sy,dragCallback=filter_sy,dropCallback=filter_sy2)
    cmds.button('b_c_sz'+ grp_panel_no_a,label='Z',bgc=[0.0,0.0,0.3],annotation='ScaleZ',
        command=select_curve_sz,dragCallback=filter_sz,dropCallback=filter_sz2)
    cmds.text(' ')
    cmds.button('b_c_v'+ grp_panel_no_a,label='V',bgc=[0.3,0.3,0.3],annotation='Visibility',
        command=select_curve_v,dragCallback=filter_v,dropCallback=filter_v2)
    cmds.text('  ')

    cmds.symbolButton('time_prev'+ grp_panel_no_a,image='timeprev.xpm',
        command=o_prev_cmd,dragCallback=o_key_prev_cmd,dropCallback=o_key_prev_cmd2)
    cmds.symbolButton('time_next'+ grp_panel_no_a,image='timenext.xpm',
        command=o_next_cmd,dragCallback=o_key_next_cmd,dropCallback=o_key_next_cmd2)
    cmds.text('  ')

    cmds.timePort(enableBackground=True,bgc=[0.2,0.2,0.2],width=500,height=20 )


    cmds.setParent('..')
    cmds.rowLayout(numberOfColumns=16)

    cmds.text('  ')

    cmds.button('mirror'+ grp_panel_no_a,label='Mirror',
        command=mirror_x,dragCallback=mirror_y,dropCallback=mirror_y2)

    cmds.button('Cycle_ON'+ grp_panel_no_a,label='Cycle_ON',command=Cycle_On)

    cmds.button('Cycle_OFF'+ grp_panel_no_a,label='Cycle_OFF',command=Cycle_Off)

    cmds.text('  ')


    cmds.button('Retime'+ grp_panel_no_a,label='Retime',command= RetimeHelper)

    cmds.button('Out_l'+ grp_panel_no_a,label='Outliner',command="mel.eval('OutlinerWindow;')" )

    cmds.optionMenu( label='Speed', changeCommand=SetSpeed )
    cmds.menuItem( label='realtime' )
    cmds.menuItem( label='2x' )
    cmds.menuItem( label='1/2x' )

    cmds.text('  ')

    cmds.symbolButton('time_rew'+ grp_panel_no_a,image='timerew.xpm',command="mel.eval('playButtonStart;')" )

    cmds.symbolButton('step_backward'+ grp_panel_no_a,image='timeend.xpm',command=lambda x:step_backward(grp_panel_no_a))

    cmds.symbolButton('play_forward'+ grp_panel_no_a,image='timeplay.xpm',command=lambda x:play_forward(grp_panel_no_a))

    cmds.symbolButton('step_forward'+ grp_panel_no_a,image='timestart.xpm',command=lambda x:step_forward(grp_panel_no_a))

    cmds.symbolButton('time_fwd'+ grp_panel_no_a,image='timefwd.xpm',command="mel.eval('playButtonEnd;')" )


    cmds.showWindow()



