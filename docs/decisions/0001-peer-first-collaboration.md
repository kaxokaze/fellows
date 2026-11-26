# ADR 0001 — Peer-first collaboration

- **Status:** Accepted as the research direction
- **Date:** 2026-11-26
- **Scope:** Initial multi-agent collaboration model

## Context

Fellows investigates how independent AI agents can contribute to one project outcome.

A hierarchical arrangement places one primary agent in charge of planning and delegation. This can simplify control, but it also makes that agent a persistent reasoning bottleneck and limits direct interaction among other agents.

A fully uncoordinated peer network is not a reliable alternative. Software work still requires authoritative state, permissions, task ownership, cost limits, and integration rules.

## Decision

Fellows will investigate a **peer-first reasoning layer backed by a deterministic control plane**.

Agents may communicate directly, publish findings, challenge proposals, negotiate work, claim bounded tasks, and review artifacts. No model is required to act as the team's permanent semantic supervisor.

The control plane remains authoritative for project state, validated transitions, message persistence, permissions, budgets, cancellation, and integration.

This is a research direction, not a claim that the system has been implemented or proven effective.

## Consequences

Expected benefits:

- Agents can exchange information without routing every interaction through a lead model.
- Reasoning and state-management responsibilities are separated.
- Permissions and state transitions can be tested independently of model behavior.
- Different model providers can be used without changing the collaboration protocol.

Costs and risks:

- Agents may duplicate effort or fail to resolve disagreement.
- Shared state and message semantics add design complexity.
- Direct communication may increase token usage and latency.
- Claims, revisions, retries, and integration require careful control.
- Untrusted model output must never become privileged instruction.

## Alternatives

### Permanent lead-agent hierarchy

Simpler to coordinate, but does not test the peer-collaboration thesis.

### Uncoordinated peer execution

Avoids a central control plane but lacks dependable state, permissions, ownership, and conflict resolution.

### Peer reasoning with deterministic coordination

Selected for investigation because it preserves agent independence while retaining enforceable operational rules.

## Validation

Compare the approach with a single-agent baseline and a conventional orchestrated team on the same bounded task. Revisit this decision if peer communication does not justify its added cost and complexity.
