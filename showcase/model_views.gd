extends Node3D
## Renders one model from several angles (side, front, rear and three-quarter views, top) into a
## single contact sheet, for checking a model against reference photos:
##   <voxel godot exe> --path . res://showcase/model_views.tscn -- <output folder> <model> [scheme]
## Saves `<model>_views.png`.

const VIEWS := [
	# [yaw around the model in degrees (0 = looking at its left side), pitch in degrees]
	[0.0, 4.0], [-90.0, 4.0], [90.0, 4.0],
	[-40.0, 16.0], [140.0, 18.0], [0.0, 89.0],
]
const CELL := Vector2i(800, 450)


func _ready() -> void:
	var args := OS.get_cmdline_user_args()
	var out: String = args[0] if args.size() > 0 else "user://"
	var model: String = args[1] if args.size() > 1 else "uh60"
	var scheme: String = args[2] if args.size() > 2 else ""
	get_window().size = CELL
	var env := Environment.new()
	env.background_mode = Environment.BG_COLOR
	env.background_color = Color("c9cdd1")
	env.ambient_light_source = Environment.AMBIENT_SOURCE_COLOR
	env.ambient_light_color = Color("aab0b8")
	env.ambient_light_energy = 0.7
	env.tonemap_mode = Environment.TONE_MAPPER_FILMIC
	var world_env := WorldEnvironment.new()
	world_env.environment = env
	add_child(world_env)
	var sun := DirectionalLight3D.new()
	sun.rotation_degrees = Vector3(-55, -35, 0)
	sun.shadow_enabled = true
	add_child(sun)
	var fill := DirectionalLight3D.new()
	fill.rotation_degrees = Vector3(-20, 150, 0)
	fill.light_energy = 0.35
	add_child(fill)
	var ground := MeshInstance3D.new()
	var plane := PlaneMesh.new()
	plane.size = Vector2(80, 80)
	var mat := StandardMaterial3D.new()
	mat.albedo_color = Color("6f6d60")
	plane.material = mat
	ground.mesh = plane
	add_child(ground)
	var node := VehicleArt.instance(model, scheme)
	add_child(node)
	VehicleArt.spin_rotors(node, 0.03)
	for rotor_name in ["MainRotor", "TailRotor"]:  # blade shadows striping the hull hide detail
		var rotor := node.get_node_or_null(rotor_name)
		if rotor:
			for part in rotor.get_children():
				part.cast_shadow = GeometryInstance3D.SHADOW_CASTING_SETTING_OFF
	var size := VehicleArt.size_m(model)
	var centre := Vector3(0, size.y * 0.45, 0)
	var reach := maxf(size.z, size.x) * 0.5 + 0.4
	var camera := Camera3D.new()
	camera.fov = 40
	add_child(camera)
	camera.current = true
	var sheet := Image.create(CELL.x * 3, CELL.y * 2, false, Image.FORMAT_RGBA8)
	for i in VIEWS.size():
		var yaw := deg_to_rad(VIEWS[i][0])
		var pitch := deg_to_rad(VIEWS[i][1])
		# Fit the model's length across the frame's width.
		var dist := reach / (tan(deg_to_rad(camera.fov * 0.5)) * float(CELL.x) / CELL.y) + reach * 0.4
		var dir := Vector3(-cos(pitch) * cos(yaw), sin(pitch), cos(pitch) * sin(yaw))
		if VIEWS[i][1] > 80.0:
			camera.look_at_from_position(centre + Vector3(0, dist, 0), centre, Vector3.LEFT)
		else:
			camera.look_at_from_position(centre + dir * dist, centre)
		for f in 8:
			await get_tree().process_frame
		var img := get_viewport().get_texture().get_image()
		img.convert(Image.FORMAT_RGBA8)
		img.resize(CELL.x, CELL.y)
		sheet.blit_rect(img, Rect2i(Vector2i.ZERO, CELL), Vector2i((i % 3) * CELL.x, (i / 3) * CELL.y))
	var path := out.path_join("%s_views.png" % model)
	sheet.save_png(path)
	print("saved ", path)
	get_tree().quit()
