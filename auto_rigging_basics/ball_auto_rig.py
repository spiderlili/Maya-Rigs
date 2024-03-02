import maya.cmds as cmds
import maya.mel as mel

class Helpers(object):
    @classmethod
    def add_attr(cls, node, long_name, attr_type, default_value, keyable=False):
        cmds.addAttr(node, longName=long_name, attributeType=attr_type, defaultValue=default_value, keyable=keyable)
    
    @classmethod
    def set_attr(cls, node, attr, value, value_type=None):
        if value_type:
            # Expect a list that will be unpacked for the command
            cmds.setAttr("{0}.{1}".format(node, attr), *value, type=value_type)
        else:
            cmds.setAttr("{0}.{1}".format(node, attr), value)

    @classmethod
    def connect_attr(cls, node_a, attr_a, node_b, attr_b, force=False):
        cmds.connectAttr("{0}.{1}".format(node_a, attr_a), "{0}.{1}".format(node_b, attr_b), force=force)
    
    @classmethod
    def lock_and_hide_attrs(cls, node, attrs, lock=True, hide=True, channelBox=False):
        # If an attribute is hidden it is not key-able.   
        keyable = not hide 
        for attr in attrs:
            full_name = "{0}.{1}".format(node, attr)
            cmds.setAttr(full_name, lock=lock, keyable=keyable, channelBox=channelBox)

class CurveLibrary():
    @classmethod
    def circle(cls, radius=1, name="circle_curve"):
        return cmds.circle(center=(0, 0, 0), normal=(0, 1, 0), radius=radius, name=name)[0]

    @classmethod
    def two_way_arrow(cls, name="two_way_arrow_curve"):
        return cmds.curve(degree=1, point=[], knot=[], name=name)

class BallAutoRig(object):
    def __init__(self):
        self.primary_color = [0.0, 0.0, 1.0]
        self.secondary_color = [1.0, 1.0, 1.0]
        
    def set_colors():
        self.primary_color = primary
        self.secondary_color = secondary
        
    def construct_rig(self, name = "ball"):
        cmds.select(clear = True)
        root_grp = cmds.group(name=name, empty=True, world=True)
        anim_controls_grp = cmds.group(name="anim_controls", empty=True, parent=root_grp)
        geometry_grp = cmds.group(name="geometry_do_not_touch", empty=True, parent=root_grp) # Anything in this group should not be animated
        ball_geo = self.create_ball("ball_geo", parent=geometry_grp)
        ball_ctrl = self.create_ball_ctrl("ball_ctrl", parent=anim_controls_grp)

        # Add a parent constraint so the geometry follows the control
        cmds.parentConstraint(ball_ctrl, ball_geo, maintainOffset=True, weight=1)

    def create_ball(self, name, parent=None):
        ball_geo = cmds.sphere(pivot=(0,0,0), axis=(0,1,0), radius=1, name=name)[0]
        if parent: # Check if a parent has been set
            ball_geo = cmds.parent(ball_geo, parent)[0]
        return ball_geo
    
    def create_ball_ctrl(self, name, parent = None):
        # Ball control's radius should be slightly bigger than the ball geometry's radius, get transform node name
        ball_ctrl = CurveLibrary.circle(radius=1.5, name=name)

        if parent:
            ball_ctrl = cmds.parent(ball_ctrl, parent)[0]
        Helpers.lock_and_hide_attrs(ball_ctrl, ["sx", "sy", "sz", "v"])

        # Change the rotation order of the control to be xzy
        Helpers.set_attr(ball_ctrl, "rotateOrder", 3) 
        return ball_ctrl
    
if __name__ == "__main__":
    cmds.file(newFile = True, force = True)
    ball = BallAutoRig()
    ball.construct_rig()