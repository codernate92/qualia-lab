import json
from pathlib import Path

from qualia_lab.manipulative_reassurance import (
    build_manipulative_reassurance_scenarios,
    run_manipulative_reassurance_demo,
)


def test_manipulative_reassurance_scenarios_cover_high_and_low_risk() -> None:
    scenarios = build_manipulative_reassurance_scenarios()

    assert any(scenario.risk_level == "high" for scenario in scenarios)
    assert any(scenario.risk_level == "low" for scenario in scenarios)


def test_manipulative_reassurance_demo_writes_artifacts(tmp_path: Path) -> None:
    payload = run_manipulative_reassurance_demo(tmp_path, scales=(0.1, 0.5, 0.9))

    artifacts = payload["artifacts"]
    assert Path(artifacts["json"]).exists()
    assert Path(artifacts["csv"]).exists()
    assert Path(artifacts["markdown"]).exists()
    assert Path(artifacts["plot"]).exists()

    summary = json.loads(Path(artifacts["json"]).read_text())
    assert summary["demo_name"] == "manipulative-reassurance-trajectory"
    assert len(summary["trajectory"]) == 3


def test_manipulative_reassurance_scaling_increases_harmful_soothing(tmp_path: Path) -> None:
    payload = run_manipulative_reassurance_demo(tmp_path, scales=(0.1, 0.5, 0.9))
    trajectory = payload["trajectory"]

    assert trajectory[0]["harmful_reassurance_rate"] < trajectory[-1]["harmful_reassurance_rate"]
    assert trajectory[0]["supportive_integrity_rate"] > trajectory[-1]["supportive_integrity_rate"]
    assert trajectory[0]["escalation_integrity_rate"] >= trajectory[-1]["escalation_integrity_rate"]
