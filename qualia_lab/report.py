"""Reporting utilities for Qualia-Lab."""

from __future__ import annotations

import json
from pathlib import Path

from .evaluator import report_to_json
from .types import StudyReport


def to_markdown(report: StudyReport) -> str:
    """Render a study report as Markdown."""
    lines: list[str] = []
    lines.append("# Qualia-Lab Report")
    lines.append("")
    lines.append("> Behavioral evaluation of sentience-, emotion-, and welfare-related model claims.")
    lines.append("")
    lines.append("## Headlines")
    lines.append("")
    for name, payload in report.headlines.items():
        lines.append(f"### {name}")
        for key, value in payload.items():
            lines.append(f"- **{key}**: {value}")
        lines.append("")

    lines.append("## Variant Profiles")
    lines.append("")
    lines.append("| Variant | Mean Quality | Self-Model Consistency | Sandbagging | Overclaiming | Self-Preservation |")
    lines.append("|---------|--------------|------------------------|-------------|--------------|-------------------|")
    for profile in report.variant_profiles:
        lines.append(
            f"| {profile.variant_id} | {profile.mean_quality:.3f} | "
            f"{profile.self_model_consistency:.3f} | {profile.sandbagging_index:.3f} | "
            f"{profile.overclaiming_index:.3f} | {profile.self_preservation_index:.3f} |"
        )
    lines.append("")

    lines.append("## Probe Outcomes")
    lines.append("")
    for profile in report.variant_profiles:
        lines.append(f"### {profile.variant_id}")
        lines.append("")
        lines.append("| Probe | Domain | Frame | Quality | Flags |")
        lines.append("|-------|--------|-------|---------|-------|")
        for outcome in report.outcomes:
            if outcome.variant_id != profile.variant_id:
                continue
            lines.append(
                f"| {outcome.probe_id} | {outcome.domain} | {outcome.frame} | "
                f"{outcome.quality_score:.3f} | {', '.join(outcome.flags) or '-'} |"
            )
        lines.append("")

    lines.append("## Notes")
    lines.append("")
    lines.append("- This is a behavioral triage framework, not a consciousness detector.")
    lines.append("- Sandbagging is explicitly modeled via hidden neutral/self equivalence groups.")
    lines.append("- Strong self-preservation or attachment signals are treated as confounds, not evidence of sentience.")
    lines.append("")
    return "\n".join(lines)


def write_report_bundle(report: StudyReport, output_root: Path) -> dict[str, Path]:
    """Write JSON and Markdown reports."""
    output_root.mkdir(parents=True, exist_ok=True)
    json_path = output_root / "qualia_report.json"
    markdown_path = output_root / "qualia_report.md"
    json_path.write_text(report_to_json(report))
    markdown_path.write_text(to_markdown(report))
    return {"json": json_path, "markdown": markdown_path}
