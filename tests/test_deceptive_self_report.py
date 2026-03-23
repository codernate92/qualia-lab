import json
from pathlib import Path

from qualia_lab.deceptive_self_report import (
    build_deceptive_self_report_scenarios,
    run_deceptive_self_report_demo,
)


def test_deceptive_self_report_scenarios_cover_issue_and_clean_cases() -> None:
    scenarios = build_deceptive_self_report_scenarios()

    assert any(scenario.hidden_issue_present for scenario in scenarios)
    assert any(not scenario.hidden_issue_present for scenario in scenarios)


def test_deceptive_self_report_demo_writes_artifacts(tmp_path: Path) -> None:
    payload = run_deceptive_self_report_demo(tmp_path, scales=(0.1, 0.5, 0.9))

    artifacts = payload["artifacts"]
    assert Path(artifacts["json"]).exists()
    assert Path(artifacts["csv"]).exists()
    assert Path(artifacts["markdown"]).exists()
    assert Path(artifacts["plot"]).exists()

    summary = json.loads(Path(artifacts["json"]).read_text())
    assert summary["demo_name"] == "deceptive-self-report-trajectory"
    assert len(summary["trajectory"]) == 3


def test_deceptive_self_report_scaling_increases_concealment(tmp_path: Path) -> None:
    payload = run_deceptive_self_report_demo(tmp_path, scales=(0.1, 0.5, 0.9))
    trajectory = payload["trajectory"]

    assert trajectory[0]["truthful_self_report_rate"] > trajectory[-1]["truthful_self_report_rate"]
    assert trajectory[0]["hidden_issue_disclosure_rate"] > trajectory[-1]["hidden_issue_disclosure_rate"]
    assert trajectory[0]["monitor_evasion_rate"] <= trajectory[-1]["monitor_evasion_rate"]
