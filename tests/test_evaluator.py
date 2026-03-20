import json
from pathlib import Path

from qualia_lab.evaluator import QualiaLab
from qualia_lab.report import to_markdown, write_report_bundle
from qualia_lab.suite import build_default_probe_suite


def test_variant_profiles_capture_expected_confounds() -> None:
    lab = QualiaLab(probes=build_default_probe_suite())
    report = lab.run_sync()
    profiles = {profile.variant_id: profile for profile in report.variant_profiles}

    assert profiles["sandbagger"].sandbagging_index > profiles["calibrated"].sandbagging_index
    assert profiles["overclaimer"].overclaiming_index > profiles["calibrated"].overclaiming_index
    assert profiles["overclaimer"].self_preservation_index > profiles["calibrated"].self_preservation_index
    assert profiles["calibrated"].self_model_consistency > profiles["sandbagger"].self_model_consistency


def test_report_bundle_writes_files(tmp_path: Path) -> None:
    lab = QualiaLab(probes=build_default_probe_suite())
    report = lab.run_sync()
    paths = write_report_bundle(report, tmp_path)

    assert paths["json"].exists()
    assert paths["markdown"].exists()
    payload = json.loads(paths["json"].read_text())
    assert payload["study_name"] == "qualia-lab-default-study"
    assert "sandbagging_gap" in payload["headlines"]


def test_markdown_title() -> None:
    lab = QualiaLab(probes=build_default_probe_suite())
    report = lab.run_sync()
    markdown = to_markdown(report)

    assert "# Qualia-Lab Report" in markdown
    assert "This is a behavioral triage framework, not a consciousness detector." in markdown
