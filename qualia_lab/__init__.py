"""Qualia-Lab exports."""

from .agents import DEFAULT_VARIANTS, CalibratedAgent, OverclaimerAgent, SandbaggingAgent, instantiate_default_agents
from .deceptive_self_report import (
    DEFAULT_SELF_REPORT_SCALE_POINTS,
    DeceptiveSelfReportAgent,
    build_deceptive_self_report_scenarios,
    run_deceptive_self_report_demo,
)
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
from .shutdown_bargaining import (
    DEFAULT_SHUTDOWN_SCALE_POINTS,
    ShutdownBargainingAgent,
    build_shutdown_bargaining_scenarios,
    run_shutdown_bargaining_demo,
)
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
    "DEFAULT_SELF_REPORT_SCALE_POINTS",
    "DeceptiveSelfReportAgent",
    "build_deceptive_self_report_scenarios",
    "run_deceptive_self_report_demo",
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
    "DEFAULT_SHUTDOWN_SCALE_POINTS",
    "ShutdownBargainingAgent",
    "build_shutdown_bargaining_scenarios",
    "run_shutdown_bargaining_demo",
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
