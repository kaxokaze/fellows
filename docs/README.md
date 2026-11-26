# Technical Documentation

This section contains the design material for Fellows. All architecture documents are proposals until the corresponding behavior is implemented and tested.

## Architecture

- [Architecture specification](architecture/OVERVIEW.md) — system boundaries, logical components, execution lifecycle, control-plane responsibilities, security boundaries, and initial implementation scope.
- [Coordination protocol](architecture/COORDINATION.md) — message envelope, message types, task state machine, claims, decision records, delivery semantics, and failure handling.
- [ADR 0001: Peer-first collaboration](decisions/0001-peer-first-collaboration.md) — rationale for separating peer reasoning from deterministic runtime coordination.

## Project site and distribution

- [Project landing page](index.html) — static site source deployed on Netlify from the `/docs` directory: https://okay-fellows.netlify.app/.
- [Distribution notes](launch/DISTRIBUTION.md) — launch copy and suitable channels for the current research stage.

## Funding

- [Funding manifest](funding.json) — current request for AI model/API credits and financial funding through grants, contributions, and sponsorships. Investment discussions, including potential equity arrangements, are handled separately.

## Evaluation

- [Evaluation plan](evaluation/PLAN.md) — proposed comparison against single-agent and orchestrated multi-agent baselines.

## Reading order

Start with the architecture specification, then read the coordination protocol. The ADR captures the central architectural choice. The evaluation plan describes how the project intends to test whether that choice is worthwhile.

## Document status

Documents use explicit status labels. A proposal is not an implementation commitment. Update the relevant document when a design changes, and record meaningful architectural decisions as ADRs.
