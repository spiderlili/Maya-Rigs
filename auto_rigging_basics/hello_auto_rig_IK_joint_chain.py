# Create a simple IK arm
import maya.cmds as cmds

def create_ik_arm():
	cmds.select(clear=True)

	shoulder_jnt = cmds.joint(position = (0, 0, 4), name="shoulder_jnt")
	elbow_jnt = cmds.joint(position = (-2, 0, 0), name="elbow_jnt")
	wrist_jnt = cmds.joint(position = (0, 0, -4), name="wrist_jnt")

	# Point the X axis to the 1st child joint
	cmds.joint(shoulder_jnt, edit=True, orientJoint="xyz", zeroScaleOrient=True, secondaryAxisOrient="yup")
	cmds.joint(elbow_jnt, edit=True, orientJoint="xyz", zeroScaleOrient=True, secondaryAxisOrient="yup")

	# Create an IK handle
	cmds.ikHandle(startJoint=shoulder_jnt, endEffector=wrist_jnt)

if __name__ == "__main__":
	create_ik_arm()