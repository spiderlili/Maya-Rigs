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

    @classmethod
    def create_display_layer(cls, name, members, reference=False):
        display_layer = cmds.createDisplayLayer(name=name, empty=True)
        if reference:
            cmds.setAttr("{0}.displayType".format(display_layer), 2) # 0 = normal, 1 = template, 2 = reference
        if members:
            cmds.editDisplayLayerMembers(display_layer, members, noRecurse=True)
        return display_layer
    
    @classmethod
    def create_and_assign_lambert_shader(cls, name, shape_node):
        shader = cmds.shadingNode("lambert", name=name, asShader=True)
        shader_shading_group = cmds.sets(name="{0}SG".format(shader), renderable=True, noSurfaceShader=True, empty=True)
        # Connect the outColor attribute from the shading node to the shader group’s surface shader attribute
        cls.connect_attr(shader, "outColor", shader_shading_group, "surfaceShader")
        cmds.sets([shape_node], edit=True, forceElement=shader_shading_group) # assign the material to the shapeNode
        return shader 

# TODO: this will expect transform_node to have >= 1 shape node which may not always be the case - add additional error checking, include support for the case where a transform node has > 1 shape node
    @classmethod
    def get_shape_from_transform(cls, transform_node):
        return cmds.listRelatives(transform_node, shapes=True, fullPath=True)[0]
    
class CurveLibrary():
    @classmethod
    def circle(cls, radius=1, name="circle_curve"):
        return cmds.circle(center=(0, 0, 0), normal=(0, 1, 0), radius=radius, name=name)[0]

    @classmethod
    def two_way_arrow(cls, name="two_way_arrow_curve"):
        return cmds.curve(degree=1, 
                          point=[(-1,0,-2),(-2,0,-2),(0,0,-4),(2,0,-2),(1,0,-2),(1,0,2),(2,0,2),(0,0,4),(-2,0,2),(-1,0,2),(-1,0,-2)], 
                          knot=[0,1,2,3,4,5,6,7,8,9,10], name=name)

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

        # Prevent the ball geometry from being selected by adding it to a reference display layer
        Helpers.create_display_layer("ball_geometry", [ball_geo], True)

    def create_ball(self, name, parent=None):
        ball_geo = cmds.sphere(pivot=(0,0,0), axis=(0,1,0), radius=1, name=name)[0]
        if parent: # Check if a parent has been set
            ball_geo = cmds.parent(ball_geo, parent)[0]
        self.create_ball_shader(ball_geo)
        return ball_geo
    
    def create_ball_shader(self, ball_geo):
        ball_shape = Helpers.get_shape_from_transform(ball_geo)
        ball_shader = Helpers.create_and_assign_lambert_shader("ballShader", ball_shape)
        return

    def create_ball_ctrl(self, name, parent = None):
        # Ball control's radius should be slightly bigger than the ball geometry's radius, get transform node name
        # ball_ctrl = CurveLibrary.circle(radius=1.5, name=name)
        ball_ctrl = CurveLibrary.two_way_arrow(name=name)

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