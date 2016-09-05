import maya.cmds as cmds
cons = cmds.ls(selection=True)
sel = []
 
 
for con in cons:
    target = cmds.listConnections(con, p=False,t="constraint") 
    str_obj = target[0]
    const =  str_obj.rpartition("_")
    sel.append(const[0])
cmds.select(sel)