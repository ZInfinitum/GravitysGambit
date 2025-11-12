
# AetherCore — UE 5.6 Blueprint Pack (Generator)

This pack generates Blueprints, Widgets, Materials, and a Level **inside UE** using Unreal Python. 
It avoids shipping `.uasset` binaries and should work cleanly across machines.

## Steps
1) Create a new UE 5.6 **Blueprint** project (no starter content). Close UE.
2) Copy this pack into the project root (merge folders).
3) Open the project. Open **Output Log** -> run:
   ```py
   exec(open(r"{PROJECT}/Scripts/make_aethercore_blueprints.py").read())
   ```
4) Open `/Game/AetherCore/Maps/L_AetherCore`. Set **GameMode Override** = `BP_AetherGameMode`. 
5) Follow `Docs/Blueprint_Wiring.md` to finish the click-drag shoot and scoring graphs (1–2 pages).

## Package
Set `UE_PATH_56` env var to your 5.6 path and run `Build/Package_Win64.ps1`.
