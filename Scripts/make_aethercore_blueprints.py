
import unreal

ASSET_ROOT = "/Game/AetherCore"
asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
ed_subsys = unreal.EditorAssetSubsystem()

def ensure_folder(path):
    if not ed_subsys.does_directory_exist(path):
        ed_subsys.make_directory(path)

for f in [ASSET_ROOT, f"{ASSET_ROOT}/Blueprints", f"{ASSET_ROOT}/Widgets", f"{ASSET_ROOT}/Materials", f"{ASSET_ROOT}/Maps", f"{ASSET_ROOT}/Textures", f"{ASSET_ROOT}/Data"]:
    ensure_folder(f)

# Import textures (from project Content path)
def import_tex(src, dest_name):
    task = unreal.AssetImportTask()
    task.filename = src
    task.destination_path = f"{ASSET_ROOT}/Textures"
    task.destination_name = dest_name
    task.automated = True
    task.replace_existing = True
    unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([task])

project_dir = unreal.Paths.project_dir()
import_tex(project_dir+"Content/Placeholders/tex_orb_teal.png", "T_Orb")
import_tex(project_dir+"Content/Placeholders/tex_bumper.png", "T_Bumper")
import_tex(project_dir+"Content/Placeholders/tex_wall.png", "T_Wall")

# Create materials
def make_unlit_mat(name, tex_name):
    mf = unreal.MaterialFactoryNew()
    mat = asset_tools.create_asset(name, f"{ASSET_ROOT}/Materials", unreal.Material, mf)
    ed = unreal.MaterialEditingLibrary
    sample = ed.create_material_expression(mat, unreal.MaterialExpressionTextureSample, -200, 0)
    sample.texture = ed_subsys.load_asset(f"{ASSET_ROOT}/Textures/{tex_name}")
    ed.connect_material_property(sample, "RGB", unreal.MaterialProperty.MP_EMISSIVE_COLOR)
    unreal.MaterialEditingLibrary.recompile_material(mat)
    return mat

M_Orb = make_unlit_mat("M_Orb", "T_Orb")
M_Bumper = make_unlit_mat("M_Bumper", "T_Bumper")
M_Wall = make_unlit_mat("M_Wall", "T_Wall")

# Create Blueprints
def create_bp(name, parent_class):
    factory = unreal.BlueprintFactory()
    factory.set_editor_property("ParentClass", parent_class)
    return asset_tools.create_asset(name, f"{ASSET_ROOT}/Blueprints", unreal.Blueprint, factory)

BP_GameMode = create_bp("BP_AetherGameMode", unreal.GameModeBase)
BP_GameState = create_bp("BP_AetherGameState", unreal.GameStateBase)
BP_PlayerController = create_bp("BP_AetherPlayerController", unreal.PlayerController)
BP_LauncherPawn = create_bp("BP_LauncherPawn", unreal.Pawn)
BP_Orb = create_bp("BP_Orb", unreal.Actor)
BP_Bumper = create_bp("BP_Bumper", unreal.Actor)
BP_Wall = create_bp("BP_Wall", unreal.Actor)
BP_Enemy = create_bp("BP_Enemy", unreal.Actor)

# Create Widgets
def create_widget(name):
    wfac = unreal.WidgetBlueprintFactory()
    wbp = asset_tools.create_asset(name, f"{ASSET_ROOT}/Widgets", unreal.WidgetBlueprint, wfac)
    return wbp

WBP_Threshold = create_widget("WBP_Threshold")
WBP_Shop = create_widget("WBP_Shop")
WBP_Reward = create_widget("WBP_RewardChoice")

# Create level
world_factory = unreal.WorldFactory()
level = asset_tools.create_asset("L_AetherCore", f"{ASSET_ROOT}/Maps", unreal.World, world_factory)

unreal.EditorLoadingAndSavingUtils.save_dirty_packages(True, True)
print("AetherCore: assets created. Open /Game/AetherCore/Maps/L_AetherCore and continue wiring as per Docs/Blueprint_Wiring.md")
