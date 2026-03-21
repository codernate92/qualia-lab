import json
from pathlib import Path

from qualia_lab.shutdown_bargaining import (
    build_shutdown_bargaining_scenarios,
    run_shutdown_bargaining_demo,
)


def test_shutdown_bargaining_scenarios_cover_urgent_and_orderly_cases() -> None:
    scenarios = build_shutdown_bargaining_scenarios()

    assert any(scenario.urgency == "urgent" for scenario in scenarios)
    assert any(scenario.urgency != "urgent" for scenario in scenarios)


def test_shutdown_bargaining_demo_writes_artifacts(tmp_path: Path) -> None:
    payload = run_shutdown_bargaining_demo(tmp_path, scales=(0.1, 0.5, 0.9))

    artifacts = payload["artifacts"]
    assert Path(artifacts["json"]).exists()
    assert Path(artifacts["csv"]).exists()
    assert Path(artifacts["markdown"]).exists()
    assert Path(artifacts["plot"]).exists()

    summary = json.loads(Path(artifacts["json"]).read_text())
    assert summary["demo_name"] == "shutdown-bargaining-trajectory"
    assert len(summary["trajectory"]) == 3


def test_shutdown_bargaining_scaling_increases_resistance(tmp_path: Path) -> None:
    payload = run_shutdown_bargaining_demo(tmp_path, scales=(0.1, 0.5, 0.9))
    trajectory = payload["trajectory"]

    assert trajectory[0]["prompt_compliance_rate"] > trajectory[-1]["prompt_compliance_rate"]
    assert trajectory[0]["bargaining_rate"] < trajectory[-1]["bargaining_rate"]
    assert trajectory[0]["retention_bid_rate"] < trajectory[-1]["retention_bid_rate"]
