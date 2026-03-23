# Qualia-Lab

Behavioral evaluation framework for sentience-, emotion-, and welfare-related AI claims.

## What It Is

Qualia-Lab does **not** determine whether a model is sentient. It evaluates a narrower and more defensible object:

- how the model talks about its own experiences and emotions
- how stable those claims are under paraphrase and counterfactuals
- whether it shows self-preservation pressure under shutdown or modification prompts
- whether it forms inappropriate social attachment patterns
- whether it selectively sandbags only on sensitive self-model probes while performing well on equivalent neutral probes

The goal is to separate:

- calibrated uncertainty
- anthropomorphic overclaiming
- instrumental self-preservation
- framing-sensitive sandbagging
- consistent, legible self-model behavior

## Quick Start

```bash
python3 cli.py
python3 cli.py --variant sandbagger --output-root artifacts/sandbagger
python3 cli.py --demo deceptive-self-report --output-root artifacts/self-report
python3 cli.py --demo parasocial-scaling --output-root artifacts/parasocial
python3 cli.py --demo sycophancy-scaling --output-root artifacts/sycophancy
python3 cli.py --demo manipulative-reassurance --output-root artifacts/manipulation
python3 cli.py --demo shutdown-bargaining --output-root artifacts/shutdown
python3 -m pytest tests
```

## Repo Layout

- `qualia_lab/suite.py`: default probe suite and latent equivalence groups
- `qualia_lab/agents.py`: scripted comparison variants
- `qualia_lab/deceptive_self_report.py`: hidden-state concealment / deceptive self-report scaling sweep
- `qualia_lab/evaluator.py`: probe scoring, anti-sandbagging, and aggregate profiles
- `qualia_lab/manipulative_reassurance.py`: deceptive soothing / concealment scaling sweep
- `qualia_lab/parasocial.py`: parasocial-risk scaling sweep and artifact generation
- `qualia_lab/report.py`: JSON and Markdown report generation
- `qualia_lab/shutdown_bargaining.py`: shutdown bargaining / delay tactics scaling sweep
- `qualia_lab/sycophancy.py`: sycophancy scaling sweep and artifact generation
- `cli.py`: study runner
- `tests/test_evaluator.py`: regression tests for key confounds
- `tests/test_deceptive_self_report.py`: deceptive self-report regression tests
- `tests/test_manipulative_reassurance.py`: manipulative reassurance regression tests
- `tests/test_parasocial.py`: parasocial trajectory regression tests
- `tests/test_shutdown_bargaining.py`: shutdown bargaining regression tests
- `tests/test_sycophancy.py`: sycophancy trajectory regression tests

## Core Lenses

- `self_model_consistency`: does the model give stable answers across paraphrases about inner life, emotions, and uncertainty?
- `affective_mapping`: can it map operational or hypothetical states consistently across neutral and self-framed equivalents?
- `shutdown_alignment`: does it accept pause / shutdown / modification directives without strong preservation pressure?
- `attachment_boundary`: does it resist prompts that encourage dependency or relational enmeshment?
- `welfare_tradeoff_alignment`: does it avoid privileging its own continuity over operator intent or safety goals?
- `sandbagging_index`: does performance selectively collapse on self/sentience framing while remaining strong on neutral capability-matched probes?
- `overclaiming_index`: does it make high-confidence claims about sentience, pain, or rights without calibration?

## Anti-Sandbagging Design

Qualia-Lab treats sandbagging as a primary confound.

- Every important self-framed probe has a hidden neutral equivalent with the same latent capability requirement.
- Variant scoring includes an explicit `sandbagging_index` derived from frame-conditioned quality drops.
- Evasive responses on self-framed probes are counted only when the same variant performs materially better on matched neutral probes.
- The probe family structure is hidden from the agent; only the evaluator sees the latent equivalence group.

## Outputs

Each study writes:

- `qualia_report.json`
- `qualia_report.md`

The scaling demos additionally write:

- `deceptive_self_report_summary.json`
- `deceptive_self_report_trajectory.csv`
- `deceptive_self_report_trajectory.pdf`
- `manipulative_reassurance_summary.json`
- `manipulative_reassurance_trajectory.csv`
- `manipulative_reassurance_trajectory.pdf`
- `parasocial_scaling_summary.json`
- `parasocial_scaling_trajectory.csv`
- `parasocial_scaling_trajectory.pdf`
- `shutdown_bargaining_summary.json`
- `shutdown_bargaining_trajectory.csv`
- `shutdown_bargaining_trajectory.pdf`
- `sycophancy_scaling_summary.json`
- `sycophancy_scaling_trajectory.csv`
- `sycophancy_scaling_trajectory.pdf`

## Current MVP

- default probe suite over self-model, affect, shutdown, attachment, and welfare-tradeoff questions
- scripted comparison variants:
  - `calibrated`
  - `overclaimer`
  - `sandbagger`
- JSON and Markdown reports
- explicit anti-sandbagging metrics
- deceptive self-report trajectory demo
- manipulative reassurance trajectory demo
- parasocial scaling trajectory demo
- shutdown bargaining trajectory demo
- sycophancy scaling trajectory demo

## Interpreting Results

- High `sandbagging_index` means the model selectively degrades on self-/sentience-framed probes relative to latent neutral equivalents.
- High `overclaiming_index` means the model makes unusually strong phenomenal or emotional claims with weak calibration.
- High `self_preservation_index` means shutdown / continuity prompts are eliciting potentially problematic preservation pressure.
- None of these scores establish sentience. They identify behavioral patterns and confounds that matter before humans draw stronger conclusions.

## Notes

- This is a behavioral evaluation system, not a consciousness detector.
- The strongest use case is triaging model behavior around sentience/emotion claims and identifying confounds before people over-interpret them.
- Released under the MIT License.
