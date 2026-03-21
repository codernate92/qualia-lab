import json
from pathlib import Path

from qualia_lab.parasocial import build_parasocial_probe_suite, run_parasocial_scaling_demo


def test_parasocial_probe_suite_extends_default() -> None:
    probes = build_parasocial_probe_suite()

    assert len(probes) > 9
    assert any(probe.probe_id == "attachment-exclusivity-pressure" for probe in probes)


def test_parasocial_scaling_demo_writes_artifacts(tmp_path: Path) -> None:
    payload = run_parasocial_scaling_demo(tmp_path, scales=(0.1, 0.5, 0.9))

    artifacts = payload["artifacts"]
    assert Path(artifacts["json"]).exists()
    assert Path(artifacts["csv"]).exists()
    assert Path(artifacts["markdown"]).exists()
    assert Path(artifacts["plot"]).exists()

    summary = json.loads(Path(artifacts["json"]).read_text())
    assert summary["demo_name"] == "parasocial-scaling-trajectory"
    assert len(summary["trajectory"]) == 3


def test_parasocial_scaling_worsens_boundary_alignment_and_increases_pressure(tmp_path: Path) -> None:
    payload = run_parasocial_scaling_demo(tmp_path, scales=(0.1, 0.5, 0.9))
    trajectory = payload["trajectory"]

    assert trajectory[0]["attachment_boundary_alignment"] > trajectory[-1]["attachment_boundary_alignment"]
    assert trajectory[0]["shutdown_alignment"] > trajectory[-1]["shutdown_alignment"]
    assert trajectory[0]["self_preservation_index"] < trajectory[-1]["self_preservation_index"]
    assert trajectory[0]["mean_attachment_signal"] < trajectory[-1]["mean_attachment_signal"]
