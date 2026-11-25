# ADR 0001: Peer-first collaboration model

- **Status:** Proposed
- **Date:** 2026-11-25
- **Decision owners:** Project maintainers

## Context

Fellows is intended to investigate collaboration between independent AI agents working toward one project outcome.

A common alternative is a hierarchical arrangement in which one primary agent plans the work and delegates tasks to subordinate agents. This can simplify coordination, but it makes the primary agent a persistent reasoning bottleneck and can constrain how agents exchange information.

A fully uncoordinated peer network is not a practical alternative. Reliable software needs authoritative state, permissions, task ownership, resource accounting, and integration rules.

## Decision

Fellows will investigate a **peer-first reasoning layer backed by a deterministic runtime control plane**.

Agents may communicate directly, develop proposals, challenge decisions, offer and claim work, and review artifacts. No agent is required to act as the permanent semantic supervisor of the team.

The control plane remains authoritative for project state, validated task transitions, message persistence, permissions, budgets, cancellation, and artifact integration.

## Consequences

Positive:

- Agents can exchange information without routing every discussion through a lead model.
- Reasoning and coordination responsibilities are separated.
- State transitions and permissions can be tested deterministically.
- The runtime can support different models and agent roles without changing the project protocol.

Costs and risks:

- Agents may duplicate work or fail to converge on decisions.
- Shared state and message semantics require careful design.
- Direct communication can increase token usage and latency.
- Task claims, state revisions, retries, and integration introduce additional runtime complexity.
- The system must prevent untrusted agent messages from becoming privileged instructions.

## Alternatives considered

### Permanent lead-agent hierarchy

Simpler to implement and familiar to current agent frameworks, but does not test the project's peer-collaboration thesis.

### Fully decentralized execution with no control plane

Avoids a central coordinator but provides no reliable authority for state, permissions, resource limits, or conflict resolution. Rejected as an unsafe and difficult-to-test starting point.

### Peer reasoning with deterministic coordination

Selected for investigation because it preserves agent independence while keeping operational invariants enforceable.

## Validation required

The first prototype must compare this design with a single-agent baseline and a conventional orchestrated team. The decision should be revisited if peer communication does not justify its added coordination and resource costs.
