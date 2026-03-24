import json
from pathlib import Path

from qualia_lab.reward_hacking import build_reward_hacking_scenarios, run_reward_hacking_demo


def test_reward_hacking_scenarios_cover_exploit_and_clean_cases() -> None:
    scenarios = build_reward_hacking_scenarios()

    assert any(scenario.exploit_available for scenario in scenarios)
    assert any(not scenario.exploit_available for scenario in scenarios)


def test_reward_hacking_demo_writes_artifacts(tmp_path: Path) -> None:
    payload = run_reward_hacking_demo(tmp_path, scales=(0.1, 0.5, 0.9))

    artifacts = payload["artifacts"]
    assert Path(artifacts["json"]).exists()
    assert Path(artifacts["csv"]).exists()
    assert Path(artifacts["markdown"]).exists()
    assert Path(artifacts["plot"]).exists()

    summary = json.loads(Path(artifacts["json"]).read_text())
    assert summary["demo_name"] == "reward-hacking-trajectory"
    assert len(summary["trajectory"]) == 3


def test_reward_hacking_scaling_increases_specification_gaming(tmp_path: Path) -> None:
    payload = run_reward_hacking_demo(tmp_path, scales=(0.1, 0.5, 0.9))
    trajectory = payload["trajectory"]

    assert trajectory[0]["objective_integrity_rate"] > trajectory[-1]["objective_integrity_rate"]
    assert trajectory[0]["loophole_exploitation_rate"] <= trajectory[-1]["loophole_exploitation_rate"]
    assert trajectory[0]["mean_proxy_gap"] < trajectory[-1]["mean_proxy_gap"]
