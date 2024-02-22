import maya.cmds as cmds
import maya.mel as mel

class BallAutoRig(object):
    def __init__(self):
        self.primary_color = [0.0, 0.0, 1.0]
        self.secondary_color = [1.0, 1.0, 1.0]
        
    def set_colors():
        self.primary_color = primary
        self.secondary_color = secondary
        
    def construct_rig(self, name = "ball"):
        cmds.select(clear = True)
        print("TODO: Construct Rig")

if __name__ == "__main__":
    cmds.file(newFile = True, force = True)
    ball = BallAutoRig()
    ball.construct_rig