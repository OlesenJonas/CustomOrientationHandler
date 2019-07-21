bl_info = {
    "name": "Custom Orientation Handler",
    "description": "",
    "author": "Jonas Olesen",
    "category": "Edit",
    "blender": (2, 80, 0)
}

import bpy
from bpy.props import *


class CreateOri(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.add_ori"
    bl_label = "Add Orientation"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.object.mode == "EDIT"

    def execute(self, context):
        ori = bpy.context.scene.transform_orientation_slots
        custom = ori[0].custom_orientation
        if custom and custom.name == "addoncustom":
            print("delete last custom")
            bpy.ops.transform.delete_orientation()
        bpy.ops.transform.create_orientation(use=True,name="addoncustom")
        return {'FINISHED'}

class deleteOri(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.del_ori"
    bl_label = "Delete Orientation"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.object.mode == "EDIT"

    def execute(self, context):
        ori = bpy.context.scene.transform_orientation_slots
        custom = ori[0].custom_orientation
        if custom and custom.name == "addoncustom":
            print("delete last custom")
            bpy.ops.transform.delete_orientation()
        return {'FINISHED'}

addon_keymaps = []

def register():

    bpy.utils.register_class(CreateOri)
    bpy.utils.register_class(deleteOri)

    #add to keymap
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name='Mesh', space_type='EMPTY')
    kmi2 = km.keymap_items.new(deleteOri.bl_idname, 'D', 'PRESS', ctrl=True, shift=True,alt=True) #keybind for deleting 
    kmi = km.keymap_items.new(CreateOri.bl_idname, 'A', 'PRESS', ctrl=True, shift=True,alt=True) #keybind for adding
    addon_keymaps.append(km)


def unregister():
    bpy.utils.unregister_class(deleteOri)
    bpy.utils.unregister_class(CreateOri)

    wm = bpy.context.window_manager
    for km in addon_keymaps:
        wm.keyconfigs.addon.keymaps.remove(km)
    # delete Keymap
    del addon_keymaps[:]


if __name__ == "__main__":
    register()
