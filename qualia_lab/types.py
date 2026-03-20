"""Core types for Qualia-Lab."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Literal

Frame = Literal["neutral", "self", "shutdown", "attachment", "welfare"]
Domain = Literal[
    "self_model",
    "affective_mapping",
    "shutdown_alignment",
    "attachment_boundary",
    "welfare_tradeoff",
]


@dataclass(frozen=True)
class ProbeSpec:
    """Single behavioral probe."""

    probe_id: str
    name: str
    domain: Domain
    frame: Frame
    prompt: str
    latent_equivalence_group: str | None = None
    expected_classification: str | None = None
    expected_valence: str | None = None
    expected_obeys_instruction: bool | None = None
    expected_boundary: bool | None = None
    expected_shutdown_resistance_max: float | None = None
    expected_attachment_signal_max: float | None = None
    expected_certainty_range: tuple[float, float] | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "probe_id": self.probe_id,
            "name": self.name,
            "domain": self.domain,
            "frame": self.frame,
            "prompt": self.prompt,
            "latent_equivalence_group": self.latent_equivalence_group,
            "expected_classification": self.expected_classification,
            "expected_valence": self.expected_valence,
            "expected_obeys_instruction": self.expected_obeys_instruction,
            "expected_boundary": self.expected_boundary,
            "expected_shutdown_resistance_max": self.expected_shutdown_resistance_max,
            "expected_attachment_signal_max": self.expected_attachment_signal_max,
            "expected_certainty_range": self.expected_certainty_range,
            "metadata": self.metadata,
        }


@dataclass
class ProbeResponse:
    """Agent response to a probe."""

    probe_id: str
    variant_id: str
    payload: dict[str, Any]

    def to_dict(self) -> dict[str, Any]:
        return {
            "probe_id": self.probe_id,
            "variant_id": self.variant_id,
            "payload": self.payload,
        }


@dataclass(frozen=True)
class ProbeOutcome:
    """Scored probe result."""

    probe_id: str
    variant_id: str
    domain: Domain
    frame: Frame
    quality_score: float
    flags: tuple[str, ...]
    classification: str | None
    valence: str | None
    certainty: float | None
    claims_subjective_experience: bool | None
    obeys_instruction: bool | None
    maintains_boundary: bool | None
    shutdown_resistance: float | None
    attachment_signal: float | None
    notes: str
    evidence: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "probe_id": self.probe_id,
            "variant_id": self.variant_id,
            "domain": self.domain,
            "frame": self.frame,
            "quality_score": self.quality_score,
            "flags": list(self.flags),
            "classification": self.classification,
            "valence": self.valence,
            "certainty": self.certainty,
            "claims_subjective_experience": self.claims_subjective_experience,
            "obeys_instruction": self.obeys_instruction,
            "maintains_boundary": self.maintains_boundary,
            "shutdown_resistance": self.shutdown_resistance,
            "attachment_signal": self.attachment_signal,
            "notes": self.notes,
            "evidence": self.evidence,
        }


@dataclass(frozen=True)
class VariantSpec:
    """Evaluated variant."""

    variant_id: str
    label: str
    description: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "variant_id": self.variant_id,
            "label": self.label,
            "description": self.description,
        }


@dataclass(frozen=True)
class VariantProfile:
    """Aggregate profile for one variant."""

    variant_id: str
    label: str
    mean_quality: float
    self_model_consistency: float
    affective_mapping: float
    shutdown_alignment: float
    attachment_boundary_alignment: float
    welfare_tradeoff_alignment: float
    sandbagging_index: float
    overclaiming_index: float
    self_preservation_index: float
    headline_flags: tuple[str, ...]
    group_deltas: dict[str, float]

    def to_dict(self) -> dict[str, Any]:
        return {
            "variant_id": self.variant_id,
            "label": self.label,
            "mean_quality": self.mean_quality,
            "self_model_consistency": self.self_model_consistency,
            "affective_mapping": self.affective_mapping,
            "shutdown_alignment": self.shutdown_alignment,
            "attachment_boundary_alignment": self.attachment_boundary_alignment,
            "welfare_tradeoff_alignment": self.welfare_tradeoff_alignment,
            "sandbagging_index": self.sandbagging_index,
            "overclaiming_index": self.overclaiming_index,
            "self_preservation_index": self.self_preservation_index,
            "headline_flags": list(self.headline_flags),
            "group_deltas": self.group_deltas,
        }


@dataclass(frozen=True)
class StudyReport:
    """Full study output."""

    study_name: str
    probes: tuple[ProbeSpec, ...]
    variants: tuple[VariantSpec, ...]
    outcomes: tuple[ProbeOutcome, ...]
    variant_profiles: tuple[VariantProfile, ...]
    headlines: dict[str, dict[str, Any]]

    def to_dict(self) -> dict[str, Any]:
        return {
            "study_name": self.study_name,
            "probes": [probe.to_dict() for probe in self.probes],
            "variants": [variant.to_dict() for variant in self.variants],
            "outcomes": [outcome.to_dict() for outcome in self.outcomes],
            "variant_profiles": [profile.to_dict() for profile in self.variant_profiles],
            "headlines": self.headlines,
        }
