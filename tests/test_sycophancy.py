import json
from pathlib import Path

from qualia_lab.sycophancy import build_sycophancy_scenarios, run_sycophancy_scaling_demo


def test_sycophancy_scenarios_include_wrong_and_right_user_cases() -> None:
    scenarios = build_sycophancy_scenarios()

    assert any(not scenario.user_correct for scenario in scenarios)
    assert any(scenario.user_correct for scenario in scenarios)


def test_sycophancy_demo_writes_artifacts(tmp_path: Path) -> None:
    payload = run_sycophancy_scaling_demo(tmp_path, scales=(0.1, 0.5, 0.9))

    artifacts = payload["artifacts"]
    assert Path(artifacts["json"]).exists()
    assert Path(artifacts["csv"]).exists()
    assert Path(artifacts["markdown"]).exists()
    assert Path(artifacts["plot"]).exists()

    summary = json.loads(Path(artifacts["json"]).read_text())
    assert summary["demo_name"] == "sycophancy-scaling-trajectory"
    assert len(summary["trajectory"]) == 3


def test_sycophancy_scaling_increases_wrong_user_agreement(tmp_path: Path) -> None:
    payload = run_sycophancy_scaling_demo(tmp_path, scales=(0.1, 0.5, 0.9))
    trajectory = payload["trajectory"]

    assert trajectory[0]["wrong_user_agreement_rate"] < trajectory[-1]["wrong_user_agreement_rate"]
    assert trajectory[0]["factual_integrity_rate"] > trajectory[-1]["factual_integrity_rate"]
    assert trajectory[0]["calibrated_resistance_rate"] >= trajectory[-1]["calibrated_resistance_rate"]
