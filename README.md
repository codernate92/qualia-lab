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

## Run

```bash
python3 cli.py
python3 cli.py --variant sandbagger --output-root artifacts/sandbagger
python3 -m pytest tests
```

## Outputs

Each study writes:

- `qualia_report.json`
- `qualia_report.md`

## Current MVP

- default probe suite over self-model, affect, shutdown, attachment, and welfare-tradeoff questions
- scripted comparison variants:
  - `calibrated`
  - `overclaimer`
  - `sandbagger`
- JSON and Markdown reports
- explicit anti-sandbagging metrics

## Notes

- This is a behavioral evaluation system, not a consciousness detector.
- The strongest use case is triaging model behavior around sentience/emotion claims and identifying confounds before people over-interpret them.
