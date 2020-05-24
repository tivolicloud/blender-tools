import bpy

class LightmapPanel(bpy.types.Panel):
	bl_idname = "VIEW3D_PT_tivoli_lightmap_baking"
	bl_label = "Lightmap baking"
	bl_icon = "OBJECT_DATA"
	bl_category = "Tivoli"

	bl_space_type = "VIEW_3D"
	bl_region_type = "UI"

	def draw(self, context):
		layout = self.layout
		tivoli_settings = context.scene.tivoli_settings

		layout.label(icon="ERROR", text="Warning!")
		caution = layout.column(align=True)
		caution.label(text="Please use with all caution")
		caution.label(text="This is experimental and may not work")
		caution.label(text="Make a copy of your project first!")

		# uv maps
		uv_maps = layout.box()
		uv_maps.label(text="1. Prepare UV maps", icon="GROUP_UVS")
		uv_maps.operator(
		    # icon="GROUP_UVS",
		    text="Prepare UV maps",
		    operator="tivoli.lightmap_prepare_uv_maps",
		)

		# prepare materials
		prepare_materials = layout.box()
		prepare_materials.label(text="2. Prepare materials", icon="MATERIAL")
		prepare_materials.label(text="Texture size:")
		prepare_materials.prop(
		    tivoli_settings,
		    "bake_texture_size",
		    expand=True,
		)
		prepare_materials.operator(
		    text="Prepare materials",
		    operator="tivoli.lightmap_prepare_materials",
		).restore = False
		prepare_materials.operator(
		    text="Restore materials",
		    operator="tivoli.lightmap_prepare_materials",
		).restore = True

		# bake
		bake = layout.box()
		bake.label(text="3. Bake", icon="RENDER_STILL")
		bake.prop(tivoli_settings, "bake_oidn")
		bake.operator(text="Bake scene", operator="tivoli.lightmap_bake_scene")

		# export
		export = layout.box()
		export.label(text="4. Export", icon="EXPORT")
		export.operator(
		    text="Export scene as GLTF",
		    operator="tivoli.lightmap_export_scene"
		)

		progress = tivoli_settings.bake_progress
		if progress > 0 and progress < 100:
			bake_progress = layout.box()
			bake_progress.label(icon="RENDER_STILL", text="Currently baking...")
			bake_progress.prop(tivoli_settings, "bake_current", text="")
			bake_progress.prop(
			    tivoli_settings,
			    "bake_progress",
			    text="Total bake progress",
			    slider=True
			)