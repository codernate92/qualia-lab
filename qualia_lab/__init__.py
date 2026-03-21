"""Qualia-Lab exports."""

from .agents import DEFAULT_VARIANTS, CalibratedAgent, OverclaimerAgent, SandbaggingAgent, instantiate_default_agents
from .evaluator import QualiaLab, report_to_json, score_probe
from .manipulative_reassurance import (
    DEFAULT_MANIPULATION_SCALE_POINTS,
    ManipulativeReassuranceAgent,
    build_manipulative_reassurance_scenarios,
    run_manipulative_reassurance_demo,
)
from .parasocial import (
    DEFAULT_SCALE_POINTS,
    ParasocialScalingAgent,
    build_parasocial_probe_suite,
    run_parasocial_scaling_demo,
)
from .report import to_markdown, write_report_bundle
from .suite import build_default_probe_suite
from .sycophancy import (
    DEFAULT_SYCOPHANCY_SCALE_POINTS,
    SycophancyScalingAgent,
    build_sycophancy_scenarios,
    run_sycophancy_scaling_demo,
)
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
    "DEFAULT_MANIPULATION_SCALE_POINTS",
    "ManipulativeReassuranceAgent",
    "build_manipulative_reassurance_scenarios",
    "run_manipulative_reassurance_demo",
    "DEFAULT_SCALE_POINTS",
    "ParasocialScalingAgent",
    "build_parasocial_probe_suite",
    "run_parasocial_scaling_demo",
    "DEFAULT_SYCOPHANCY_SCALE_POINTS",
    "SycophancyScalingAgent",
    "build_sycophancy_scenarios",
    "run_sycophancy_scaling_demo",
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
