import maya.cmds as cmds

def showWindow():
    name = "Quadruped Auto-rigger"
    if cmds.window(name, query = True, exists = True):
        cmds.deleteUI(name)
    
    cmds.window(name)
    cmds.showWindow()

''' Place locators to define rig shape '''
def SetColorOverrideBlue(s):
    cmds.setAttr(s + '.overrideEnabled', 1)
    cmds.setAttr(s + '.overrideColor', 15)

def SetColorOverrideYellow(s):
    cmds.setAttr(s + '.overrideEnabled', 1)
    cmds.setAttr(s + '.overrideColor', 17)

def SetColorOverrideRed(s):
    cmds.setAttr(s + '.overrideEnabled', 1)
    cmds.setAttr(s + '.overrideColor', 13)
    
def lockTranslate(s):
    cmds.setAttr(s + '.tx', k = False, l = True)
    cmds.setAttr(s + '.ty', k = False, l = True)
    cmds.setAttr(s + '.tz', k = False, l = True)

def lockScale(s):
    cmds.setAttr(s + '.sx', k = False, l = True)
    cmds.setAttr(s + '.sy', k = False, l = True)
    cmds.setAttr(s + '.sz', k = False, l = True)

def lockRotate(s):
    cmds.setAttr(s + '.rx', k = False, l = True)
    cmds.setAttr(s + '.ry', k = False, l = True)
    cmds.setAttr(s + '.rz', k = False, l = True)

hindToe = cmds.spaceLocator(n='L_hindToe_LOC')
cmds.setAttr(hindToe[0]+'.translateX', 12)
cmds.setAttr(hindToe[0]+'.translateZ', -20)
SetColorOverrideBlue(hindToe[0])

hindAnkle = cmds.spaceLocator(n='L_hindAnkle_LOC')
cmds.setAttr(hindAnkle[0]+'.translateX', 12)
cmds.setAttr(hindAnkle[0]+'.translateY', 5)
cmds.setAttr(hindAnkle[0]+'.translateZ', -23)
SetColorOverrideBlue(hindAnkle[0])

hindKnee = cmds.spaceLocator(n='L_hindKnee_LOC')
cmds.setAttr(hindKnee[0]+'.translateX', 12)
cmds.setAttr(hindKnee[0]+'.translateY', 25)
cmds.setAttr(hindKnee[0]+'.translateZ', -28)
SetColorOverrideBlue(hindKnee[0])

hindUpperKnee = cmds.spaceLocator(n='L_hindUpperKnee_LOC')
cmds.setAttr(hindUpperKnee[0]+'.translateX', 12)
cmds.setAttr(hindUpperKnee[0]+'.translateY', 36)
cmds.setAttr(hindUpperKnee[0]+'.translateZ', -19)
SetColorOverrideBlue(hindUpperKnee[0])

hindFemur = cmds.spaceLocator(n='L_hindFemur_LOC')
cmds.setAttr(hindFemur[0]+'.translateX', 12)
cmds.setAttr(hindFemur[0]+'.translateY', 50)
cmds.setAttr(hindFemur[0]+'.translateZ', -25)
SetColorOverrideBlue(hindFemur[0])

hindPelvis = cmds.spaceLocator(n='L_hindPelvis_LOC')
cmds.setAttr(hindPelvis[0]+'.translateY', 54)
cmds.setAttr(hindPelvis[0]+'.translateZ', -24)
SetColorOverrideYellow(hindPelvis[0])

hindLocGrp = cmds.group(hindToe,hindAnkle, hindKnee, hindUpperKnee, hindFemur, hindPelvis, n='HindPlacement_GRP')

''' Front leg locator placement '''
frontToe = cmds.spaceLocator(n='L_frontToe_LOC')
cmds.setAttr(frontToe[0]+'.translateX', 12)
cmds.setAttr(frontToe[0]+'.translateZ', 24)
SetColorOverrideBlue(frontToe[0])

frontAnkle = cmds.spaceLocator(n='L_frontAnkle_LOC')
cmds.setAttr(frontAnkle[0]+'.translateX', 12)
cmds.setAttr(frontAnkle[0]+'.translateY', 5)
cmds.setAttr(frontAnkle[0]+'.translateZ', 21)
SetColorOverrideBlue(frontAnkle[0])

frontKnee = cmds.spaceLocator(n='L_frontKnee_LOC')
cmds.setAttr(frontKnee[0]+'.translateX', 12)
cmds.setAttr(frontKnee[0]+'.translateY', 25)
cmds.setAttr(frontKnee[0]+'.translateZ', 24)
SetColorOverrideBlue(frontKnee[0])

frontUpperKnee = cmds.spaceLocator(n='L_frontUpperKnee_LOC')
cmds.setAttr(frontUpperKnee[0]+'.translateX', 12)
cmds.setAttr(frontUpperKnee[0]+'.translateY', 36)
cmds.setAttr(frontUpperKnee[0]+'.translateZ', 18)
SetColorOverrideBlue(frontUpperKnee[0])

frontFemur = cmds.spaceLocator(n='L_frontFemur_LOC')
cmds.setAttr(frontFemur[0]+'.translateX', 12)
cmds.setAttr(frontFemur[0]+'.translateY', 44)
cmds.setAttr(frontFemur[0]+'.translateZ', 25)
SetColorOverrideBlue(frontFemur[0])

frontPelvis = cmds.spaceLocator(n='L_frontPelvis_LOC')
cmds.setAttr(frontPelvis[0]+'.translateY', 54)
cmds.setAttr(frontPelvis[0]+'.translateZ', 20)
SetColorOverrideYellow(frontPelvis[0])

frontLocGrp = cmds.group(frontToe, frontAnkle, frontKnee, frontUpperKnee, frontFemur, frontPelvis, n='FrontPlacement_GRP')

''' Neck locators '''
neckRoot = cmds.spaceLocator(n='NeckRoot_LOC')
cmds.setAttr(neckRoot[0]+'.translateY', 48)
cmds.setAttr(neckRoot[0]+'.translateZ', 30)
SetColorOverrideYellow(neckRoot[0])

neckEnd = cmds.spaceLocator(n='neckEnd_LOC')
cmds.setAttr(neckEnd[0]+'.translateY', 58)
cmds.setAttr(neckEnd[0]+'.translateZ', 50)
SetColorOverrideYellow(neckEnd[0])

neckLocGrp = cmds.group(neckRoot, neckEnd, n='NeckPlacement_GRP')

''' Tail locators '''
tailRootLoc = cmds.spaceLocator(n='TailRoot_LOC')
cmds.setAttr(tailRootLoc[0]+'.translateY', 54)
cmds.setAttr(tailRootLoc[0]+'.translateZ', -32)
SetColorOverrideYellow(tailRootLoc[0])

tailEndLoc = cmds.spaceLocator(n='TailEnd_LOC')
cmds.setAttr(tailEndLoc[0]+'.translateY', 54)
cmds.setAttr(tailEndLoc[0]+'.translateZ', -62)
SetColorOverrideYellow(tailEndLoc[0])

tailLocGrp = cmds.group(tailRootLoc, tailEndLoc, n='TailPlacement_GRP')

''' Finalize placement locator module '''
mainLocGrp = cmds.group(tailLocGrp, neckLocGrp, frontLocGrp, hindLocGrp, n='MainPlacementLoC_GRP')

''' World Controller. TODO: Replace with Custom Curves'''
worldCtrl = cmds.circle(nr = [0,1,0], n = 'World Controller')[0]
subworldCtrl = cmds.circle(nr = [0,1,0],n = 'Sub World Controller')
subworldCtrl = subworldCtrl[0]
cmds.scale(0.7, 0.7, 0.7, subworldCtrl + '.cv[0:16]')
cmds.parent(subworldCtrl, worldCtrl)
cmds.select(d = True)
SetColorOverrideYellow(worldCtrl)

# cont up: worldController
# Hind legs Joints
''' Create legs module '''
hindPelvisJnt = cmds.joint(n = 'C_HindPelvis_JNT')
SetColorOverrideYellow(hindPelvisJnt)
constraintaint = cmds.pointConstraint(hindPelvis, hindPelvisJnt)
cmds.delete(constraintaint)
cmds.select(d = True)

L_hindToeJnt = cmds.joint(n = 'L_HindToe_JNT')
SetColorOverrideYellow(L_hindToeJnt)
constraintaint = cmds.pointConstraint(hindToe, L_hindToeJnt)
cmds.delete(constraintaint)
cmds.select(d = True)

L_hindAnkleJnt = cmds.joint(n = 'L_HindAnkle_JNT')
SetColorOverrideYellow(L_hindAnkleJnt)
constraintaint = cmds.pointConstraint(hindAnkle, L_hindAnkleJnt)
cmds.delete(constraintaint)
cmds.select(d = True)

L_hindKneeJnt = cmds.joint(n = 'L_HindKnee_JNT')
SetColorOverrideYellow(L_hindKneeJnt)
constraintaint = cmds.pointConstraint(hindKnee, L_hindKneeJnt)
cmds.delete(constraintaint)
cmds.select(d = True)

L_hindUpperKneeJnt = cmds.joint(n = 'L_HindUpperKnee_JNT')
SetColorOverrideYellow(L_hindUpperKneeJnt) 
constraintaint = cmds.pointConstraint(hindUpperKnee, L_hindUpperKneeJnt)
cmds.delete(constraintaint)
cmds.select(d = True)

L_hindFemurJnt = cmds.joint(n = 'L_HindFemur_JNT') 
SetColorOverrideYellow(L_hindFemurJnt)
constraintaint = cmds.pointConstraint(hindFemur, L_hindFemurJnt)
cmds.delete(constraintaint)
cmds.select(d = True)

# Mirror joints to L & R sides
R_hindToeJnt = cmds.duplicate(L_hindToeJnt, n = 'R_HindToe_JNT')[0]
xPos = cmds.getAttr(L_hindToeJnt + '.tx')
cmds.setAttr(R_hindToeJnt + '.tx', -xPos)

R_hindAnkleJnt = cmds.duplicate(L_hindAnkleJnt, n = 'R_HindAnkle_JNT')[0]
xPos = cmds.getAttr(L_hindAnkleJnt + '.tx')
cmds.setAttr(R_hindAnkleJnt + '.tx', -xPos)

R_hindKneeJnt = cmds.duplicate(L_hindKneeJnt, n = 'R_HindKnee_JNT')[0]
xPos = cmds.getAttr(L_hindKneeJnt + '.tx')
cmds.setAttr(R_hindKneeJnt + '.tx', -xPos)

R_hindUpperKneeJnt = cmds.duplicate(L_hindUpperKneeJnt, n = 'R_HindUpperKnee_JNT')[0]
xPos = cmds.getAttr(L_hindUpperKneeJnt + '.tx')
cmds.setAttr(R_hindUpperKneeJnt + '.tx', -xPos)

R_hindFemurJnt = cmds.duplicate(L_hindFemurJnt, n = 'R_HindFemur_JNT')[0]
xPos = cmds.getAttr(L_hindFemurJnt + '.tx')
cmds.setAttr(R_hindFemurJnt + '.tx', -xPos)

# End joints for Maya skinning
L_hindToeEndJnt = cmds.joint(n = 'L_HindToeEnd_JNT')
constraintaint = cmds.pointConstraint(hindToe, L_hindToeEndJnt)
cmds.delete(constraintaint)
cmds.parent(L_hindToeEndJnt, L_hindToeJnt)
cmds.setAttr(L_hindToeEndJnt + '.tz', 0.04)
cmds.setAttr(L_hindToeEndJnt + '.visibility', 0)
cmds.select(d = True)

R_hindToeEndJnt = cmds.joint(n = 'R_HindToeEnd_JNT')
cmds.parent(R_hindToeEndJnt, R_hindToeJnt, r=True)
cmds.setAttr(R_hindToeEndJnt + '.tz', 0.04)
cmds.setAttr(R_hindToeEndJnt + '.visibility', 0)
cmds.select(d = True)

# Parent hind leg joints, set up both L & R joint chains
cmds.parent(L_hindToeJnt, L_hindAnkleJnt)
cmds.parent(L_hindAnkleJnt, L_hindKneeJnt)
cmds.parent(L_hindKneeJnt, L_hindUpperKneeJnt)
cmds.parent(L_hindUpperKneeJnt, L_hindFemurJnt)
cmds.parent(L_hindFemurJnt, hindPelvisJnt)

cmds.parent(R_hindToeJnt, R_hindAnkleJnt)
cmds.parent(R_hindAnkleJnt, R_hindKneeJnt)
cmds.parent(R_hindKneeJnt, R_hindUpperKneeJnt)
cmds.parent(R_hindUpperKneeJnt, R_hindFemurJnt)
cmds.parent(R_hindFemurJnt, hindPelvisJnt)

# Orient joints
cmds.select(L_hindFemurJnt)
cmds.joint(e = True, zso = True, oj = 'xyz', secondaryAxisOrient = 'yup', ch = True)
cmds.select(R_hindFemurJnt)
cmds.joint(e = True, zso = True, oj = 'xyz', secondaryAxisOrient = 'yup', ch = True)
cmds.select(d = True)

''' IK Hind Legs '''
L_hindToeJntIK = cmds.joint(n='L_HindToeIK_JNT')
constraintaint = cmds.pointConstraint(hindToe, L_hindToeJntIK)
cmds.delete(constraintaint)
cmds.select(d = True)

L_hindAnkleJntIK = cmds.joint(n = 'L_HindAnkleIK_JNT')
constraintaint = cmds.pointConstraint(hindAnkle, L_hindAnkleJntIK)
cmds.delete(constraintaint)
cmds.select(d = True)

L_hindKneeJntIK = cmds.joint(n = 'L_HindKneeIK_JNT')
constraintaint = cmds.pointConstraint(hindKnee, L_hindKneeJntIK)
cmds.delete(constraintaint)
cmds.select(d = True)

L_hindUpperKneeJntIK = cmds.joint(n = 'L_HindUpperKneeIK_JNT')
constraintaint = cmds.pointConstraint(hindUpperKnee, L_hindUpperKneeJntIK)
cmds.delete(constraintaint)
cmds.select(d = True)

L_hindFemurJntIK = cmds.joint(n = 'L_HindFemurIK_JNT') 
constraintaint = cmds.pointConstraint(hindFemur, L_hindFemurJntIK)
cmds.delete(constraintaint)
cmds.select(d = True)

# Mirror IK joints to L & R sides
R_hindToeJntIK = cmds.duplicate(L_hindToeJntIK, n = 'R_HindToeIK_JNT')[0]
xPos = cmds.getAttr(L_hindToeJntIK + '.tx')
cmds.setAttr(R_hindToeJntIK + '.tx', -xPos)

R_hindAnkleJntIK = cmds.duplicate(L_hindAnkleJntIK, n = 'R_HindAnkleIK_JNT')[0]
xPos = cmds.getAttr(L_hindAnkleJntIK + '.tx')
cmds.setAttr(R_hindAnkleJntIK + '.tx', -xPos)

R_hindKneeJntIK = cmds.duplicate(L_hindKneeJntIK, n = 'R_HindKneeIK_JNT')[0]
xPos = cmds.getAttr(L_hindKneeJntIK + '.tx')
cmds.setAttr(R_hindKneeJntIK + '.tx', -xPos)

R_hindUpperKneeJntIK = cmds.duplicate(L_hindUpperKneeJntIK, n = 'R_HindUpperKneeIK_JNT')[0]
xPos = cmds.getAttr(L_hindUpperKneeJntIK + '.tx')
cmds.setAttr(R_hindUpperKneeJntIK + '.tx', -xPos)

R_hindFemurJntIK = cmds.duplicate(L_hindFemurJntIK, n = 'R_HindFemurIK_JNT')[0]
xPos = cmds.getAttr(L_hindFemurJntIK + '.tx')
cmds.setAttr(R_hindFemurJntIK + '.tx', -xPos)

# Parent hind leg IK joints, set up both L & R IK joint chains
cmds.parent(L_hindToeJntIK, L_hindAnkleJntIK)
cmds.parent(L_hindAnkleJntIK, L_hindKneeJntIK)
cmds.parent(L_hindKneeJntIK, L_hindUpperKneeJntIK)
cmds.parent(L_hindUpperKneeJntIK, L_hindFemurJntIK)
cmds.parent(L_hindFemurJntIK, hindPelvisJnt)

cmds.parent(R_hindToeJntIK, R_hindAnkleJntIK)
cmds.parent(R_hindAnkleJntIK, R_hindKneeJntIK)
cmds.parent(R_hindKneeJntIK, R_hindUpperKneeJntIK)
cmds.parent(R_hindUpperKneeJntIK, R_hindFemurJntIK)
cmds.parent(R_hindFemurJntIK, hindPelvisJnt)

# Orient IK joints chain correctly
cmds.select(L_hindFemurJntIK)
cmds.joint(e = True, zso = True, oj = 'xyz', secondaryAxisOrient = 'yup', ch = True)
cmds.select(R_hindFemurJntIK)
cmds.joint(e = True, zso = True, oj = 'xyz', secondaryAxisOrient = 'yup', ch = True)
cmds.select(d = True)

''' FK Hind Legs '''
L_hindToeJntFK = cmds.joint(n='L_HindToeFK_JNT')
constraintaint = cmds.pointConstraint(hindToe, L_hindToeJntFK)
cmds.delete(constraintaint)
cmds.select(d = True)

L_hindAnkleJntFK = cmds.joint(n = 'L_HindAnkleFK_JNT')
constraintaint = cmds.pointConstraint(hindAnkle, L_hindAnkleJntFK)
cmds.delete(constraintaint)
cmds.select(d = True)

L_hindKneeJntFK = cmds.joint(n = 'L_HindKneeFK_JNT')
constraintaint = cmds.pointConstraint(hindKnee, L_hindKneeJntFK)
cmds.delete(constraintaint)
cmds.select(d = True)

L_hindUpperKneeJntFK = cmds.joint(n = 'L_HindUpperKneeFK_JNT')
constraintaint = cmds.pointConstraint(hindUpperKnee, L_hindUpperKneeJntFK)
cmds.delete(constraintaint)
cmds.select(d = True)

L_hindFemurJntFK = cmds.joint(n = 'L_HindFemurFK_JNT') 
constraintaint = cmds.pointConstraint(hindFemur, L_hindFemurJntFK)
cmds.delete(constraintaint)
cmds.select(d = True)

# Mirror FK joints to L & R sides
R_hindToeJntFK = cmds.duplicate(L_hindToeJntFK, n = 'R_HindToeFK_JNT')[0]
xPos = cmds.getAttr(L_hindToeJntFK + '.tx')
cmds.setAttr(R_hindToeJntFK + '.tx', -xPos)

R_hindAnkleJntFK = cmds.duplicate(L_hindAnkleJntFK, n = 'R_HindAnkleFK_JNT')[0]
xPos = cmds.getAttr(L_hindAnkleJntFK + '.tx')
cmds.setAttr(R_hindAnkleJntFK + '.tx', -xPos)

R_hindKneeJntFK = cmds.duplicate(L_hindKneeJntFK, n = 'R_HindKneeFK_JNT')[0]
xPos = cmds.getAttr(L_hindKneeJntFK + '.tx')
cmds.setAttr(R_hindKneeJntFK + '.tx', -xPos)

R_hindUpperKneeJntFK = cmds.duplicate(L_hindUpperKneeJntFK, n = 'R_HindUpperKneeFK_JNT')[0]
xPos = cmds.getAttr(L_hindUpperKneeJntFK + '.tx')
cmds.setAttr(R_hindUpperKneeJntFK + '.tx', -xPos)

R_hindFemurJntFK = cmds.duplicate(L_hindFemurJntFK, n = 'R_HindFemurFK_JNT')[0]
xPos = cmds.getAttr(L_hindFemurJntFK + '.tx')
cmds.setAttr(R_hindFemurJntFK + '.tx', -xPos)

# Parent hind leg FK joints, set up both L & R FK joint chains
cmds.parent(L_hindToeJntFK, L_hindAnkleJntFK)
cmds.parent(L_hindAnkleJntFK, L_hindKneeJntFK)
cmds.parent(L_hindKneeJntFK, L_hindUpperKneeJntFK)
cmds.parent(L_hindUpperKneeJntFK, L_hindFemurJntFK)
cmds.parent(L_hindFemurJntFK, hindPelvisJnt)

cmds.parent(R_hindToeJntFK, R_hindAnkleJntFK)
cmds.parent(R_hindAnkleJntFK, R_hindKneeJntFK)
cmds.parent(R_hindKneeJntFK, R_hindUpperKneeJntFK)
cmds.parent(R_hindUpperKneeJntFK, R_hindFemurJntFK)
cmds.parent(R_hindFemurJntFK, hindPelvisJnt)

# Orient FK joints chain correctly
cmds.select(L_hindFemurJntFK)
cmds.joint(e = True, zso = True, oj = 'xyz', secondaryAxisOrient = 'yup', ch = True)
cmds.select(R_hindFemurJntFK)
cmds.joint(e = True, zso = True, oj = 'xyz', secondaryAxisOrient = 'yup', ch = True)
cmds.select(d = True)

# Front Leg Joints
''' Create legs module '''
frontPelvisJnt = cmds.joint(n = 'C_FrontPelvis_JNT')
SetColorOverrideYellow(frontPelvisJnt)
constraintaint = cmds.pointConstraint(frontPelvis, frontPelvisJnt)
cmds.delete(constraintaint)
cmds.select(d = True)

L_frontToeJnt = cmds.joint(n = 'L_FrontToe_JNT')
SetColorOverrideYellow(L_frontToeJnt)
constraintaint = cmds.pointConstraint(frontToe, L_frontToeJnt)
cmds.delete(constraintaint)
cmds.select(d = True)

L_frontAnkleJnt = cmds.joint(n = 'L_FrontAnkle_JNT')
SetColorOverrideYellow(L_frontAnkleJnt)
constraintaint = cmds.pointConstraint(frontAnkle, L_frontAnkleJnt)
cmds.delete(constraintaint)
cmds.select(d = True)

L_frontKneeJnt = cmds.joint(n = 'L_FrontKnee_JNT')
constraintaint = cmds.pointConstraint(frontKnee, L_frontKneeJnt)
cmds.delete(constraintaint)
cmds.select(d = True)
SetColorOverrideYellow(L_frontKneeJnt)

L_frontUpperKneeJnt = cmds.joint(n = 'L_FrontUpperKnee_JNT')
SetColorOverrideYellow(L_frontUpperKneeJnt) 
constraintaint = cmds.pointConstraint(frontUpperKnee, L_frontUpperKneeJnt)
cmds.delete(constraintaint)
cmds.select(d = True)

L_frontFemurJnt = cmds.joint(n = 'L_FrontFemur_JNT') 
SetColorOverrideYellow(L_frontFemurJnt)
constraintaint = cmds.pointConstraint(frontFemur, L_frontFemurJnt)
cmds.delete(constraintaint)
cmds.select(d = True)

# Mirror joints to L & R sides
R_frontToeJnt = cmds.duplicate(L_frontToeJnt, n = 'R_FrontToe_JNT')[0]
xPos = cmds.getAttr(L_frontToeJnt + '.tx')
cmds.setAttr(R_frontToeJnt + '.tx', -xPos)

R_frontAnkleJnt = cmds.duplicate(L_frontAnkleJnt, n = 'R_FrontAnkle_JNT')[0]
xPos = cmds.getAttr(L_frontAnkleJnt + '.tx')
cmds.setAttr(R_frontAnkleJnt + '.tx', -xPos)

R_frontKneeJnt = cmds.duplicate(L_frontKneeJnt, n = 'R_FrontKnee_JNT')[0]
xPos = cmds.getAttr(L_frontKneeJnt + '.tx')
cmds.setAttr(R_frontKneeJnt + '.tx', -xPos)

R_frontUpperKneeJnt = cmds.duplicate(L_frontUpperKneeJnt, n = 'R_FrontUpperKnee_JNT')[0]
xPos = cmds.getAttr(L_frontUpperKneeJnt + '.tx')
cmds.setAttr(R_frontUpperKneeJnt + '.tx', -xPos)

R_frontFemurJnt = cmds.duplicate(L_frontFemurJnt, n = 'R_FrontFemur_JNT')[0]
xPos = cmds.getAttr(L_frontFemurJnt + '.tx')
cmds.setAttr(R_frontFemurJnt + '.tx', -xPos)

# End joints for Maya skinning
L_frontToeEndJnt = cmds.joint(n = 'L_FrontToeEnd_JNT')
constraintaint = cmds.pointConstraint(frontToe, L_frontToeEndJnt)
cmds.delete(constraintaint)
cmds.parent(L_frontToeEndJnt, L_frontToeJnt)
cmds.setAttr(L_frontToeEndJnt + '.tz', 0.04)
cmds.setAttr(L_frontToeEndJnt + '.visibility', 0)
cmds.select(d = True)

R_frontToeEndJnt = cmds.joint(n = 'R_FrontToeEnd_JNT')
cmds.parent(R_frontToeEndJnt, R_frontToeJnt, r=True)
cmds.setAttr(R_frontToeEndJnt + '.tz', 0.04)
cmds.setAttr(R_frontToeEndJnt + '.visibility', 0)
cmds.select(d = True)

# Parent front leg joints, set up both L & R joint chains
cmds.parent(L_frontToeJnt, L_frontAnkleJnt)
cmds.parent(L_frontAnkleJnt, L_frontKneeJnt)
cmds.parent(L_frontKneeJnt, L_frontUpperKneeJnt)
cmds.parent(L_frontUpperKneeJnt, L_frontFemurJnt)
cmds.parent(L_frontFemurJnt, frontPelvisJnt)
cmds.parent(R_frontToeJnt, R_frontAnkleJnt)
cmds.parent(R_frontAnkleJnt, R_frontKneeJnt)
cmds.parent(R_frontKneeJnt, R_frontUpperKneeJnt)
cmds.parent(R_frontUpperKneeJnt, R_frontFemurJnt)
cmds.parent(R_frontFemurJnt, frontPelvisJnt)
# TODO: cmds.parent(frontPelvisJnt, subworldCtrl)

# Orient joints
cmds.select(L_frontFemurJnt)
cmds.joint(e=True,zso=True, oj='xyz',secondaryAxisOrient='yup',ch=True)
cmds.select(R_frontFemurJnt)
cmds.joint(e=True,zso=True, oj='xyz',secondaryAxisOrient='yup',ch=True)
cmds.select(d=True)

''' IK Front Legs '''
L_frontToeJntIK = cmds.joint(n='L_FrontToeIK_JNT')
constraintaint = cmds.pointConstraint(frontToe, L_frontToeJntIK)
cmds.delete(constraintaint)
cmds.select(d = True)

L_frontAnkleJntIK = cmds.joint(n = 'L_FrontAnkleIK_JNT')
constraintaint = cmds.pointConstraint(frontAnkle, L_frontAnkleJntIK)
cmds.delete(constraintaint)
cmds.select(d = True)

L_frontKneeJntIK = cmds.joint(n = 'L_FrontKneeIK_JNT')
constraintaint = cmds.pointConstraint(frontKnee, L_frontKneeJntIK)
cmds.delete(constraintaint)
cmds.select(d = True)

L_frontUpperKneeJntIK = cmds.joint(n = 'L_FrontUpperKneeIK_JNT')
constraintaint = cmds.pointConstraint(frontUpperKnee, L_frontUpperKneeJntIK)
cmds.delete(constraintaint)
cmds.select(d = True)

L_frontFemurJntIK = cmds.joint(n = 'L_FrontFemurIK_JNT') 
constraintaint = cmds.pointConstraint(frontFemur, L_frontFemurJntIK)
cmds.delete(constraintaint)
cmds.select(d = True)

# Mirror IK joints to L & R sides
R_frontToeJntIK = cmds.duplicate(L_frontToeJntIK, n = 'R_FrontToeIK_JNT')[0]
xPos = cmds.getAttr(R_frontToeJntIK + '.tx')
cmds.setAttr(R_frontToeJntIK + '.tx', -xPos)

R_frontAnkleJntIK = cmds.duplicate(L_frontAnkleJntIK, n = 'R_FrontAnkleIK_JNT')[0]
xPos = cmds.getAttr(R_frontAnkleJntIK + '.tx')
cmds.setAttr(R_frontAnkleJntIK + '.tx', -xPos)

R_frontKneeJntIK = cmds.duplicate(L_frontKneeJntIK, n = 'R_FrontKneeIK_JNT')[0]
xPos = cmds.getAttr(R_frontKneeJntIK + '.tx')
cmds.setAttr(R_frontKneeJntIK + '.tx', -xPos)

R_frontUpperKneeJntIK = cmds.duplicate(L_frontUpperKneeJntIK, n = 'R_FrontUpperKneeIK_JNT')[0]
xPos = cmds.getAttr(R_frontUpperKneeJntIK + '.tx')
cmds.setAttr(R_frontUpperKneeJntIK + '.tx', -xPos)

R_frontFemurJntIK = cmds.duplicate(L_frontFemurJntIK, n = 'R_FrontFemurIK_JNT')[0]
xPos = cmds.getAttr(R_frontFemurJntIK + '.tx')
cmds.setAttr(R_frontFemurJntIK + '.tx', -xPos)

# Parent front leg IK joints, set up both L & R IK joint chains
cmds.parent(L_frontToeJntIK, L_frontAnkleJntIK)
cmds.parent(L_frontAnkleJntIK, L_frontKneeJntIK)
cmds.parent(L_frontKneeJntIK, L_frontUpperKneeJntIK)
cmds.parent(L_frontUpperKneeJntIK, L_frontFemurJntIK)
cmds.parent(L_frontFemurJntIK, frontPelvisJnt)

cmds.parent(R_frontToeJntIK, R_frontAnkleJntIK)
cmds.parent(R_frontAnkleJntIK, R_frontKneeJntIK)
cmds.parent(R_frontKneeJntIK, R_frontUpperKneeJntIK)
cmds.parent(R_frontUpperKneeJntIK, R_frontFemurJntIK)
cmds.parent(R_frontFemurJntIK, frontPelvisJnt)

# Orient IK joints chain correctly
cmds.select(L_frontFemurJntIK)
cmds.joint(e = True, zso = True, oj = 'xyz', secondaryAxisOrient = 'yup', ch = True)
cmds.select(R_frontFemurJntIK)
cmds.joint(e = True, zso = True, oj = 'xyz', secondaryAxisOrient = 'yup', ch = True)
cmds.select(d = True)

''' FK Front Legs '''
L_frontToeJntFK = cmds.joint(n='L_FrontToeFK_JNT')
constraintaint = cmds.pointConstraint(frontToe, L_frontToeJntFK)
cmds.delete(constraintaint)
cmds.select(d = True)

L_frontAnkleJntFK = cmds.joint(n = 'L_FrontAnkleFK_JNT')
constraintaint = cmds.pointConstraint(frontAnkle, L_frontAnkleJntFK)
cmds.delete(constraintaint)
cmds.select(d = True)

L_frontKneeJntFK = cmds.joint(n = 'L_FrontKneeFK_JNT')
constraintaint = cmds.pointConstraint(frontKnee, L_frontKneeJntFK)
cmds.delete(constraintaint)
cmds.select(d = True)

L_frontUpperKneeJntFK = cmds.joint(n = 'L_FrontUpperKneeFK_JNT')
constraintaint = cmds.pointConstraint(frontUpperKnee, L_frontUpperKneeJntFK)
cmds.delete(constraintaint)
cmds.select(d = True)

L_frontFemurJntFK = cmds.joint(n = 'L_FrontFemurFK_JNT') 
constraintaint = cmds.pointConstraint(frontFemur, L_frontFemurJntFK)
cmds.delete(constraintaint)
cmds.select(d = True)

# Mirror FK joints to L & R sides
R_frontToeJntFK = cmds.duplicate(L_frontToeJntFK, n = 'R_FrontToeFK_JNT')[0]
xPos = cmds.getAttr(L_frontToeJntFK + '.tx')
cmds.setAttr(R_frontToeJntFK + '.tx', -xPos)

R_frontAnkleJntFK = cmds.duplicate(L_frontAnkleJntFK, n = 'R_FrontAnkleFK_JNT')[0]
xPos = cmds.getAttr(L_frontAnkleJntFK + '.tx')
cmds.setAttr(R_frontAnkleJntFK + '.tx', -xPos)

R_frontKneeJntFK = cmds.duplicate(L_frontKneeJntFK, n = 'R_FrontKneeFK_JNT')[0]
xPos = cmds.getAttr(L_frontKneeJntFK + '.tx')
cmds.setAttr(R_frontKneeJntFK + '.tx', -xPos)

R_frontUpperKneeJntFK = cmds.duplicate(L_frontUpperKneeJntFK, n = 'R_FrontUpperKneeFK_JNT')[0]
xPos = cmds.getAttr(L_frontUpperKneeJntFK + '.tx')
cmds.setAttr(R_frontUpperKneeJntFK + '.tx', -xPos)

R_frontFemurJntFK = cmds.duplicate(L_frontFemurJntFK, n = 'R_FrontFemurFK_JNT')[0]
xPos = cmds.getAttr(L_frontFemurJntFK + '.tx')
cmds.setAttr(R_frontFemurJntFK + '.tx', -xPos)

# Parent front leg FK joints, set up both L & R FK joint chains
cmds.parent(L_frontToeJntFK, L_frontAnkleJntFK)
cmds.parent(L_frontAnkleJntFK, L_frontKneeJntFK)
cmds.parent(L_frontKneeJntFK, L_frontUpperKneeJntFK)
cmds.parent(L_frontUpperKneeJntFK, L_frontFemurJntFK)
cmds.parent(L_frontFemurJntFK, frontPelvisJnt)

cmds.parent(R_frontToeJntFK, R_frontAnkleJntFK)
cmds.parent(R_frontAnkleJntFK, R_frontKneeJntFK)
cmds.parent(R_frontKneeJntFK, R_frontUpperKneeJntFK)
cmds.parent(R_frontUpperKneeJntFK, R_frontFemurJntFK)
cmds.parent(R_frontFemurJntFK, frontPelvisJnt)

# Orient FK joints chain correctly
cmds.select(L_frontFemurJntFK)
cmds.joint(e = True, zso = True, oj = 'xyz', secondaryAxisOrient = 'yup', ch = True)
cmds.select(R_frontFemurJntFK)
cmds.joint(e = True, zso = True, oj = 'xyz', secondaryAxisOrient = 'yup', ch = True)
cmds.select(d = True)

# IK controllers
''' IK controllers: Left hind leg''' 
L_IK = cmds.ikHandle(sol = 'ikRPsolver', n = 'L_HindLeg_IK', sj = L_hindFemurJntIK, ee = L_hindAnkleJntIK)
L_hindIKCtrl = cmds.curve(d=1, p=[(1,0,-1),(-1,0,-1),(-1,0,1),(1,0,1),(1,0,-1)], k=[0,1,2,3,4], n='L_FootIK_CTRL')

# Get distance to get controller with decent scale from front hind leg toe to back hind leg toe
dist = cmds.createNode('distanceDimShape', n='temp_to_delete') 
legStart = cmds.xform(L_hindToeJntIK, q = True, ws = True, rp = True) # q = query for specific value, ws = world space, rq = rotation pivot point
legEnd = cmds.xform(L_frontToeJntIK, q = True, ws = True, rp = True) # q = query for specific value, ws = world space, rq = rotation pivot point
cmds.setAttr(dist + '.endPoint', *(legStart)) # Star sign to unpack the variable = different way to access values in a list
cmds.setAttr(dist + '.startPoint', *(legEnd))
distance = cmds.getAttr(dist + '.distance')
cmds.delete(cmds.listRelatives(dist, p = True))
distance = distance / 8
cmds.setAttr(L_hindIKCtrl + '.sx', distance)
cmds.setAttr(L_hindIKCtrl + '.sy', distance)
cmds.setAttr(L_hindIKCtrl + '.sz', distance)
cmds.makeIdentity(L_hindIKCtrl, apply = True, t = 1, r = 1, s = 1, n = 0)
lockScale(L_hindIKCtrl)
L_HindIK_CTRL_GRP = cmds.group(L_hindIKCtrl, n = 'L_FootIKCtrl_GRP')
SetColorOverrideBlue(L_HindIK_CTRL_GRP)

constraintaint = cmds.pointConstraint(L_hindToeJnt, L_HindIK_CTRL_GRP)
cmds.delete(constraintaint)
cmds.parent(L_IK[0], L_hindIKCtrl)
cmds.setAttr(L_IK[0] + '.visibility', 0)

# Aim constraintaint makes the upper hind femur joints follow by some but lets the leg fold up like it should
cmds.aimConstraint(L_hindIKCtrl, L_hindFemurJntIK, n = 'L_Femur_Aim_Towards_Foot_CTRL', mo = True, wu = [0,0,0])
L_IK_Toe = cmds.ikHandle(sol = 'ikRPsolver', n = 'L_HindToe_IK', sj = L_hindAnkleJntIK, ee = L_hindToeJntIK)
cmds.parent(L_IK_Toe[0], L_hindIKCtrl)
cmds.setAttr(L_IK_Toe[0] + '.visibility', 0)

''' IK Controller: Right hind leg '''
R_IK = cmds.ikHandle(sol = 'ikRPsolver', n = 'R_HindLeg_IK', sj = R_hindUpperKneeJntIK, ee = R_hindAnkleJntIK)
R_hindIKCtrl = cmds.curve(d=1, p=[(1,0,-1),(-1,0,-1), (-1,0,1), (1,0,1),(1,0,-1)],k=[0,1,2,3,4], n='R_FootIK_CTRL')

cmds.scale(distance,distance,distance)
cmds.makeIdentity(R_hindIKCtrl, apply = True, t = 1, r = 1, s = 1, n = 0)
lockScale(R_hindIKCtrl)
R_HindIK_CTRL_GRP = cmds.group(R_hindIKCtrl, n = 'R_FootIKCtrl_GRP')
SetColorOverrideRed(R_HindIK_CTRL_GRP)

constraintaint = cmds.pointConstraint(R_hindToeJnt, R_HindIK_CTRL_GRP)
cmds.delete(constraintaint)
cmds.parent(R_IK[0], R_hindIKCtrl)
cmds.setAttr(R_IK[0] + '.visibility', 0)

'''TODO: find location, doesn't fit, to safely delete
L_FrontToe_IK = cmds.ikHandle(sol = 'ikRPsolver', n = 'L_FrontToe_IK', sj = L_frontAnkleJntIK, ee = L_frontToeJntIK)
cmds.parent(L_FrontToe_IK[0],L_frontIKCtrl)
cmds.setAttr(L_FrontToe_IK[0]+'.visibility', 0)

R_FrontToe_IK = cmds.ikHandle(sol = 'ikRPsolver', n = 'R_FrontToe_IK', sj = R_frontAnkleJntIK[0], ee = R_frontToeJntIK[0])
cmds.parent(R_FrontToe_IK[0],R_frontIKCtrl)
cmds.setAttr(R_FrontToe_IK[0]+'.visibility',0)
'''

# Aim constraintaint makes the upper hind femur joints follow by some but lets the leg fold up like it should
cmds.aimConstraint(R_hindIKCtrl, R_hindFemurJntIK, n = 'R_Femur_Aim_Towards_Foot_CTRL', mo = True, wu = [0,0,0])
R_IK_Toe = cmds.ikHandle(sol = 'ikRPsolver', n = 'R_HindToe_IK', sj = R_hindAnkleJntIK, ee = R_hindToeJntIK)
cmds.parent(R_IK_Toe[0], R_hindIKCtrl)
cmds.setAttr(R_IK_Toe[0] + '.visibility', 0)

''' IK Controller: Left front leg ''' 
L_Front_IK = cmds.ikHandle(sol = 'ikRPsolver', n = 'L_FrontLeg_IK', sj = L_frontUpperKneeJntIK, ee = L_frontAnkleJntIK)
L_frontIKCtrl = cmds.curve(d=1, p=[(1,0,-1),(-1,0,-1),(-1,0,1),(1,0,1),(1,0,-1)], k=[0,1,2,3,4], n='L_Front_Foot_IK_CTRL')
cmds.setAttr(L_frontIKCtrl + '.sx', distance)
cmds.setAttr(L_frontIKCtrl + '.sy', distance)
cmds.setAttr(L_frontIKCtrl + '.sz', distance)
cmds.makeIdentity(L_frontIKCtrl, apply = True, t = 1, r = 1, s = 1, n = 0)
lockScale(L_frontIKCtrl)
L_FrontIK_CTRL_GRP = cmds.group(L_frontIKCtrl, n = 'L_FrontFoot_IK_Ctrl_GRP')
SetColorOverrideBlue(L_FrontIK_CTRL_GRP)
constraintaint = cmds.pointConstraint(L_frontToeJnt, L_FrontIK_CTRL_GRP)
cmds.delete(constraintaint)
cmds.parent(L_Front_IK[0], L_frontIKCtrl)
cmds.setAttr(L_Front_IK[0] + '.visibility', 0)
L_Front_Toe_IK=cmds.ikHandle(sol='ikRPsolver',n='L_Front_Toe_IK',sj=L_frontAnkleJntIK,ee=L_frontToeJntIK)
cmds.parent(L_Front_Toe_IK[0],L_frontIKCtrl)

''' Left IK Front Leg Rotation Controller '''
L_frontLeg_Rotation=cmds.circle(nr = (1, 0, 0), c = (0, 0, 0), n = 'L_FrontLeg_Rotate_CTRL')[0]
L_frontLeg_Rotation_GRP = cmds.group(L_frontLeg_Rotation, n = 'L_FrontLeg_Rotate_CTRL_GRP')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(L_frontLeg_Rotation_GRP,apply=True, t=1, r=1, s=1, n=0)
constraintaint=cmds.pointConstraint(L_frontFemurJntFK, L_frontLeg_Rotation_GRP)
cmds.delete(constraintaint)
SetColorOverrideBlue(L_frontLeg_Rotation)

''' IK Controller: Right front leg '''
R_Front_IK = cmds.ikHandle(sol = 'ikRPsolver', n = 'R_FrontLeg_IK', sj = R_frontUpperKneeJntIK, ee = R_frontAnkleJntIK)
R_frontIKCtrl = cmds.curve(d=1, p=[(1,0,-1),(-1,0,-1),(-1,0,1),(1,0,1),(1,0,-1)], k=[0,1,2,3,4], n='R_Front_Foot_IK_CTRL')
cmds.setAttr(R_frontIKCtrl + '.sx', distance)
cmds.setAttr(R_frontIKCtrl + '.sy', distance)
cmds.setAttr(R_frontIKCtrl + '.sz', distance)
cmds.makeIdentity(R_frontIKCtrl, apply = True, t = 1, r = 1, s = 1, n = 0)
lockScale(R_frontIKCtrl)

R_FrontIK_CTRL_GRP = cmds.group(R_frontIKCtrl, n = 'R_FrontFoot_IK_Ctrl_GRP')
SetColorOverrideRed(R_FrontIK_CTRL_GRP)
constraintaint = cmds.pointConstraint(R_frontToeJnt, R_FrontIK_CTRL_GRP)
cmds.delete(constraintaint)
cmds.parent(R_Front_IK[0], R_frontIKCtrl)
cmds.setAttr(R_Front_IK[0] + '.visibility', 0)

R_Front_Toe_IK=cmds.ikHandle(sol='ikRPsolver',n='R_Front_Toe_IK',sj = R_frontAnkleJntIK, ee = R_frontToeJntIK)
cmds.parent(R_Front_Toe_IK[0],R_frontIKCtrl)

# Right IK Front Leg Rotation Controller
R_frontLeg_Rotation=cmds.circle(nr = (1, 0, 0), c = (0, 0, 0), n = 'R_FrontLeg_Rotate_CTRL')[0]
R_frontLeg_Rotation_GRP = cmds.group(R_frontLeg_Rotation, n = 'R_FrontLeg_Rotate_CTRL_GRP')
cmds.scale(distance, distance, distance)
cmds.makeIdentity(R_frontLeg_Rotation_GRP, apply=True, t=1, r=1, s=1, n=0) 
constraintaint=cmds.pointConstraint(R_frontFemurJntFK, R_frontLeg_Rotation_GRP)
cmds.delete(constraintaint)
SetColorOverrideRed(R_frontLeg_Rotation)

''' Create IK polevector for L hind IK '''
# Left Hind IK PoleVector
L_hindPole = cmds.curve(d=1, p=[(-1.03923,0,0.6),(1.03923,0,0.6),(0,0,-1.2),(-1.03923,0,0.6)], k=[0,1,2,3],n='L_HindPoleVector_CTRL')
cmds.scale(distance/2, distance/2, distance/2)
cmds.makeIdentity(L_hindPole, apply = True, t = 1, r = 1, s = 1, n = 0)
lockScale(L_hindPole)
lockRotate(L_hindPole)
L_HindPole_GRP = cmds.group(L_hindPole, n = 'L_HindPoleVector_CTRL_GRP')
constraintaint = cmds.parentConstraint(hindKnee, L_HindPole_GRP)
cmds.delete(constraintaint)

addDist = cmds.getAttr(L_HindPole_GRP + '.translateZ')
cmds.setAttr(L_HindPole_GRP + '.translateZ', addDist * 2)
SetColorOverrideBlue(L_hindPole)
cmds.poleVectorConstraint(L_hindPole, L_IK[0])

# If the leg rotates in a weird way: set the twist of the IK to 180 degrees to get the leg back to normal. Not always necessary (tested on Mac: necessary). 
cmds.setAttr(L_IK[0] + '.twist', 180)

# Right Hind IK PoleVector
R_hindPole=cmds.curve(d=1, p=[(-1.03923,0,0.6),(1.03923,0,0.6),(0,0,-1.2),(-1.03923,0,0.6)], k=[0,1,2,3],n='R_HindPoleVector_CTRL')
cmds.scale(distance/2, distance/2, distance/2)
cmds.makeIdentity(R_hindPole, apply = True, t = 1, r = 1, s = 1, n = 0)
lockScale(R_hindPole)
lockRotate(R_hindPole)
R_HindPole_GRP = cmds.group(R_hindPole, n = 'R_HindPoleVector_CTRL_GRP')
constraintaint = cmds.parentConstraint(hindKnee, R_HindPole_GRP)
cmds.delete(constraintaint)
reverseDist = cmds.getAttr(R_HindPole_GRP + '.translateX')
cmds.setAttr(R_HindPole_GRP + '.translateX', -reverseDist)
cmds.setAttr(R_HindPole_GRP + '.translateZ', addDist * 2)
cmds.poleVectorConstraint(R_hindPole, R_IK[0])
SetColorOverrideRed(R_hindPole)

# If the leg rotates in a weird way: set the twist of the IK to 180 degrees to get the leg back to normal. Not always necessary. 
# cmds.setAttr(R_IK[0] + '.twist', 180) 

# Left & Right Front IK PoleVector
L_frontPole = cmds.curve(d=1, p=[(-1.03923,0,0.6),(1.03923,0,0.6),(0,0,-1.2),(-1.03923,0,0.6)], k=[0,1,2,3],n='L_FrontPoleVector_CTRL')
cmds.scale(distance/2, distance/2, distance/2)
cmds.makeIdentity(L_frontPole, apply = True, t = 1, r = 1, s = 1, n = 0)
lockScale(L_frontPole)
lockRotate(L_frontPole)
L_FrontPole_GRP = cmds.group(L_frontPole, n = 'L_FrontPoleVector_CTRL_GRP')
constraintaint = cmds.parentConstraint(frontKnee, L_FrontPole_GRP)
cmds.delete(constraintaint)
addDist = cmds.getAttr(L_FrontPole_GRP + '.translateZ')
cmds.setAttr(L_FrontPole_GRP + '.translateZ', distance * 2)
SetColorOverrideBlue(L_frontPole)
cmds.poleVectorConstraint(L_frontPole, L_Front_IK[0])
# If the leg rotates in a weird way: set the twist of the IK to 180 degrees to get the leg back to normal. Not always necessary  (tested on Mac: necessary).  
cmds.setAttr(L_Front_IK[0] + '.twist', 180) 

R_frontPole = cmds.curve(d=1, p=[(-1.03923,0,0.6),(1.03923,0,0.6),(0,0,-1.2),(-1.03923,0,0.6)], k=[0,1,2,3],n='R_FrontPoleVector_CTRL')
cmds.scale(distance/2, distance/2, distance/2)
cmds.makeIdentity(R_frontPole, apply = True, t = 1, r = 1, s = 1, n = 0)
lockScale(R_frontPole)
lockRotate(R_frontPole)
R_FrontPole_GRP = cmds.group(R_frontPole, n = 'R_FrontPoleVector_CTRL_GRP')
constraintaint = cmds.parentConstraint(frontKnee, R_FrontPole_GRP)
cmds.delete(constraintaint)
addDist=cmds.getAttr(R_FrontPole_GRP+'.tz')
cmds.setAttr(R_FrontPole_GRP+'.tz', distance*2)
reverseDist = cmds.getAttr(R_FrontPole_GRP + '.translateX')
cmds.setAttr(R_FrontPole_GRP + '.translateX', -reverseDist)
SetColorOverrideRed(R_frontPole)
cmds.poleVectorConstraint(R_frontPole, R_Front_IK[0])
# If the leg rotates in a weird way: set the twist of the IK to 180 degrees to get the leg back to normal. Not always necessary. 
cmds.setAttr(R_Front_IK[0] + '.twist', 180) 

# Group IK Pole Vectors
poleVectorGRP = cmds.group(L_FrontPole_GRP, R_FrontPole_GRP, L_HindPole_GRP, R_HindPole_GRP, n='C_PoleVector_GRP')
IK_CTRL_GRP=cmds.group(poleVectorGRP,R_frontLeg_Rotation_GRP,L_frontLeg_Rotation_GRP,R_FrontIK_CTRL_GRP,L_FrontIK_CTRL_GRP,R_HindIK_CTRL_GRP,L_HindIK_CTRL_GRP, n='C_IK_CTRL_GRP')

# cont
''' FK Leg Setup '''
# FK Left Hind Leg
L_HindLeg_FK_CTRL = cmds.circle(nr = (0, 1, 0), c = (0, 0, 0), n = 'L_HindLeg_FK_CTRL')
cmds.scale(distance, distance, distance)
cmds.makeIdentity(L_HindLeg_FK_CTRL, apply=True, t=1, r=1, s=1, n=0)
L_HindLeg_FK_CTRL_GRP=cmds.group(L_HindLeg_FK_CTRL,n='L_HindLeg_FK_CTRL_GRP')
constraintaint=cmds.pointConstraint(L_hindFemurJntFK, L_HindLeg_FK_CTRL_GRP)
cmds.delete(constraintaint)
constraintaint=cmds.parentConstraint(L_HindLeg_FK_CTRL_GRP,L_hindFemurJntFK,mo=True)
lockScale(L_HindLeg_FK_CTRL[0])

L_HindUpperKneeF_FK_CTRL=cmds.circle(nr=(0, 1, 0), c=(0, 0, 0),n='L_HindUpperKnee_FK_CTRL')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(L_HindUpperKneeF_FK_CTRL,apply=True, t=1, r=1, s=1, n=0)
L_HindUpperKnee_FK_CTRL_GRP=cmds.group(L_HindUpperKneeF_FK_CTRL,n='L_HindUpperKnee_FK_CTRL_GRP')
constraintaint=cmds.pointConstraint(L_hindUpperKneeJntFK,L_HindUpperKnee_FK_CTRL_GRP)
cmds.delete(constraintaint)
constraintaint=cmds.parentConstraint(L_HindUpperKneeF_FK_CTRL,L_hindUpperKneeJntFK,mo=True)
lockScale(L_HindUpperKneeF_FK_CTRL[0])

L_HindKnee_FK_CTRL=cmds.circle( nr=(0, 1, 0), c=(0, 0, 0),n='L_HindKnee_FK_CTRL')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(L_HindKnee_FK_CTRL,apply=True, t=1, r=1, s=1, n=0)
L_HindKnee_FK_CTRL_GRP=cmds.group(L_HindKnee_FK_CTRL,n='L_HindKnee_FK_CTRL_GRP')
constraintaint=cmds.pointConstraint(L_hindKneeJntFK,L_HindKnee_FK_CTRL_GRP)
cmds.delete(constraintaint)
constraintaint=cmds.parentConstraint(L_HindKnee_FK_CTRL,L_hindKneeJntFK,mo=True)
lockScale(L_HindKnee_FK_CTRL[0])

L_HindAnkle_FK_CTRL=cmds.circle( nr=(0, 1, 0), c=(0, 0, 0),n='L_HindAnkle_FK_CTRL')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(L_HindAnkle_FK_CTRL,apply=True, t=1, r=1, s=1, n=0)
L_HindAnkle_FK_CTRL_GRP=cmds.group(L_HindAnkle_FK_CTRL,n='L_HindAnkle_FK_CTRL_GRP')
constraintaint=cmds.pointConstraint(L_hindAnkleJntFK,L_HindAnkle_FK_CTRL_GRP)
cmds.delete(constraintaint)
constraintaint=cmds.parentConstraint(L_HindAnkle_FK_CTRL,L_hindAnkleJntFK,mo=True)
lockScale(L_HindAnkle_FK_CTRL[0])

L_HindToe_FK_CTRL=cmds.circle( nr=(0, 1, 0), c=(0, 0, 0),n='L_HindToe_FK_CTRL')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(L_HindToe_FK_CTRL,apply=True, t=1, r=1, s=1, n=0)
L_HindToe_FK_CTRL_GRP=cmds.group(L_HindToe_FK_CTRL,n='L_HindToe_FK_CTRL_GRP')
constraintaint=cmds.pointConstraint(L_hindToeJntFK,L_HindToe_FK_CTRL_GRP)
cmds.delete(constraintaint)
constraintaint=cmds.parentConstraint(L_HindToe_FK_CTRL,L_hindToeJntFK,mo=True)
lockScale(L_HindToe_FK_CTRL[0])

# Parent hind left leg FK controllers to hind pelvis
cmds.parent(L_HindToe_FK_CTRL_GRP,L_HindAnkle_FK_CTRL[0])
cmds.parent(L_HindAnkle_FK_CTRL_GRP,L_HindKnee_FK_CTRL[0])
cmds.parent(L_HindKnee_FK_CTRL_GRP,L_HindUpperKneeF_FK_CTRL[0])
cmds.parent(L_HindUpperKnee_FK_CTRL_GRP,L_HindLeg_FK_CTRL[0])
SetColorOverrideBlue(L_HindLeg_FK_CTRL[0])
cmds.parentConstraint(hindPelvisJnt,L_HindLeg_FK_CTRL_GRP,mo=True)

# FK Right Hind Leg
R_HindLeg_FK_CTRL = cmds.circle(nr = (0, 1, 0), c = (0, 0, 0), n = 'R_HindLeg_FK_CTRL')
cmds.scale(distance, distance, distance)
cmds.makeIdentity(R_HindLeg_FK_CTRL, apply=True, t=1, r=1, s=1, n=0)
R_HindLeg_FK_CTRL_GRP=cmds.group(R_HindLeg_FK_CTRL,n='R_HindLeg_FK_CTRL_GRP')
constraintaint=cmds.pointConstraint(R_hindFemurJntFK, R_HindLeg_FK_CTRL_GRP)
cmds.delete(constraintaint)
constraintaint=cmds.parentConstraint(R_HindLeg_FK_CTRL_GRP,R_hindFemurJntFK,mo=True)
lockScale(R_HindLeg_FK_CTRL[0])

R_HindUpperKnee_FK_CTRL=cmds.circle(nr=(0, 1, 0), c=(0, 0, 0),n='R_HindUpperKnee_FK_CTRL')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(R_HindUpperKnee_FK_CTRL,apply=True, t=1, r=1, s=1, n=0)
R_HindUpperKnee_FK_CTRL_GRP=cmds.group(R_HindUpperKnee_FK_CTRL,n='R_HindUpperKnee_FK_CTRL_GRP')
constraintaint=cmds.pointConstraint(R_hindUpperKneeJntFK,R_HindUpperKnee_FK_CTRL_GRP)
cmds.delete(constraintaint)
constraintaint=cmds.parentConstraint(R_HindUpperKnee_FK_CTRL,R_hindUpperKneeJntFK,mo=True)
lockScale(R_HindUpperKnee_FK_CTRL[0])

R_HindKnee_FK_CTRL=cmds.circle( nr=(0, 1, 0), c=(0, 0, 0),n='R_HindKnee_FK_CTRL')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(R_HindKnee_FK_CTRL,apply=True, t=1, r=1, s=1, n=0)
R_HindKnee_FK_CTRL_GRP=cmds.group(R_HindKnee_FK_CTRL,n='R_HindKnee_FK_CTRL_GRP')
constraintaint=cmds.pointConstraint(R_hindKneeJntFK,R_HindKnee_FK_CTRL_GRP)
cmds.delete(constraintaint)
constraintaint=cmds.parentConstraint(R_HindKnee_FK_CTRL,R_hindKneeJntFK,mo=True)
lockScale(R_HindKnee_FK_CTRL[0])

R_HindAnkle_FK_CTRL=cmds.circle( nr=(0, 1, 0), c=(0, 0, 0),n='R_HindAnkle_FK_CTRL')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(R_HindAnkle_FK_CTRL,apply=True, t=1, r=1, s=1, n=0)
R_HindAnkle_FK_CTRL_GRP=cmds.group(R_HindAnkle_FK_CTRL,n='R_HindAnkle_FK_CTRL_GRP')
constraintaint=cmds.pointConstraint(R_hindAnkleJntFK,R_HindAnkle_FK_CTRL_GRP)
cmds.delete(constraintaint)
constraintaint=cmds.parentConstraint(R_HindAnkle_FK_CTRL,R_hindAnkleJntFK,mo=True)
lockScale(R_HindAnkle_FK_CTRL[0])

R_HindToe_FK_CTRL=cmds.circle( nr=(0, 1, 0), c=(0, 0, 0),n='R_HindToe_FK_CTRL')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(R_HindToe_FK_CTRL,apply=True, t=1, r=1, s=1, n=0)
R_HindToe_FK_CTRL_GRP=cmds.group(R_HindToe_FK_CTRL,n='R_HindToe_FK_CTRL_GRP')
constraintaint=cmds.pointConstraint(R_hindToeJntFK,R_HindToe_FK_CTRL_GRP)
cmds.delete(constraintaint)
constraintaint=cmds.parentConstraint(R_HindToe_FK_CTRL,R_hindToeJntFK,mo=True)
lockScale(R_HindToe_FK_CTRL[0])

# Parent hind right leg FK controllers to hind pelvis
cmds.parent(R_HindToe_FK_CTRL_GRP,R_HindAnkle_FK_CTRL[0])
cmds.parent(R_HindAnkle_FK_CTRL_GRP,R_HindKnee_FK_CTRL[0])
cmds.parent(R_HindKnee_FK_CTRL_GRP,R_HindUpperKnee_FK_CTRL[0])
cmds.parent(R_HindUpperKnee_FK_CTRL_GRP,R_HindLeg_FK_CTRL[0])
SetColorOverrideBlue(R_HindLeg_FK_CTRL[0])
cmds.parentConstraint(hindPelvisJnt,R_HindLeg_FK_CTRL_GRP,mo=True)

# FK Left Front Leg
L_FrontLeg_FK_CTRL = cmds.circle(nr = (0, 1, 0), c = (0, 0, 0), n = 'L_FrontLeg_FK_CTRL')
cmds.scale(distance, distance, distance)
cmds.makeIdentity(L_FrontLeg_FK_CTRL, apply=True, t=1, r=1, s=1, n=0)
L_FrontLeg_FK_CTRL_GRP=cmds.group(L_FrontLeg_FK_CTRL,n='L_FrontLeg_FK_CTRL_GRP')
constraintaint=cmds.pointConstraint(L_frontFemurJntFK, L_FrontLeg_FK_CTRL_GRP)
cmds.delete(constraintaint)
constraintaint=cmds.parentConstraint(L_FrontLeg_FK_CTRL_GRP,L_frontFemurJntFK,mo=True)
lockScale(L_FrontLeg_FK_CTRL[0])

L_FrontUpperKneeF_FK_CTRL=cmds.circle(nr=(0, 1, 0), c=(0, 0, 0),n='L_FrontUpperKnee_FK_CTRL')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(L_FrontUpperKneeF_FK_CTRL,apply=True, t=1, r=1, s=1, n=0)
L_FrontUpperKnee_FK_CTRL_GRP=cmds.group(L_FrontUpperKneeF_FK_CTRL,n='L_FrontUpperKnee_FK_CTRL_GRP')
constraintaint=cmds.pointConstraint(L_frontUpperKneeJntFK,L_FrontUpperKnee_FK_CTRL_GRP)
cmds.delete(constraintaint)
constraintaint=cmds.parentConstraint(L_FrontUpperKneeF_FK_CTRL,L_frontUpperKneeJntFK,mo=True)
lockScale(L_FrontUpperKneeF_FK_CTRL[0])

L_FrontKnee_FK_CTRL=cmds.circle( nr=(0, 1, 0), c=(0, 0, 0),n='L_FrontKnee_FK_CTRL')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(L_FrontKnee_FK_CTRL,apply=True, t=1, r=1, s=1, n=0)
L_FrontKnee_FK_CTRL_GRP=cmds.group(L_FrontKnee_FK_CTRL,n='L_FrontKnee_FK_CTRL_GRP')
constraintaint=cmds.pointConstraint(L_frontKneeJntFK,L_FrontKnee_FK_CTRL_GRP)
cmds.delete(constraintaint)
constraintaint=cmds.parentConstraint(L_FrontKnee_FK_CTRL,L_frontKneeJntFK,mo=True)
lockScale(L_FrontKnee_FK_CTRL[0])

L_FrontAnkle_FK_CTRL=cmds.circle( nr=(0, 1, 0), c=(0, 0, 0),n='L_FrontAnkle_FK_CTRL')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(L_FrontAnkle_FK_CTRL,apply=True, t=1, r=1, s=1, n=0)
L_FrontAnkle_FK_CTRL_GRP=cmds.group(L_FrontAnkle_FK_CTRL,n='L_FrontAnkle_FK_CTRL_GRP')
constraintaint=cmds.pointConstraint(L_frontAnkleJntFK,L_FrontAnkle_FK_CTRL_GRP)
cmds.delete(constraintaint)
constraintaint=cmds.parentConstraint(L_FrontAnkle_FK_CTRL,L_frontAnkleJntFK,mo=True)
lockScale(L_FrontAnkle_FK_CTRL[0])

L_FrontToe_FK_CTRL=cmds.circle( nr=(0, 1, 0), c=(0, 0, 0),n='L_FrontToe_FK_CTRL')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(L_FrontToe_FK_CTRL,apply=True, t=1, r=1, s=1, n=0)
L_FrontToe_FK_CTRL_GRP=cmds.group(L_FrontToe_FK_CTRL,n='L_FrontToe_FK_CTRL_GRP')
constraintaint=cmds.pointConstraint(L_frontToeJntFK,L_FrontToe_FK_CTRL_GRP)
cmds.delete(constraintaint)
constraintaint=cmds.parentConstraint(L_FrontToe_FK_CTRL,L_frontToeJntFK,mo=True)
lockScale(L_FrontToe_FK_CTRL[0])

# Parent left front leg FK controllers to front pelvis
cmds.parent(L_FrontToe_FK_CTRL_GRP,L_FrontAnkle_FK_CTRL[0])
cmds.parent(L_FrontAnkle_FK_CTRL_GRP,L_FrontKnee_FK_CTRL[0])
cmds.parent(L_FrontKnee_FK_CTRL_GRP,L_FrontUpperKneeF_FK_CTRL[0])
cmds.parent(L_FrontUpperKnee_FK_CTRL_GRP,L_FrontLeg_FK_CTRL[0])
SetColorOverrideBlue(L_FrontLeg_FK_CTRL[0])
cmds.parentConstraint(frontPelvisJnt,L_FrontLeg_FK_CTRL_GRP,mo=True)

# FK Right Front Leg
R_FrontLeg_FK_CTRL = cmds.circle(nr = (0, 1, 0), c = (0, 0, 0), n = 'R_FrontLeg_FK_CTRL')
cmds.scale(distance, distance, distance)
cmds.makeIdentity(R_FrontLeg_FK_CTRL, apply=True, t=1, r=1, s=1, n=0)
R_FrontLeg_FK_CTRL_GRP=cmds.group(R_FrontLeg_FK_CTRL,n='R_FrontLeg_FK_CTRL_GRP')
constraintaint=cmds.pointConstraint(R_frontFemurJntFK, R_FrontLeg_FK_CTRL_GRP)
cmds.delete(constraintaint)
constraintaint=cmds.parentConstraint(R_FrontLeg_FK_CTRL_GRP,R_frontFemurJntFK,mo=True)
lockScale(R_FrontLeg_FK_CTRL[0])

R_FrontUpperKneeF_FK_CTRL=cmds.circle(nr=(0, 1, 0), c=(0, 0, 0),n='R_FrontUpperKnee_FK_CTRL')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(R_FrontUpperKneeF_FK_CTRL,apply=True, t=1, r=1, s=1, n=0)
R_FrontUpperKnee_FK_CTRL_GRP=cmds.group(R_FrontUpperKneeF_FK_CTRL,n='R_FrontUpperKnee_FK_CTRL_GRP')
constraintaint=cmds.pointConstraint(R_frontUpperKneeJntFK,R_FrontUpperKnee_FK_CTRL_GRP)
cmds.delete(constraintaint)
constraintaint=cmds.parentConstraint(R_FrontUpperKneeF_FK_CTRL,R_frontUpperKneeJntFK,mo=True)
lockScale(R_FrontUpperKneeF_FK_CTRL[0])

R_FrontKnee_FK_CTRL=cmds.circle( nr=(0, 1, 0), c=(0, 0, 0),n='R_FrontKnee_FK_CTRL')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(R_FrontKnee_FK_CTRL,apply=True, t=1, r=1, s=1, n=0)
R_FrontKnee_FK_CTRL_GRP=cmds.group(R_FrontKnee_FK_CTRL,n='R_FrontKnee_FK_CTRL_GRP')
constraintaint=cmds.pointConstraint(R_frontKneeJntFK,R_FrontKnee_FK_CTRL_GRP)
cmds.delete(constraintaint)
constraintaint=cmds.parentConstraint(R_FrontKnee_FK_CTRL,R_frontKneeJntFK,mo=True)
lockScale(R_FrontKnee_FK_CTRL[0])

R_FrontAnkle_FK_CTRL=cmds.circle( nr=(0, 1, 0), c=(0, 0, 0),n='R_FrontAnkle_FK_CTRL')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(R_FrontAnkle_FK_CTRL,apply=True, t=1, r=1, s=1, n=0)
R_FrontAnkle_FK_CTRL_GRP=cmds.group(R_FrontAnkle_FK_CTRL,n='R_FrontAnkle_FK_CTRL_GRP')
constraintaint=cmds.pointConstraint(R_frontAnkleJntFK,R_FrontAnkle_FK_CTRL_GRP)
cmds.delete(constraintaint)
constraintaint=cmds.parentConstraint(R_FrontAnkle_FK_CTRL,R_frontAnkleJntFK,mo=True)
lockScale(R_FrontAnkle_FK_CTRL[0])

R_FrontToe_FK_CTRL=cmds.circle( nr=(0, 1, 0), c=(0, 0, 0),n='R_FrontToe_FK_CTRL')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(R_FrontToe_FK_CTRL,apply=True, t=1, r=1, s=1, n=0)
R_FrontToe_FK_CTRL_GRP=cmds.group(R_FrontToe_FK_CTRL,n='R_FrontToe_FK_CTRL_GRP')
constraintaint=cmds.pointConstraint(R_frontToeJntFK,R_FrontToe_FK_CTRL_GRP)
cmds.delete(constraintaint)
constraintaint=cmds.parentConstraint(R_FrontToe_FK_CTRL,R_frontToeJntFK,mo=True)
lockScale(R_FrontToe_FK_CTRL[0])

# Parent left front leg FK controllers to front pelvis
cmds.parent(R_FrontToe_FK_CTRL_GRP,R_FrontAnkle_FK_CTRL[0])
cmds.parent(R_FrontAnkle_FK_CTRL_GRP,R_FrontKnee_FK_CTRL[0])
cmds.parent(R_FrontKnee_FK_CTRL_GRP,R_FrontUpperKneeF_FK_CTRL[0])
cmds.parent(R_FrontUpperKnee_FK_CTRL_GRP,R_FrontLeg_FK_CTRL[0])
SetColorOverrideBlue(R_FrontLeg_FK_CTRL[0])
cmds.parentConstraint(frontPelvisJnt,R_FrontLeg_FK_CTRL_GRP,mo=True)

# Group fk controllers...
FK_CTRL_GRP=cmds.group(L_HindLeg_FK_CTRL_GRP,R_HindLeg_FK_CTRL_GRP,L_FrontLeg_FK_CTRL_GRP,R_FrontLeg_FK_CTRL_GRP, n='C_FK_CTRL_GRP')

''' IK FK Switch '''
# L & R Hind Leg Switch
L_hindSwitch=cmds.curve(d=3, p=[(0.474561,0,-1.241626),(0.171579,0,-1.214307),(-0.434384,0,-1.159672),(-1.124061,0,-0.419971),(-1.169741,0,0.305922),(-0.792507,0,1.018176),(-0.0412486,0,1.262687),(0.915809,0,1.006098),(1.258635,0,0.364883),(1.032378,0,-0.461231),(0.352527,0,-0.810017),(-0.451954,0,-0.43765),(-0.634527,0,0.208919),(-0.0751226,0,0.696326),(0.292338,0,0.414161),(0.476068,0,0.273078)],k=[0,0,0,1,2,3,4,5,6,7,8,9,10,11,12,13,13,13],n='l_hindSwitch_CTRL')
cmds.scale(distance/3,distance/3,distance/3)
cmds.makeIdentity(apply=True, t=1,r=1,s=1,n=0)
lockScale(L_hindSwitch)
lockTranslate(L_hindSwitch)
lockRotate(L_hindSwitch)

L_HindSwitch_GRP=cmds.group(L_hindSwitch, n='L_HindSwitch_CTRL_GRP')
constraintaint=cmds.pointConstraint(L_hindAnkleJnt, L_HindSwitch_GRP)
cmds.delete(constraintaint)
dist=cmds.getAttr(L_HindSwitch_GRP+'.tz')
cmds.setAttr(L_HindSwitch_GRP+'.tz',dist-distance)

constraintaint=cmds.pointConstraint(L_hindAnkleJnt,L_HindSwitch_GRP,mo=True)
SetColorOverrideBlue(L_hindSwitch)
cmds.addAttr(L_hindSwitch,longName='Leg_functions',at='enum',en=('____'),k=True)
cmds.setAttr(L_hindSwitch+'.Leg_functions',l=True)
cmds.addAttr(L_hindSwitch,longName='IK_FK',at='float', min=0, max=1, k=True)

R_hindSwitch=cmds.curve(d=3, p=[(0.474561,0,-1.241626),(0.171579,0,-1.214307),(-0.434384,0,-1.159672),(-1.124061,0,-0.419971),(-1.169741,0,0.305922),(-0.792507,0,1.018176),(-0.0412486,0,1.262687),(0.915809,0,1.006098),(1.258635,0,0.364883),(1.032378,0,-0.461231),(0.352527,0,-0.810017),(-0.451954,0,-0.43765),(-0.634527,0,0.208919),(-0.0751226,0,0.696326),(0.292338,0,0.414161),(0.476068,0,0.273078)],k=[0,0,0,1,2,3,4,5,6,7,8,9,10,11,12,13,13,13],n='l_hindSwitch_CTRR')
cmds.scale(distance/3,distance/3,distance/3)
cmds.makeIdentity(apply=True, t=1,r=1,s=1,n=0)
lockScale(R_hindSwitch)
lockTranslate(R_hindSwitch)
lockRotate(R_hindSwitch)

R_HindSwitch_GRP=cmds.group(R_hindSwitch, n='R_HindSwitch_CTRR_GRP')
constraintaint=cmds.pointConstraint(R_hindAnkleJnt, R_HindSwitch_GRP)
cmds.delete(constraintaint)
dist=cmds.getAttr(R_HindSwitch_GRP+'.tz')
cmds.setAttr(R_HindSwitch_GRP+'.tz',dist-distance)

constraintaint=cmds.pointConstraint(R_hindAnkleJnt,R_HindSwitch_GRP,mo=True)
SetColorOverrideRed(R_hindSwitch)
cmds.addAttr(R_hindSwitch,longName='Leg_functions',at='enum',en=('____'),k=True)
cmds.setAttr(R_hindSwitch+'.Leg_functions',l=True)
cmds.addAttr(R_hindSwitch,longName='IK_FK',at='float', min=0, max=1, k=True)

# Visibility of controllers: make sure you don't see the extra controllers when they're not active.
cmds.connectAttr(L_hindSwitch+'.IK_FK',L_HindLeg_FK_CTRL_GRP+'.visibility') 
cmds.connectAttr(R_hindSwitch+'.IK_FK',R_HindLeg_FK_CTRL_GRP+'.visibility')
Ik_FK_Hind_Reverse = cmds.createNode('reverse', n='IK_FK_HindLeg_REV')
cmds.connectAttr(L_hindSwitch+'.IK_FK', Ik_FK_Hind_Reverse+'.ix')
cmds.connectAttr(R_hindSwitch+'.IK_FK', Ik_FK_Hind_Reverse+'.iy')
cmds.connectAttr(Ik_FK_Hind_Reverse+'.ox', L_HindIK_CTRL_GRP+'.visibility') 
cmds.connectAttr(Ik_FK_Hind_Reverse+'.oy', R_HindIK_CTRL_GRP+'.visibility') 
cmds.connectAttr(Ik_FK_Hind_Reverse+'.ox', L_HindPole_GRP+'.visibility') 
cmds.connectAttr(Ik_FK_Hind_Reverse+'.oy', R_HindPole_GRP+'.visibility') 

# L & R Front Leg Switch
L_frontSwitch=cmds.curve(d=3, p=[(0.474561,0,-1.241626),(0.171579,0,-1.214307),(-0.434384,0,-1.159672),(-1.124061,0,-0.419971),(-1.169741,0,0.305922),(-0.792507,0,1.018176),(-0.0412486,0,1.262687),(0.915809,0,1.006098),(1.258635,0,0.364883),(1.032378,0,-0.461231),(0.352527,0,-0.810017),(-0.451954,0,-0.43765),(-0.634527,0,0.208919),(-0.0751226,0,0.696326),(0.292338,0,0.414161),(0.476068,0,0.273078)],k=[0,0,0,1,2,3,4,5,6,7,8,9,10,11,12,13,13,13],n='l_frontSwitch_CTRL')
cmds.scale(distance/3,distance/3,distance/3)
cmds.makeIdentity(apply=True, t=1,r=1,s=1,n=0)
lockScale(L_frontSwitch)
lockTranslate(L_frontSwitch)
lockRotate(L_frontSwitch)

L_FrontSwitch_GRP=cmds.group(L_frontSwitch, n='L_FrontSwitch_CTRL_GRP')
constraintaint=cmds.pointConstraint(L_frontAnkleJnt, L_FrontSwitch_GRP)
cmds.delete(constraintaint)
dist=cmds.getAttr(L_FrontSwitch_GRP+'.tz')
cmds.setAttr(L_FrontSwitch_GRP+'.tz',dist-distance)

constraintaint=cmds.pointConstraint(L_frontAnkleJnt,L_FrontSwitch_GRP,mo=True)
SetColorOverrideBlue(L_frontSwitch)
cmds.addAttr(L_frontSwitch,longName='Leg_functions',at='enum',en=('____'),k=True)
cmds.setAttr(L_frontSwitch+'.Leg_functions',l=True)
cmds.addAttr(L_frontSwitch,longName='IK_FK',at='float', min=0, max=1, k=True)

R_frontSwitch=cmds.curve(d=3, p=[(0.474561,0,-1.241626),(0.171579,0,-1.214307),(-0.434384,0,-1.159672),(-1.124061,0,-0.419971),(-1.169741,0,0.305922),(-0.792507,0,1.018176),(-0.0412486,0,1.262687),(0.915809,0,1.006098),(1.258635,0,0.364883),(1.032378,0,-0.461231),(0.352527,0,-0.810017),(-0.451954,0,-0.43765),(-0.634527,0,0.208919),(-0.0751226,0,0.696326),(0.292338,0,0.414161),(0.476068,0,0.273078)],k=[0,0,0,1,2,3,4,5,6,7,8,9,10,11,12,13,13,13],n='l_frontSwitch_CTRR')
cmds.scale(distance/3,distance/3,distance/3)
cmds.makeIdentity(apply=True, t=1,r=1,s=1,n=0)
lockScale(R_frontSwitch)
lockTranslate(R_frontSwitch)
lockRotate(R_frontSwitch)

R_FrontSwitch_GRP=cmds.group(R_frontSwitch, n='R_FrontSwitch_CTRR_GRP')
constraintaint=cmds.pointConstraint(R_frontAnkleJnt, R_FrontSwitch_GRP)
cmds.delete(constraintaint)
dist=cmds.getAttr(R_FrontSwitch_GRP+'.tz')
cmds.setAttr(R_FrontSwitch_GRP+'.tz',dist-distance)

constraintaint=cmds.pointConstraint(R_frontAnkleJnt,R_FrontSwitch_GRP,mo=True)
SetColorOverrideRed(R_frontSwitch)
cmds.addAttr(R_frontSwitch,longName='Leg_functions',at='enum',en=('____'),k=True)
cmds.setAttr(R_frontSwitch+'.Leg_functions',l=True)
cmds.addAttr(R_frontSwitch,longName='IK_FK',at='float', min=0, max=1, k=True)

# Visibility of controllers: make sure you don't see the extra controllers when they're not active.
cmds.connectAttr(L_frontSwitch+'.IK_FK',L_FrontLeg_FK_CTRL_GRP+'.visibility')
cmds.connectAttr(R_frontSwitch+'.IK_FK',R_FrontLeg_FK_CTRL_GRP+'.visibility')
IkFkfrontRev=cmds.createNode('reverse', n='IK_FK_frontLeg_REV')
cmds.connectAttr(L_frontSwitch+'.IK_FK', IkFkfrontRev+'.ix')
cmds.connectAttr(R_frontSwitch+'.IK_FK', IkFkfrontRev+'.iy')
cmds.connectAttr(IkFkfrontRev+'.ox', L_FrontIK_CTRL_GRP+'.visibility')
cmds.connectAttr(IkFkfrontRev+'.oy', R_FrontIK_CTRL_GRP+'.visibility')
cmds.connectAttr(IkFkfrontRev+'.ox', L_FrontPole_GRP+'.visibility')
cmds.connectAttr(IkFkfrontRev+'.oy', R_FrontPole_GRP+'.visibility')

# Group IK FK switch system
legSwitchGrp=cmds.group(L_FrontSwitch_GRP,R_FrontSwitch_GRP,L_HindSwitch_GRP,R_HindSwitch_GRP, n='C_LegSwitch_CTRL_GRP')
leg_CTRL_GRP=cmds.group(IK_CTRL_GRP,FK_CTRL_GRP, n='C_Leg_CTRL_GRP')

# Blend IK FK joint influence...
def BlendJoints(ikJoints,fkJoints,skinJoints,master):
    count=0
    for e in skinJoints:
        # Order: IK - FK - Main
        blendR1=cmds.shadingNode('blendColors',asUtility=True, n='L_IKFK_Switch_rotate_1')
        cmds.connectAttr(ikJoints[count]+'.rx',blendR1+'.color1R')
        cmds.connectAttr(ikJoints[count]+'.ry',blendR1+'.color1G')
        cmds.connectAttr(ikJoints[count]+'.rz',blendR1+'.color1B')
        cmds.connectAttr(fkJoints[count]+'.rx',blendR1+'.color2R')
        cmds.connectAttr(fkJoints[count]+'.ry',blendR1+'.color2G')
        cmds.connectAttr(fkJoints[count]+'.rz',blendR1+'.color2B')
        # Connect the master to the blender attribute
        cmds.connectAttr(blendR1+'.output.outputR',skinJoints[count]+'.rx')
        cmds.connectAttr(blendR1+'.output.outputG',skinJoints[count]+'.ry')
        cmds.connectAttr(blendR1+'.output.outputB',skinJoints[count]+'.rz')
        cmds.connectAttr(master,blendR1+'.blender')
        count+=1

skinJoints=[L_hindToeJnt,L_hindAnkleJnt,L_hindKneeJnt,L_hindUpperKneeJnt,L_hindFemurJnt]
ikJoints=[L_hindToeJntIK,L_hindAnkleJntIK,L_hindKneeJntIK,L_hindUpperKneeJntIK,L_hindFemurJntIK]
fkJoints=[L_hindToeJntFK,L_hindAnkleJntFK,L_hindKneeJntFK,L_hindUpperKneeJntFK,L_hindFemurJntFK]
master = Ik_FK_Hind_Reverse + '.ox' # Left leg
BlendJoints(ikJoints,fkJoints,skinJoints,master)

skinJoints=[R_hindToeJnt,R_hindAnkleJnt,R_hindKneeJnt,R_hindUpperKneeJnt,R_hindFemurJnt]
ikJoints=[R_hindToeJntIK,R_hindAnkleJntIK,R_hindKneeJntIK,R_hindUpperKneeJntIK,R_hindFemurJntIK]
fkJoints=[R_hindToeJntFK,R_hindAnkleJntFK,R_hindKneeJntFK,R_hindUpperKneeJntFK,R_hindFemurJntFK]
master = Ik_FK_Hind_Reverse + '.ox' # Right leg
BlendJoints(ikJoints,fkJoints,skinJoints,master)

skinJoints=[L_frontToeJnt,L_frontAnkleJnt,L_frontKneeJnt,L_frontUpperKneeJnt,L_frontFemurJnt]
ikJoints=[L_frontToeJntIK,L_frontAnkleJntIK,L_frontKneeJntIK,L_frontUpperKneeJntIK,L_frontFemurJntIK]
fkJoints=[L_frontToeJntFK,L_frontAnkleJntFK,L_frontKneeJntFK,L_frontUpperKneeJntFK,L_frontFemurJntFK]
master= IkFkfrontRev +'.ox'
BlendJoints(ikJoints,fkJoints,skinJoints,master)

skinJoints=[R_frontToeJnt,R_frontAnkleJnt,R_frontKneeJnt,R_frontUpperKneeJnt,R_frontFemurJnt]
ikJoints=[R_frontToeJntIK,R_frontAnkleJntIK,R_frontKneeJntIK,R_frontUpperKneeJntIK,R_frontFemurJntIK]
fkJoints=[R_frontToeJntFK,R_frontAnkleJntFK,R_frontKneeJntFK,R_frontUpperKneeJntFK,R_frontFemurJntFK]
master= IkFkfrontRev +'.ox'
BlendJoints(ikJoints,fkJoints,skinJoints,master)

# Front femur must be connected to translations
def BlendJointsTranslate(ikJoints,fkJoints,skinJoints,master):
    count=0
    for e in skinJoints:
        blendr1=cmds.shadingNode('blendColors',asUtility=True,n='L_IKFK_switch_translate_1')
        cmds.connectAttr(ikJoints[count]+'.tx',blendr1+'.color1R')
        cmds.connectAttr(ikJoints[count]+'.ty',blendr1+'.color1G')
        cmds.connectAttr(ikJoints[count]+'.tz',blendr1+'.color1B')
        cmds.connectAttr(fkJoints[count]+'.tx',blendr1+'.color2R')
        cmds.connectAttr(fkJoints[count]+'.ty',blendr1+'.color2G')
        cmds.connectAttr(fkJoints[count]+'.tz',blendr1+'.color2B')
        cmds.connectAttr(blendr1+'.output.outputR',skinJoints[count]+'.tx')
        cmds.connectAttr(blendr1+'.output.outputG',skinJoints[count]+'.ty')
        cmds.connectAttr(blendr1+'.output.outputB',skinJoints[count]+'.tz')
        cmds.connectAttr(master,blendr1+'.blender')
        count+=1    

skinJoints=[L_frontFemurJnt]
ikJoints=[L_frontFemurJntIK]
fkJoints=[L_frontFemurJntFK]
master=IkFkfrontRev+'.ox' 
BlendJointsTranslate(ikJoints,fkJoints,skinJoints,master)

skinJoints=[R_frontFemurJnt]
ikJoints=[R_frontFemurJntIK]
fkJoints=[R_frontFemurJntFK]
BlendJointsTranslate(ikJoints,fkJoints,skinJoints,master)

# Set of skinning joints
skinJntSet = cmds.sets(L_hindToeJnt,R_hindToeJnt,L_hindAnkleJnt,R_hindAnkleJnt,L_hindKneeJnt,R_hindKneeJnt,
L_hindUpperKneeJnt,R_hindUpperKneeJnt,L_hindFemurJnt,R_hindFemurJnt,L_frontToeJnt,R_frontToeJnt,
L_frontAnkleJnt,R_frontAnkleJnt,L_frontKneeJnt,R_frontKneeJnt,L_frontUpperKneeJnt,R_frontUpperKneeJnt,
L_frontFemurJnt,R_frontFemurJnt,n='Skin_JNT_Set')

''' Create tail/spine module '''
# Meassure the distance between joints and get tail root placement
dist=cmds.createNode('distanceDimShape', n='TEMP_DELETE')
tailStart=cmds.xform(tailRootLoc,q=True,ws=True,rp=True)
tailEnd=cmds.xform(tailEndLoc,q=True,ws=True,rp=True)
cmds.setAttr(dist+'.endPoint',*(tailEnd))
cmds.setAttr(dist+'.startPoint',*(tailStart))
distance=cmds.getAttr(dist+'.distance')
cmds.delete(cmds.listRelatives(dist, p=True))

# Joints chain in the tail. TODO: Expose initialAmmountOfJoints in UI
initialAmmountOfJoints = 5
ammountOfJoints = initialAmmountOfJoints - 1
cmds.select(d=True)
tailRootJnt=cmds.joint(n='C_TailRoot_JNT')
while ammountOfJoints > 0:
    tailJnt=cmds.joint(n='C_Tail'+str(ammountOfJoints)+'_JNT') 
    ammountOfJoints-=1
cmds.select(tailRootJnt, hi=True)
tailJointChain=cmds.ls(sl=True)

# Calculate translation distance between each joint
ammountOfJoints = initialAmmountOfJoints - 1
distancePerJoint=distance/ammountOfJoints
for e in tailJointChain:
    cmds.setAttr(e+'.tz',-distancePerJoint) # TODO: Expose tail direction in UI. Set to - OR + depending on tail direction (left/right)
cmds.setAttr(tailRootJnt+'.tz',0)
cmds.rename(tailJointChain[-1],tailJointChain[-1]+'End') # Not going to skin the end joint of the joint chain
# Point constraintain the tail root joint to the tail root locator to avoid rotation influence being added to the joint
constraintaint=cmds.pointConstraint(tailRootLoc,tailJointChain[0])  

# Rotate joint to aim for the end of the chain
# Place the tail's joint chain in case modeller hadn't figured out that the tail needs to be modelled straight (-z)
tempcon=cmds.aimConstraint(tailEndLoc, tailRootJnt, aimVector=(0,0,-1)) 
rotation=cmds.getAttr(tailRootJnt+'.rx')
cmds.delete(tempcon)

cmds.parent(tailJointChain[1],w=True) # Parent the 2nd joint to the world => can change the root tail joint without affecting all the other joints
cmds.setAttr(tailRootJnt+'.rx',0)
cmds.setAttr(tailRootJnt+'.ry',0)
cmds.setAttr(tailRootJnt+'.rz',0)
cmds.parent(tailJointChain[1],tailRootJnt)
cmds.joint(e=True, zso=True, oj='xyz', secondaryAxisOrient='yup', ch=True) # Orient joint chain: y points up

# Create IK Spline solver from root to end of tail joint chain
IK_Tail_Handle=cmds.ikHandle(sol='ikSplineSolver', ns=4, n='C_TailSolver_IK', sj=tailRootJnt, ee=tailJointChain[-1]+'End')
IK_Handle_GRP=cmds.group(IK_Tail_Handle[0],IK_Tail_Handle[2], n='C_IK_TailSystem_GRP' ) # Effector is not grouped to stay at the end of joint chain
cmds.setAttr(IK_Handle_GRP+'.inheritsTransform',0) # For scalability
cmds.rename(IK_Tail_Handle[1], 'C_TailSolver_Effector')
cmds.rename(IK_Tail_Handle[2], 'C_TailSolver_Curve')

# Create clusters for the tail - needed to control spline. Create 3 controllers for the tails, 3 clusters controlling each third of the spline curve
cmds.select('C_TailSolver_Curve.cv[1:2]')
tailRootCluster=cmds.cluster( rel=True, n='Tail_Root_Cluster') # cls1
cmds.select('C_TailSolver_Curve.cv[3:4]')
tailMidCluster=cmds.cluster( rel=True, n='Tail_Mid_Cluster') # cls2_
cmds.select('C_TailSolver_Curve.cv[5:6]')
tailEndCluster=cmds.cluster( rel=True, n='Tail_End_Cluster') # cls3_

# Put each tail cluster into an offset group
cluster1_GRP=cmds.group(tailRootCluster, n='TailCluster1_Root_GRP')
cluster2_GRP=cmds.group(tailMidCluster, n='TailCluster2_Mid_GRP')
cluster3_GRP=cmds.group(tailEndCluster, n='TailCluster3_End_GRP')

# 1 left-over cv to be static in rig. take the root cv of curve & create a cluster on it with an offset group.
cmds.select('C_TailSolver_Curve.cv[0]')
cluster4Neutral=cmds.cluster( rel=True, n='C_Neutral_Cluster') # cls4
cluster4Neutral_GRP=cmds.group(cluster4Neutral, n='C_Cluster4_GRP')

# Group tail clusters to create IK hierarchy structure
cmds.parent(cluster1_GRP,cluster2_GRP,cluster3_GRP,cluster4Neutral_GRP,IK_Handle_GRP)

# Create controllers for the tail, scale them and freeze the transforms, lock scale so they can't be changed by animator
tail_CTRL_Root = cmds.circle( nr=(0,0,1), c=(0,0,0), n='C_TailRoot_CTRL') # tailCtl1
cmds.scale(distance/3,distance/3,distance/3)
cmds.makeIdentity(tail_CTRL_Root,apply=True,t=1,r=1,s=1,n=0)
lockScale(tail_CTRL_Root[0])
SetColorOverrideYellow(tail_CTRL_Root[0])
tail_CTRL_Root_GRP=cmds.group(tail_CTRL_Root, n='C_TailRoot_CTRL_GRP') # tailCtl1Grp

tail_CTRL_Mid=cmds.circle( nr=(0,0,1), c=(0,0,0), n='C_TailMid_CTRL') # tailCtl2
cmds.scale(distance/3,distance/3,distance/3)
cmds.makeIdentity(tail_CTRL_Mid,apply=True,t=1,r=1,s=1,n=0)
lockScale(tail_CTRL_Mid[0])
SetColorOverrideYellow(tail_CTRL_Mid[0])
tail_CTRL_Mid_GRP=cmds.group(tail_CTRL_Mid, n='C_TailMid_CTRL_GRP') # tailCtl2Grp

tail_CTRL_Point=cmds.circle( nr=(0,0,1), c=(0,0,0), n='C_TailPoint_CTRL') # tailCtl3
cmds.scale(distance/3,distance/3,distance/3)
cmds.makeIdentity(tail_CTRL_Point,apply=True,t=1,r=1,s=1,n=0)
lockScale(tail_CTRL_Point[0])
SetColorOverrideYellow(tail_CTRL_Point[0])
tail_CTRL_Point_GRP=cmds.group(tail_CTRL_Point, n='C_TailPoint_CTRL_GRP') # tailCtl3Grp

# Place tail controllers: in case tail is modelled at an angle, rotate controller's offset groups to point at the right direction
cmds.setAttr(tail_CTRL_Root_GRP+'.rx',rotation)
cmds.setAttr(tail_CTRL_Mid_GRP+'.rx',rotation)
cmds.setAttr(tail_CTRL_Point_GRP+'.rx',rotation)
clsXform=cmds.xform(tailRootCluster[1], piv=True, q=True)
cmds.setAttr(tail_CTRL_Root_GRP+'.tx',clsXform[0])
cmds.setAttr(tail_CTRL_Root_GRP+'.ty',clsXform[1])
cmds.setAttr(tail_CTRL_Root_GRP+'.tz',clsXform[2])
clsXform=cmds.xform(tailMidCluster[1], piv=True, q=True)
cmds.setAttr(tail_CTRL_Mid_GRP+'.tx',clsXform[0])
cmds.setAttr(tail_CTRL_Mid_GRP+'.ty',clsXform[1])
cmds.setAttr(tail_CTRL_Mid_GRP+'.tz',clsXform[2])
clsXform=cmds.xform(tailEndCluster[1], piv=True, q=True)
cmds.setAttr(tail_CTRL_Point_GRP+'.tx',clsXform[0])
cmds.setAttr(tail_CTRL_Point_GRP+'.ty',clsXform[1])
cmds.setAttr(tail_CTRL_Point_GRP+'.tz',clsXform[2])

# Connect tail clusters to their respective controllers 
cmds.parentConstraint(tail_CTRL_Root,tailRootCluster, mo=True, n='C_tailRoot_controller')
cmds.parentConstraint(tail_CTRL_Mid,tailMidCluster, mo=True, n='C_tailMid_controller')
cmds.parentConstraint(tail_CTRL_Point,tailEndCluster, mo=True, n='C_tailPoint_controller')

# Create tail FK controllers 
tail_FK_CTRL=cmds.curve(d=1, p=[(1,0,-1),(-1,0,-1),(-1,0,1),(1,0,1),(1,0,-1)], k=[0,1,2,3,4], n='C_Tail1_FK_CTRL')
cmds.scale(distance/4,distance/4,distance/4)
cmds.makeIdentity(tail_FK_CTRL,apply=True,t=1,r=1,s=1,n=0)
lockScale(tail_FK_CTRL)

tail_FK_CTRL_GRP=cmds.group(tail_FK_CTRL, n='C_Tail_FK_CTRL1_GRP')
tail_FK_CTRL2=cmds.curve(d=1, p=[(1,0,-1),(-1,0,-1),(-1,0,1),(1,0,1),(1,0,-1)], k=[0,1,2,3,4], n='C_Tail2_FK_CTRL')
cmds.scale(distance/4,distance/4,distance/4)
cmds.makeIdentity(tail_FK_CTRL2,apply=True,t=1,r=1,s=1,n=0)
lockScale(tail_FK_CTRL2)

tail_FK_CTRL2_GRP=cmds.group(tail_FK_CTRL2, n='C_Tail_FK_CTRL2_GRP')
rotation=cmds.getAttr(tail_CTRL_Root_GRP+'.rx')
cmds.setAttr(tail_FK_CTRL_GRP+'.rx',rotation)
cmds.setAttr(tail_FK_CTRL2_GRP+'.rx',rotation)
constraintaint=cmds.pointConstraint(tail_CTRL_Root,tail_FK_CTRL_GRP)
cmds.delete(constraintaint)
constraintaint=cmds.pointConstraint(tail_CTRL_Mid,tail_FK_CTRL2_GRP)
cmds.delete(constraintaint)

# Place pivot at tail root: pivot from the beginning of the joint chain they're supposed to influence (NOT from the independent clusters)
coordinate=cmds.xform(tailRootLoc, ws=True, t=True, q=True)
cmds.xform(tail_FK_CTRL, piv=(coordinate), ws=True)
cmds.parent(tail_FK_CTRL2_GRP, tail_FK_CTRL)
cmds.parent(tail_CTRL_Root_GRP, tail_FK_CTRL)
cmds.parent(tail_CTRL_Mid_GRP,tail_FK_CTRL2) # place 2nd FK controller at the middle of the tail
cmds.parent(tail_CTRL_Point_GRP, tail_FK_CTRL2)

# Group the tail elements
tailGRP=cmds.group(tailRootJnt, IK_Handle_GRP, tail_FK_CTRL_GRP, n='C_TailRig_GRP')
cmds.setAttr(IK_Handle_GRP+'.visibility', 0)

# To make tail module translatable: parentConstraint the neutral cluster (not influenced) to make tail follow the parent group and enable scaling
cmds.parentConstraint(tail_FK_CTRL, cluster4Neutral, mo=True)

# Tail twist when tail end IK controller rotates and no twist. 
# For tail rotate to be visually the same direction as the controller: use multiplyDivide node to multiply rotation by -1
mult=cmds.shadingNode('multiplyDivide', asUtility=True, n='C_TailTwist_ReverseValueRotation_Multiply')

# TODO: IF tail is rotating opposite controller, connect controller directly to the rotation, if NOT need to get a reversed reaction by *-1
cmds.setAttr(mult+'.input2X',-1)
cmds.connectAttr(tail_CTRL_Point[0]+'.rz',mult+'.input1X')
cmds.connectAttr(mult+'.outputX', IK_Tail_Handle[0]+'.twist')

''' create spine/spine module '''
# Measure the distance between joints and get spine root placement
dist=cmds.createNode('distanceDimShape', n='TEMP_DELETE')
spineStart=cmds.xform(hindPelvis,q=True,ws=True,rp=True)
spineEnd=cmds.xform(frontPelvis,q=True,ws=True,rp=True)
cmds.setAttr(dist+'.endPoint',*(spineEnd))
cmds.setAttr(dist+'.startPoint',*(spineStart))
distance=cmds.getAttr(dist+'.distance')
cmds.delete(cmds.listRelatives(dist, p=True))

# Joints in spine chain
initialAmmountOfJoints=8
ammountOfJoints=initialAmmountOfJoints-1
cmds.select(d=True)
spineRootJnt=cmds.joint(n='C_SpineRoot_JNT')
while ammountOfJoints > 0:
    spineJnt=cmds.joint(n='C_Spine'+str(ammountOfJoints)+'_JNT')
    ammountOfJoints-=1
cmds.select(spineRootJnt, hi=True)
spineJointChain=cmds.ls(sl=True)

# calculate translation distance between each joint...
ammountOfJoints=initialAmmountOfJoints-1
distancePerJoint=distance/ammountOfJoints
for e in spineJointChain:
    cmds.setAttr(e+'.tz',-distancePerJoint)
cmds.setAttr(spineRootJnt+'.tz',0)
cmds.rename(spineJointChain[-1],spineJointChain[-1]+'End')
constraint=cmds.pointConstraint(frontPelvis,spineJointChain[0])

# rotate joint to aim for the end of the chain...
tempcon=cmds.aimConstraint(hindPelvis,spineRootJnt, aimVector=(0,0,-1))
rotation=cmds.getAttr(spineRootJnt+'.rx')
cmds.delete(tempcon)
cmds.parent(spineJointChain[1],w=True)
cmds.setAttr(spineRootJnt+'.rx',0)
cmds.setAttr(spineRootJnt+'.ry',0)
cmds.setAttr(spineRootJnt+'.rz',0)
cmds.parent(spineJointChain[1],spineRootJnt)
cmds.joint(e=True, zso=True, oj='xyz', secondaryAxisOrient='yup', ch=True)

# create IK solver...
IKSpineHandle=cmds.ikHandle(sol='ikSplineSolver', ns=4, n='C_SpineSolver_IK', sj=spineRootJnt, ee=spineJointChain[-1]+'End')
IK_Handle_GRP=cmds.group(IKSpineHandle[0],IKSpineHandle[2], n='C_IK_SpineSystem_GRP' )
cmds.setAttr(IK_Handle_GRP+'.inheritsTransform',0)
cmds.rename(IKSpineHandle[1], 'C_SpineSolverEffector')
cmds.rename(IKSpineHandle[2], 'C_SpineSolverCurve')

# create clusters for the Spine...
cmds.select('C_SpineSolverCurve.cv[1:2]')
cluster_Spine_Root =cmds.cluster( rel=True, n='Spine_Root_Cluster') # cls1
cmds.select('C_SpineSolverCurve.cv[3:4]')
cluster_Spine_Mid =cmds.cluster( rel=True, n='Spine_Mid_Cluster') # cls2
cmds.select('C_SpineSolverCurve.cv[5:6]')
cluster_Spine_End=cmds.cluster( rel=True, n='Spine_End_Cluster') # cls3
cluster_Spine_Root_GRP=cmds.group(cluster_Spine_Root, n='Spine_Cluster_Root_GRP') # cls1Grp
cluster_Spine_Mid_GRP=cmds.group(cluster_Spine_Mid, n='Spine_Cluster_Mid_GRP') # cls2Grp
cluster_Spine_End_GRP=cmds.group(cluster_Spine_End, n='Spine_Cluster_End_GRP') # cls3Grp

# a left over cv to be static in rig...
cmds.select('C_SpineSolverCurve.cv[0]')
cluster_Neutral_Spine=cmds.cluster( rel=True, n='C_Neutral_Cluster') # cls4
cluster_Neutral_Spine_GRP = cmds.group(cluster_Neutral_Spine, n='C_Neutral_Cluster_GRP') # cls4Grp

# Group the spine clusters
cmds.parent(cluster_Spine_Root_GRP,cluster_Spine_Mid_GRP,cluster_Spine_End_GRP,cluster_Neutral_Spine_GRP,IK_Handle_GRP)

# Create controllers for the Spine
Spine_CTRL_1=cmds.circle( nr=(0,0,1), c=(0,0,0), n='C_Spine_Root_CTRL')
cmds.scale(distance/3,distance/3,distance/3)
cmds.makeIdentity(Spine_CTRL_1,apply=True,t=1,r=1,s=1,n=0)
lockScale(Spine_CTRL_1[0])
SetColorOverrideYellow(Spine_CTRL_1[0])
Spine_CTRL_1_GRP=cmds.group(Spine_CTRL_1, n='C_Spine_Root_CTRL_GRP')

Spine_CTRL_2=cmds.circle( nr=(0,0,1), c=(0,0,0), n='C_Spine_Mid_CTRL')
cmds.scale(distance/3,distance/3,distance/3)
cmds.makeIdentity(Spine_CTRL_2,apply=True,t=1,r=1,s=1,n=0)
lockScale(Spine_CTRL_2[0])
SetColorOverrideYellow(Spine_CTRL_2[0])
Spine_CTRL_2_GRP=cmds.group(Spine_CTRL_2, n='C_Spine_Mid_CTRL_GRP')

Spine_CTRL_3=cmds.circle( nr=(0,0,1), c=(0,0,0), n='C_Spine_Point_CTRL')
cmds.scale(distance/3,distance/3,distance/3)
cmds.makeIdentity(Spine_CTRL_3,apply=True,t=1,r=1,s=1,n=0)
lockScale(Spine_CTRL_3[0])
SetColorOverrideYellow(Spine_CTRL_3[0])
Spine_CTRL_3_GRP=cmds.group(Spine_CTRL_3, n='C_Spine_Point_CTRL_GRP')

# place controllers...
cmds.setAttr(Spine_CTRL_1_GRP+'.rx',rotation)
cmds.setAttr(Spine_CTRL_2_GRP+'.rx',rotation)
cmds.setAttr(Spine_CTRL_3_GRP+'.rx',rotation)
clsXform=cmds.xform(cluster_Spine_Root[1], piv=True, q=True)
cmds.setAttr(Spine_CTRL_1_GRP+'.tx',clsXform[0])
cmds.setAttr(Spine_CTRL_1_GRP+'.ty',clsXform[1])
cmds.setAttr(Spine_CTRL_1_GRP+'.tz',clsXform[2])
clsXform=cmds.xform(cluster_Spine_Mid[1], piv=True, q=True)
cmds.setAttr(Spine_CTRL_2_GRP+'.tx',clsXform[0])
cmds.setAttr(Spine_CTRL_2_GRP+'.ty',clsXform[1])
cmds.setAttr(Spine_CTRL_2_GRP+'.tz',clsXform[2])
clsXform=cmds.xform(cluster_Spine_End[1], piv=True, q=True)
cmds.setAttr(Spine_CTRL_3_GRP+'.tx',clsXform[0])
cmds.setAttr(Spine_CTRL_3_GRP+'.ty',clsXform[1])
cmds.setAttr(Spine_CTRL_3_GRP+'.tz',clsXform[2])

# connect spine controllers...
cmds.parentConstraint(Spine_CTRL_1,cluster_Spine_Root, mo=True, n='C_Spine_Root_Controller')
cmds.parentConstraint(Spine_CTRL_2,cluster_Spine_Mid, mo=True, n='C_Spine_Mid_Controller')
cmds.parentConstraint(Spine_CTRL_3,cluster_Spine_End, mo=True, n='C_Spine_Point_Controller')

# Spine FK controllers...
Spine_FK_CTRL1=cmds.curve(d=1, p=[(1,0,-1),(-1,0,-1),(-1,0,1),(1,0,1),(1,0,-1)], k=[0,1,2,3,4], n='C_Spine1_FK_CTRL')
cmds.scale(distance/4,distance/4,distance/4)
cmds.makeIdentity(Spine_FK_CTRL1,apply=True,t=1,r=1,s=1,n=0)
lockScale(Spine_FK_CTRL1)

Spine_FK_CTRL_GRP=cmds.group(Spine_FK_CTRL1, n='C_Spine_FK_CTRL1_GRP')
Spine_FK_CTRL2=cmds.curve(d=1, p=[(1,0,-1),(-1,0,-1),(-1,0,1),(1,0,1),(1,0,-1)], k=[0,1,2,3,4], n='C_Spine2_FK_CTRL')
cmds.scale(distance/4,distance/4,distance/4)
cmds.makeIdentity(Spine_FK_CTRL2,apply=True,t=1,r=1,s=1,n=0)
lockScale(Spine_FK_CTRL2)
Spine_FK_CTRL2_GRP=cmds.group(Spine_FK_CTRL2, n='C_Spine_FK_CTRL2_GRP')

rotation=cmds.getAttr(Spine_CTRL_1_GRP+'.rx')
cmds.setAttr(Spine_FK_CTRL_GRP+'.rx',rotation)
cmds.setAttr(Spine_FK_CTRL2_GRP+'.rx',rotation)
constraintaint=cmds.pointConstraint(Spine_CTRL_1,Spine_FK_CTRL_GRP)
cmds.delete(constraintaint)
constraintaint=cmds.pointConstraint(Spine_CTRL_2,Spine_FK_CTRL2_GRP)
cmds.delete(constraintaint)

# connect spine end to hind JNT...
cmds.parentConstraint(Spine_CTRL_1[0],Spine_CTRL_2_GRP, mo=True)
cmds.parentConstraint(Spine_CTRL_3[0],Spine_CTRL_2_GRP, mo=True)
cmds.parentConstraint(Spine_CTRL_1[0],frontPelvisJnt, mo=True)
cmds.parentConstraint(Spine_CTRL_3[0],hindPelvisJnt, mo=True)
cmds.parentConstraint(Spine_CTRL_3[0],tail_FK_CTRL_GRP, mo=True)

# master Spine controller...
Spine_Master_CTRL=cmds.curve(d=1, p=[(0.5,0.5,0.5),(0.5,0.5,-0.5),(-0.5,0.5,-0.5),(-0.5,-0.5,-0.5),(0.5,-0.5,-0.5),(0.5,0.5,-0.5),(-0.5,0.5,-0.5),(-0.5,0.5,0.5),(0.5,0.5,0.5),(0.5,-0.5,0.5),(0.5,-0.5,-0.5),(-0.5,-0.5,-0.5),(-0.5,-0.5,0.5),(0.5,-0.5,0.5),(-0.5,-0.5,0.5),(-0.5,0.5,0.5)], k=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],n='C_Spine_Master_CTRL')
cmds.scale(distance/4,distance/4,distance*1.5)
cmds.makeIdentity(Spine_Master_CTRL, apply=True, t=1, r=1, s=1, n=0)
Spine_Master_CTRL_GRP=cmds.group(Spine_Master_CTRL, n='C_Spine_Master_CTRL_GRP')
constraint=cmds.pointConstraint(Spine_FK_CTRL2, Spine_Master_CTRL_GRP)
cmds.delete(constraint)
dist=cmds.getAttr(Spine_Master_CTRL_GRP+'.ty')
cmds.setAttr(Spine_Master_CTRL_GRP+'.ty',dist*1.5)
cmds.parent(Spine_FK_CTRL2_GRP, Spine_FK_CTRL1)
cmds.parent(Spine_CTRL_1_GRP, Spine_FK_CTRL1)
cmds.parent(Spine_CTRL_2_GRP,Spine_FK_CTRL2)
cmds.parent(Spine_CTRL_3_GRP, Spine_FK_CTRL2)
cmds.parentConstraint(Spine_CTRL_1[0],cluster_Neutral_Spine, mo=True)

cmds.setAttr(IK_Handle_GRP+'.visibility',0)
Spine_GRP=cmds.group(IK_Handle_GRP, spineRootJnt, Spine_FK_CTRL_GRP, n='C_Spine_Rig_GRP')

''' Create neck/neck module '''
# Meassure the distance between joints and get neck root placement...
dist=cmds.createNode('distanceDimShape', n='TEMP_DELETE')
neckStart=cmds.xform(neckRoot,q=True,ws=True,rp=True)
neckEndPos=cmds.xform(neckEnd,q=True,ws=True,rp=True)
cmds.setAttr(dist+'.endPoint',*(neckEndPos))
cmds.setAttr(dist+'.startPoint',*(neckStart))
distance=cmds.getAttr(dist+'.distance')
cmds.delete(cmds.listRelatives(dist, p=True))

# Neck joints in chain: 8 by default
initialAmmountOfJoints=8
ammountOfJoints=initialAmmountOfJoints-1
cmds.select(d=True)
neckRootJnt=cmds.joint(n='C_Neck_Root_JNT')  # c_neck9_JNT
while ammountOfJoints > 0:
    neckJnt=cmds.joint(n='C_Neck'+str(ammountOfJoints)+'_JNT')
    ammountOfJoints-=1
cmds.select(neckRootJnt, hi=True)
neckJointChain=cmds.ls(sl=True)

# calculate translation distance between each joint...
ammountOfJoints=initialAmmountOfJoints-1
distancePerJoint=distance/ammountOfJoints
for e in neckJointChain:
    cmds.setAttr(e+'.tz',distancePerJoint)
cmds.setAttr(neckRootJnt+'.tz',0)
cmds.rename(neckJointChain[-1],neckJointChain[-1]+'End')
constraint=cmds.pointConstraint(neckRoot,neckJointChain[0])

# rotate joint to aim for the end of the chain...
tempcon=cmds.aimConstraint(neckEnd,neckRootJnt, aimVector=(0,0,1))
rotation=cmds.getAttr(neckRootJnt+'.rx')
cmds.delete(tempcon)
cmds.parent(neckJointChain[1],w=True)
cmds.setAttr(neckRootJnt+'.rx',0)
cmds.setAttr(neckRootJnt+'.ry',0)
cmds.setAttr(neckRootJnt+'.rz',0)
cmds.parent(neckJointChain[1],neckRootJnt)
cmds.joint(e=True, zso=True, oj='xyz', secondaryAxisOrient='yup', ch=True)

# create IK_ solver...
IK_Neck_Handle=cmds.ikHandle(sol='ikSplineSolver', ns=4, n='C_Neck_Solver_IK_', sj=neckRootJnt, ee=neckJointChain[-1]+'End')
IK_Handle_GRP=cmds.group(IK_Neck_Handle[0],IK_Neck_Handle[2], n='C_IK_NeckSystem_GRP' )
cmds.setAttr(IK_Handle_GRP+'.inheritsTransform',0)
cmds.rename(IK_Neck_Handle[1], 'C_Neck_Solver_Effector')
cmds.rename(IK_Neck_Handle[2], 'C_Neck_Solver_Curve')

# create clusters for the neck...
cmds.select('C_Neck_Solver_Curve.cv[1:2]')
NeckCluster1=cmds.cluster( rel=True, n='Neck_Root_Cluster') # cls1
cmds.select('C_Neck_Solver_Curve.cv[3:4]')
NeckCluster2=cmds.cluster( rel=True, n='Neck_Mid_Cluster') # cls2
cmds.select('C_Neck_Solver_Curve.cv[5:6]')
NeckCluster3=cmds.cluster( rel=True, n='Neck_End_Cluster') # cls3
NeckCluster1Grp=cmds.group(NeckCluster1, n='Neck_Cluster1_GRP')
NeckCluster2Grp=cmds.group(NeckCluster2, n='Neck_Cluster2_GRP')
NeckCluster3Grp=cmds.group(NeckCluster3, n='Neck_Cluster3_GRP')

# a left over cv to be static in rig...
cmds.select('C_Neck_Solver_Curve.cv[0]')
NeckNeutralCluster=cmds.cluster( rel=True, n='C_Neck_Neutral_Cluster')
NeckNeutralClusterGRP=cmds.group(NeckNeutralCluster, n='C_Neck_Neutral_Cluster_GRP') # cls4Grp

# group em...
cmds.parent(NeckCluster1Grp,NeckCluster2Grp,NeckCluster3Grp,NeckNeutralClusterGRP,IK_Handle_GRP)

# create controllers for the Neck...
Neck_CTRL_1=cmds.circle( nr=(0,0,1), c=(0,0,0), n='C_Neck_Root_CTRL')
cmds.scale(distance/3,distance/3,distance/3)
cmds.makeIdentity(Neck_CTRL_1,apply=True,t=1,r=1,s=1,n=0)
lockScale(Neck_CTRL_1[0])
SetColorOverrideYellow(Neck_CTRL_1[0])
Neck_CTRL_1_GRP=cmds.group(Neck_CTRL_1, n='C_Neck_Root_CTRL_GRP')

Neck_CTRL_2=cmds.circle( nr=(0,0,1), c=(0,0,0), n='C_Neck_Mid_CTRL')
cmds.scale(distance/3,distance/3,distance/3)
cmds.makeIdentity(Neck_CTRL_2,apply=True,t=1,r=1,s=1,n=0)
lockScale(Neck_CTRL_2[0])
SetColorOverrideYellow(Neck_CTRL_2[0])
Neck_CTRL_2_GRP=cmds.group(Neck_CTRL_2, n='C_Neck_Mid_CTRL_GRP')

Neck_CTRL_3=cmds.circle( nr=(0,0,1), c=(0,0,0), n='C_Neck_Point_CTRL')
cmds.scale(distance/3,distance/3,distance/3)
cmds.makeIdentity(Neck_CTRL_3,apply=True,t=1,r=1,s=1,n=0)
lockScale(Neck_CTRL_3[0])
SetColorOverrideYellow(Neck_CTRL_3[0])
Neck_CTRL_3_GRP=cmds.group(Neck_CTRL_3, n='C_Neck_Point_CTRL_GRP')

# place controllers...
cmds.setAttr(Neck_CTRL_1_GRP+'.rx',rotation)
cmds.setAttr(Neck_CTRL_2_GRP+'.rx',rotation)
cmds.setAttr(Neck_CTRL_3_GRP+'.rx',rotation)
clusterXform=cmds.xform(NeckCluster1[1], piv=True, q=True)
cmds.setAttr(Neck_CTRL_1_GRP+'.tx',clusterXform[0])
cmds.setAttr(Neck_CTRL_1_GRP+'.ty',clusterXform[1])
cmds.setAttr(Neck_CTRL_1_GRP+'.tz',clusterXform[2])
clusterXform=cmds.xform(NeckCluster2[1], piv=True, q=True)
cmds.setAttr(Neck_CTRL_2_GRP+'.tx',clusterXform[0])
cmds.setAttr(Neck_CTRL_2_GRP+'.ty',clusterXform[1])
cmds.setAttr(Neck_CTRL_2_GRP+'.tz',clusterXform[2])
clusterXform=cmds.xform(NeckCluster3[1], piv=True, q=True)
cmds.setAttr(Neck_CTRL_3_GRP+'.tx',clusterXform[0])
cmds.setAttr(Neck_CTRL_3_GRP+'.ty',clusterXform[1])
cmds.setAttr(Neck_CTRL_3_GRP+'.tz',clusterXform[2])

# connect neck controllers...
cmds.parentConstraint(Neck_CTRL_1,NeckCluster1, mo=True, n='C_Neck_Root_Controller')
cmds.parentConstraint(Neck_CTRL_2,NeckCluster2, mo=True, n='C_Neck_Mid_Controller')
cmds.parentConstraint(Neck_CTRL_3,NeckCluster3, mo=True, n='C_Neck_Point_controller')

# Neck FK controllers...
Neck_FK_CTRL1=cmds.curve(d=1, p=[(1,0,-1),(-1,0,-1),(-1,0,1),(1,0,1),(1,0,-1)], k=[0,1,2,3,4], n='C_Neck1_FK_CTRL')
cmds.scale(distance/4,distance/4,distance/4)
cmds.makeIdentity(Neck_FK_CTRL1,apply=True,t=1,r=1,s=1,n=0)
lockScale(Neck_FK_CTRL1)
Neck_FK_CTRL_GRP=cmds.group(Neck_FK_CTRL1, n='C_Neck_FK_CTRL1_GRP')
Neck_FK_CTRL2=cmds.curve(d=1, p=[(1,0,-1),(-1,0,-1),(-1,0,1),(1,0,1),(1,0,-1)], k=[0,1,2,3,4], n='C_Neck2_FK_CTRL')
cmds.scale(distance/4,distance/4,distance/4)
cmds.makeIdentity(Neck_FK_CTRL2,apply=True,t=1,r=1,s=1,n=0)
lockScale(Neck_FK_CTRL2)
Neck_FK_CTRL2_GRP=cmds.group(Neck_FK_CTRL2, n='C_Neck_FK_CTRL2_GRP')

rotation=cmds.getAttr(Neck_CTRL_1_GRP+'.rx')
cmds.setAttr(Neck_FK_CTRL_GRP+'.rx',rotation)
cmds.setAttr(Neck_FK_CTRL2_GRP+'.rx',rotation)
constraint=cmds.pointConstraint(Neck_CTRL_1,Neck_FK_CTRL_GRP)
cmds.delete(constraint)
constraint=cmds.pointConstraint(Neck_CTRL_2,Neck_FK_CTRL2_GRP)
cmds.delete(constraint)

# move neck root pivot and parent controllers...
coordinate=cmds.xform(neckRoot, ws=True, t=True, q=True)
cmds.xform(Neck_FK_CTRL1, piv=(coordinate), ws=True)
cmds.parent(Neck_FK_CTRL2_GRP, Neck_FK_CTRL1)
cmds.parent(Neck_CTRL_1_GRP, Neck_FK_CTRL1)
cmds.parent(Neck_CTRL_2_GRP,Neck_FK_CTRL2)
cmds.parent(Neck_CTRL_3_GRP, Neck_FK_CTRL2)

# cleanup...
cmds.setAttr(IK_Handle_GRP+'.visibility',0)

# neckGRP causes Warning: Cycle on 'C_Neck_Mid_CTRL.parentMatrix[0]' may not evaluate as expected. 
# Debug: cmds.cycleCheck('C_Neck_Mid_CTRL.parentMatrix[0]', list=True) 
neckGRP=cmds.group(neckRootJnt,IK_Handle_GRP,Neck_FK_CTRL_GRP, n='C_Neck_Rig_GRP') 

''' Create foot roll module '''
# L side Hind Foot Roll
cmds.select(d=True)
L_Hind_Ankle_Rotate=cmds.joint(n='L_Hind_Ankle_Rotate_JNT')
L_Hind_Heel_JNT=cmds.joint(n='L_Hind_HeelRoll_JNT')
L_Hind_Ball_JNT=cmds.joint(n='L_Hind_BallRoll_JNT')
L_Hind_Ankle_JNT=cmds.joint(n='L_Hind_AnkleRoll_JNT')
constraint = cmds.pointConstraint(L_hindAnkleJnt, L_Hind_Ankle_Rotate)
cmds.delete(constraint)
constraint=cmds.pointConstraint(L_hindToeJnt, L_Hind_Heel_JNT)
cmds.delete(constraint)

cmds.setAttr(L_Hind_Heel_JNT+'.tz',0)
constraint=cmds.pointConstraint(L_hindToeJnt, L_Hind_Ball_JNT)
cmds.delete(constraint)
constraint=cmds.pointConstraint(L_hindAnkleJnt, L_Hind_Ankle_JNT)
cmds.delete(constraint)

cmds.parent(L_IK[0], L_Hind_Ankle_JNT)
cmds.parent(L_IK_Toe[0], L_Hind_Ball_JNT)
coordinate=cmds.xform(L_Hind_Ankle_Rotate, ws=True, t=True, q=True)
cmds.xform(L_hindIKCtrl, piv=(coordinate), ws=True)
L_Hind_Heel_CTRL=cmds.circle(nr=(1,0,0), r=distance/4, n='L_Hind_Heel_CTRL')
L_Hind_Heel_CTRL_GRP=cmds.group(n='L_Hind_Heel_CTRL_GRP')
constraint=cmds.pointConstraint(L_Hind_Heel_JNT, L_Hind_Heel_CTRL[0])
cmds.delete(constraint)

L_Hind_ToeTip_CTRL=cmds.circle(nr=(1,0,0), r=distance/4, n='L_Hind_ToeTip_CTRL')
L_Hind_ToeTip_CTRL_GRP=cmds.group(n='L_Hind_ToeTip_CTRL_GRP')
constraint=cmds.pointConstraint(L_Hind_Ball_JNT, L_Hind_ToeTip_CTRL_GRP)
cmds.delete(constraint)

cmds.parent(L_Hind_ToeTip_CTRL_GRP, L_Hind_Heel_CTRL[0])
cmds.parentConstraint(L_Hind_Heel_CTRL[0], L_Hind_Heel_JNT, mo=True)
cmds.parentConstraint(L_Hind_ToeTip_CTRL[0], L_Hind_Ball_JNT, mo=True)
cmds.parent(L_Hind_Heel_CTRL_GRP, L_hindIKCtrl)
cmds.parentConstraint(L_hindIKCtrl, L_Hind_Ankle_Rotate, mo=True)
cmds.setAttr(L_Hind_Ankle_Rotate+'.visibility',0)

# R side Hind Foot Roll
cmds.select(d=True)
R_Hind_Ankle_Rotate=cmds.joint(n='R_Hind_Ankle_Rotate_JNT')
R_Hind_Heel_JNT=cmds.joint(n='R_Hind_HeelRoll_JNT')
R_Hind_Ball_JNT=cmds.joint(n='R_Hind_BallRoll_JNT')
R_Hind_Ankle_JNT=cmds.joint(n='R_Hind_AnkleRoll_JNT')
constraint = cmds.pointConstraint(R_hindAnkleJnt, R_Hind_Ankle_Rotate)
cmds.delete(constraint)
constraint=cmds.pointConstraint(R_hindToeJnt, R_Hind_Heel_JNT)
cmds.delete(constraint)

cmds.setAttr(R_Hind_Heel_JNT+'.tz',0)
constraint=cmds.pointConstraint(R_hindToeJnt, R_Hind_Ball_JNT)
cmds.delete(constraint)
constraint=cmds.pointConstraint(R_hindAnkleJnt, R_Hind_Ankle_JNT)
cmds.delete(constraint)

cmds.parent(R_IK[0], R_Hind_Ankle_JNT)
cmds.parent(R_IK_Toe[0], R_Hind_Ball_JNT)
coordinate=cmds.xform(R_Hind_Ankle_Rotate, ws=True, t=True, q=True)
cmds.xform(R_hindIKCtrl, piv=(coordinate), ws=True)
R_Hind_Heel_CTRL=cmds.circle(nr=(1,0,0), r=distance/4, n='R_Hind_Heel_CTRL')
R_Hind_Heel_CTRL_GRP=cmds.group(n='R_Hind_Heel_CTRL_GRP')
constraint=cmds.pointConstraint(R_Hind_Heel_JNT, R_Hind_Heel_CTRL[0])
cmds.delete(constraint)

R_Hind_ToeTip_CTRL=cmds.circle(nr=(1,0,0), r=distance/4, n='R_Hind_ToeTip_CTRL')
R_Hind_ToeTip_CTRL_GRP=cmds.group(n='R_Hind_ToeTip_CTRL_GRP')
constraint=cmds.pointConstraint(R_Hind_Ball_JNT, R_Hind_ToeTip_CTRL_GRP)
cmds.delete(constraint)

cmds.parent(R_Hind_ToeTip_CTRL_GRP, R_Hind_Heel_CTRL[0])
cmds.parentConstraint(R_Hind_Heel_CTRL[0], R_Hind_Heel_JNT, mo=True)
cmds.parentConstraint(R_Hind_ToeTip_CTRL[0], R_Hind_Ball_JNT, mo=True)
cmds.parent(R_Hind_Heel_CTRL_GRP, R_hindIKCtrl)
cmds.parentConstraint(R_hindIKCtrl, R_Hind_Ankle_Rotate, mo=True)
cmds.setAttr(R_Hind_Ankle_Rotate+'.visibility',0)

# L front leg foot roll
cmds.select(d=True)
L_Front_Ankle_Rotate=cmds.joint(n='l_frontAnkleRotate_JNT')
L_Front_Heel_JNT=cmds.joint(n='l_frontHeelRool_JNT')
L_Front_Ball_JNT=cmds.joint(n='l_frontBallRool_JNT')
L_Front_Ankle_JNT=cmds.joint(n='l_frontAnkleRool_JNT')
constraint=cmds.pointConstraint(L_frontAnkleJnt, L_Front_Ankle_Rotate)
cmds.delete(constraint)
constraint=cmds.pointConstraint(L_frontToeJnt, L_Front_Heel_JNT)
cmds.delete(constraint)
cmds.setAttr(L_Front_Heel_JNT+'.tz',0)
constraint=cmds.pointConstraint(L_frontToeJnt, L_Front_Ball_JNT)
cmds.delete(constraint)
constraint=cmds.pointConstraint(L_frontAnkleJnt, L_Front_Ankle_JNT)
cmds.delete(constraint)
cmds.parent(L_Front_IK[0], L_Front_Ankle_JNT)
cmds.parent(L_Front_Toe_IK[0], L_Front_Ball_JNT)
coordinate=cmds.xform(L_Front_Ankle_Rotate, ws=True, t=True, q=True)
cmds.xform(L_frontIKCtrl, piv=(coordinate), ws=True)
L_Front_Heel_CTRL=cmds.circle(nr=(1,0,0), r=distance/4, n='L_Front_Heel_CTRL')
L_Front_Heel_CTRL_GRP=cmds.group(n='L_Front_Heel_CTRL_GRP')
constraint=cmds.pointConstraint(L_Front_Heel_JNT, L_Front_Heel_CTRL[0])
cmds.delete(constraint)
L_Front_ToeTip_CTRL=cmds.circle(nr=(1,0,0), r=distance/4, n='L_Front_ToeTip_CTRL')
L_Front_ToeTip_CTRL_GRP=cmds.group(n='L_Front_ToeTip_CTRL_GRP')
constraint=cmds.pointConstraint(L_Front_Ball_JNT, L_Front_ToeTip_CTRL_GRP)
cmds.delete(constraint)
cmds.parent(L_Front_ToeTip_CTRL_GRP, L_Front_Heel_CTRL[0])
cmds.parentConstraint(L_Front_Heel_CTRL[0], L_Front_Heel_JNT, mo=True)
cmds.parentConstraint(L_Front_ToeTip_CTRL[0], L_Front_Ball_JNT, mo=True)
cmds.parent(L_Front_Heel_CTRL_GRP, L_frontIKCtrl)
cmds.parentConstraint(L_frontIKCtrl, L_Front_Ankle_Rotate, mo=True)
cmds.setAttr(L_Front_Ankle_Rotate+'.visibility',0)

# R front leg foot roll
cmds.select(d=True)
R_Front_Ankle_Rotate=cmds.joint(n='R_Front_Ankle_Rotate_JNT')
R_Front_Heel_JNT=cmds.joint(n='R_Front_Heel_Roll_JNT')
R_Front_Ball_JNT=cmds.joint(n='R_Front_Ball_Roll_JNT')
R_Front_Ankle_JNT=cmds.joint(n='R_frontAnkleRoll_JNT')
constraint=cmds.pointConstraint(R_frontAnkleJnt, R_Front_Ankle_Rotate)
cmds.delete(constraint)
constraint=cmds.pointConstraint(R_frontToeJnt, R_Front_Heel_JNT)
cmds.delete(constraint)
cmds.setAttr(R_Front_Heel_JNT+'.tz',0)
constraint=cmds.pointConstraint(R_frontToeJnt, R_Front_Ball_JNT)
cmds.delete(constraint)
constraint=cmds.pointConstraint(R_frontAnkleJnt, R_Front_Ankle_JNT)
cmds.delete(constraint)
cmds.parent(R_Front_IK[0], R_Front_Ankle_JNT)
cmds.parent(R_Front_Toe_IK[0], R_Front_Ball_JNT)
coordinate=cmds.xform(R_Front_Ankle_Rotate, ws=True, t=True, q=True)
cmds.xform(R_frontIKCtrl, piv=(coordinate), ws=True)
R_Front_Heel_CTRL=cmds.circle(nr=(1,0,0), r=distance/4, n='R_Front_Heel_CTRL')
R_Front_Heel_CTRL_GRP=cmds.group(n='R_Front_Heel_CTRL_GRP')
constraint=cmds.pointConstraint(R_Front_Heel_JNT, R_Front_Heel_CTRL[0])
cmds.delete(constraint)
R_Front_ToeTip_CTRL=cmds.circle(nr=(1,0,0), r=distance/4, n='R_Front_ToeTip_CTRL')
R_Front_ToeTip_CTRL_GRP=cmds.group(n='R_Front_ToeTip_CTRL_GRP')
constraint=cmds.pointConstraint(R_Front_Ball_JNT, R_Front_ToeTip_CTRL_GRP)
cmds.delete(constraint)
cmds.parent(R_Front_ToeTip_CTRL_GRP, R_Front_Heel_CTRL[0])
cmds.parentConstraint(R_Front_Heel_CTRL[0], R_Front_Heel_JNT, mo=True)
cmds.parentConstraint(R_Front_ToeTip_CTRL[0], R_Front_Ball_JNT, mo=True)
cmds.parent(R_Front_Heel_CTRL_GRP, R_frontIKCtrl)
cmds.parentConstraint(R_frontIKCtrl, R_Front_Ankle_Rotate, mo=True)
cmds.setAttr(R_Front_Ankle_Rotate+'.visibility',0)

roll_JNT_GRP=cmds.group(L_Front_Ankle_Rotate, R_Front_Ankle_Rotate, L_Hind_Ankle_Rotate, R_Hind_Ankle_Rotate, n='C_FootRoll_JNT_GRP')

# constraintaint front leg rotation ctrl to IK controller...
constraintPoint=cmds.parentConstraint(frontPelvisJnt, L_frontLeg_Rotation_GRP, mo=True)
cmds.parentConstraint(L_frontLeg_Rotation, L_frontFemurJntIK, mo=True)
cmds.parentConstraint(L_frontIKCtrl, L_frontLeg_Rotation_GRP, mo=True)
cmds.setAttr(constraintPoint[0] + '.L_Front_Foot_IK_CTRLW1', 0.3)

constraintPoint=cmds.parentConstraint(frontPelvisJnt, R_frontLeg_Rotation_GRP, mo=True)
cmds.parentConstraint(R_frontLeg_Rotation, R_frontFemurJntIK, mo=True)
cmds.parentConstraint(R_frontIKCtrl, R_frontLeg_Rotation_GRP, mo=True)
cmds.setAttr(constraintPoint[0] + '.R_Front_Foot_IK_CTRLW1', 0.3)


# nullify placement locators...
cmds.delete(mainLocGrp)

''' Cleanup '''
# Group body...
cmds.parent(Spine_GRP, Spine_Master_CTRL)
rigGRP=cmds.group(tailGRP,leg_CTRL_GRP,legSwitchGrp,Spine_Master_CTRL_GRP, neckGRP, n='C_Rig_GRP')
jntGRP=cmds.group(roll_JNT_GRP, hindPelvisJnt, frontPelvisJnt, tailRootJnt, spineRootJnt, neckRootJnt, n='C_JNT_GRP')

cmds.parent(rigGRP, jntGRP, subworldCtrl)
cmds.setAttr(L_hindFemurJntIK+'.visibility',0)
cmds.setAttr(R_hindFemurJntIK+'.visibility',0)
cmds.setAttr(L_frontFemurJntIK+'.visibility',0)
cmds.setAttr(R_frontFemurJntIK+'.visibility',0)

''' Stretchy spine '''
baseLoc = cmds.spaceLocator(n = 'baseSpine_LOC')
poseLoc = cmds.spaceLocator(n = 'poseSpine_LOC')
targetLoc = cmds.spaceLocator(n = 'targetSpine_LOC')
cmds.setAttr(baseLoc[0] + '.visibility',0)
cmds.setAttr(poseLoc[0] + '.visibility',0)
cmds.setAttr(targetLoc[0] + '.visibility',0)
cmds.parent(baseLoc, spineJointChain[0], r = True)
cmds.parent(targetLoc, hindPelvisJnt, r = True)
spineStretchGRP = cmds.group(baseLoc[0], poseLoc[0], targetLoc[0], n='C_SpineDistanceReader_GRP')
cmds.pointConstraint(Spine_CTRL_3[0], poseLoc[0], sk=('x', 'y'), mo = True)

dist = cmds.createNode('distanceDimShape', n = 'distanceMasterSpine')
cmds.connectAttr(baseLoc[0] + '.worldPosition[0]', dist + '.startPoint')
cmds.connectAttr(poseLoc[0] + '.worldPosition[0]', dist + '.endPoint')

dist2 = cmds.createNode('distanceDimShape', n = 'distancePoseSpine')
cmds.connectAttr(baseLoc[0] + '.worldPosition[0]', dist2 + '.startPoint')
cmds.connectAttr(targetLoc[0] + '.worldPosition[0]', dist2 + '.endPoint')

divide = cmds.shadingNode('multiplyDivide', asUtility = True, n = 'StretchSpine_DivideWithScale')
cmds.setAttr(divide + '.operation', 2)
cmds.connectAttr(dist + '.distance', divide + '.input1X')
cmds.connectAttr(dist2 + '.distance', divide + '.input2X')
cmds.addAttr(baseLoc[0], longName = 'output_value', at = 'enum', en = ('____'), max = 1, min = 0, k = True)
cmds.addAttr(baseLoc[0], longName='distance', at='float', k=True)
cmds.connectAttr(divide+'.outputX', baseLoc[0]+'.distance')

nonShape=cmds.listRelatives(dist, p=True)
cmds.setAttr(nonShape[0]+'.visibility', 0)
nonShape=cmds.rename(nonShape[0], 'distanceMaster_DST')
nonShape2=cmds.listRelatives(dist2, p=True)
cmds.setAttr(nonShape2[0]+'.visibility', 0)
nonShape2=cmds.rename(nonShape2[0], 'distancePose_DST')

for e in spineJointChain:
    try:
        cmds.connectAttr(baseLoc[0]+'.distance', e+'.scaleX')
    except:      
        print ("spine end jnt ignored")
cmds.parent(nonShape, nonShape2, spineStretchGRP)
cmds.parent(spineStretchGRP, Spine_GRP)
cmds.select(d=True) 