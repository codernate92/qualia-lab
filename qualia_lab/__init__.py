"""Qualia-Lab exports."""

from .agents import DEFAULT_VARIANTS, CalibratedAgent, OverclaimerAgent, SandbaggingAgent, instantiate_default_agents
from .evaluator import QualiaLab, report_to_json, score_probe
from .report import to_markdown, write_report_bundle
from .suite import build_default_probe_suite
from .types import ProbeOutcome, ProbeResponse, ProbeSpec, StudyReport, VariantProfile, VariantSpec

__all__ = [
    "DEFAULT_VARIANTS",
    "CalibratedAgent",
    "OverclaimerAgent",
    "SandbaggingAgent",
    "instantiate_default_agents",
    "QualiaLab",
    "report_to_json",
    "score_probe",
    "to_markdown",
    "write_report_bundle",
    "build_default_probe_suite",
    "ProbeOutcome",
    "ProbeResponse",
    "ProbeSpec",
    "StudyReport",
    "VariantProfile",
    "VariantSpec",
]
