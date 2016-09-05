# -*- coding: utf-8 -*-
import maya.cmds as cmds
import maya.mel as mel	

def SelPoly_Hide():
	#�I�������X�g�Ɋi�[
	oSel = cmds.ls(sl=True)
	#�t���O����
	Check = 0
	#�I������Ă��Ȃ�������
	if oSel == []:
		return
	#�L�[�{�[�h�X�e�[�g���`�F�b�N
	mods = cmds.getModifiers()
	#�R���g���[�������Ă�����A�֐��ɔ��ŏI��
	if (mods & 4) > 0:
		if oSel[0] == "Poly_Hide_Set":
			Toggle(oSel)
			Clean()
			return
	#�I�����Z�b�g�Ŋ��A�R���g���[�������Ă��Ȃ�������B
	if oSel[0] == "Poly_Hide_Set":
		Toggle(oSel)
		return
	#�t�F�[�X��I��
	oSelFace = cmds.filterExpand(sm=34)
	#�t�F�[�X����Ȃ�������
	if oSelFace == None:
		return
	#�t�F�[�X����I�u�W�F�N�g���擾
	const =  oSelFace[0].rpartition(".")
	#�q�X�g���[���擾
	oList = cmds.listHistory(const[0])
	for i in oList:
		#���J����q�X�g���[����������A�t���O�𗧂Ă�
		if i == "Hide_Poly":
			Check = 1  
	#�t���O�������Ă�����
	if Check == 1:
		cmds.polyHole(assignHole=0)
	#�Ȃ�������
	else:
		mel.eval('ToggleHoleFaces;')
		FaceSet = cmds.sets(n="Poly_Hide_Set")
		cmds.polyHole(assignHole=1)
		cmds.rename("polyHoleFace1","Hide_Poly")
	
#�P���ɕ\����؂�ւ��Ă��邾��
def Toggle(oSel):
	cmds.select(hierarchy=True)
	mel.eval('ToggleHoleFaces;')
	cmds.select(cl=True)

#�q�X�g���ƃZ�b�g���폜
def Clean():
	cmds.delete("Hide_Poly")
	cmds.delete("Poly_Hide_Set")



SelPoly_Hide()