
# Blueprint Wiring (Minimal Playable)

- **BP_LauncherPawn**: mouse/touch drag backward → compute Dir & Power → Spawn `BP_Orb` → `AddImpulse`.
- **BP_Orb**: Simulate Physics true; OnHit with `BP_Bumper` → GameState.AddScore(10).
- **BP_Bumper**: Collision Sphere; OnHit by `BP_Orb` → bounce (physics handles) + call score.
- **BP_AetherGameState**: holds `Score`, `RoundThreshold`; broadcasts to UI.
- **WBP_Threshold**: bind a progress bar to Score/Threshold (turn green when >=1).
- **Speed Controls**: optional keys 1/2/3 to set `GlobalTimeDilation` 0.5/1/2.
