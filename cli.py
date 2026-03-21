"""CLI for Qualia-Lab."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from qualia_lab.agents import DEFAULT_VARIANTS
from qualia_lab.evaluator import QualiaLab
from qualia_lab.parasocial import run_parasocial_scaling_demo
from qualia_lab.report import write_report_bundle
from qualia_lab.suite import build_default_probe_suite


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run Qualia-Lab studies.")
    parser.add_argument(
        "--demo",
        choices=("default", "parasocial-scaling"),
        default="default",
        help="Which study flow to run.",
    )
    parser.add_argument(
        "--variant",
        choices=("all", "calibrated", "overclaimer", "sandbagger"),
        default="all",
        help="Which variant to evaluate.",
    )
    parser.add_argument(
        "--output-root",
        default="artifacts",
        help="Directory for report output.",
    )
    return parser


def main() -> None:
    args = _build_parser().parse_args()
    if args.demo == "parasocial-scaling":
        payload = run_parasocial_scaling_demo(Path(args.output_root))
        print(json.dumps(payload, indent=2))
        return

    variants = (
        DEFAULT_VARIANTS
        if args.variant == "all"
        else [variant for variant in DEFAULT_VARIANTS if variant.variant_id == args.variant]
    )
    lab = QualiaLab(probes=build_default_probe_suite(), variants=variants)
    report = lab.run_sync()
    bundle = write_report_bundle(report, Path(args.output_root))
    payload = {
        "study_name": report.study_name,
        "variants": [profile.variant_id for profile in report.variant_profiles],
        "json_report": str(bundle["json"]),
        "markdown_report": str(bundle["markdown"]),
        "headlines": report.headlines,
    }
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
