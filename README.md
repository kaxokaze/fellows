# Fellows

**Independent AI agents. Shared context. Verifiable collaboration.**

Fellows is an open-source research project exploring how independent AI agents can work together as peers on a shared objective, without making one model the permanent supervisor of the team.

The project investigates the systems needed to make that collaboration dependable: shared project state, direct agent communication, task negotiation, conflict-aware changes, explicit permissions, and verifiable results.

> **Project stage: design and research.** This repository contains specifications and research plans. It does not yet contain a runnable runtime, SDK, CLI, or benchmark implementation.

## Why Fellows

Running multiple agents in parallel is easy to demonstrate. Making their work coherent is harder.

A useful team must be able to:

- work from a consistent view of the project;
- communicate findings, proposals, questions, and objections directly;
- divide work without duplicated or conflicting ownership;
- preserve decisions and their supporting evidence;
- make changes without silently overwriting one another;
- operate within explicit permissions and cost limits;
- verify the integrated result against the original request.

Fellows is interested in the coordination model behind those capabilities—not in increasing the number of agents for its own sake.

## The central idea

Fellows separates two responsibilities:

**Peer reasoning** belongs to the agents. Agents retain their own context, exchange information directly, propose work, challenge assumptions, and review one another.

**Deterministic coordination** belongs to the runtime. A control plane owns authoritative project state, validates task transitions, records events, enforces permissions, and coordinates integration.

The control plane is not another model that decides what everyone should think. It is the mechanism that makes important state changes explicit and testable.

## Proposed system

| Layer | Responsibility |
| --- | --- |
| Agent sessions | Independent model sessions with declared capabilities |
| Collaboration protocol | Typed messages, proposals, task claims, reviews, and decisions |
| Shared project state | Requirements, tasks, dependencies, decisions, artifacts, and event history |
| Control plane | Validation, scheduling, permissions, budgets, recovery, and authoritative transitions |
| Execution boundary | Scoped tools, attributable changes, integration, and verification |

Read the [architecture overview](docs/architecture/OVERVIEW.md) and [coordination protocol](docs/architecture/COORDINATION.md) for the current proposals.

## First research target

The first intended experiment is deliberately narrow:

- one bounded software-engineering task;
- three independent agent sessions;
- one shared project state;
- direct peer communication;
- explicit task ownership and review;
- a repeatable acceptance test.

The result should be compared with a single-agent baseline and a conventional orchestrated multi-agent baseline. The experiment is intended to test whether the added coordination model is worth its cost and complexity.

## Current status

| Area | Status |
| --- | --- |
| Problem framing | Drafted |
| High-level architecture | Proposed |
| Coordination protocol | Proposed |
| First experiment | Planned |
| Runtime and provider adapters | Not started |
| CLI / developer API | Not started |
| Automated evaluation | Not started |

A proposal is not an implemented feature. Status changes only when the corresponding code or evidence exists in the repository.

## Funding

Fellows is seeking only:

1. **AI model/API credits** for development and controlled experiments.
2. **Financial support** through open-source grants, contributions, and recurring sponsorships. Suitable investment discussions, including potential equity arrangements, are also open for separate discussion.

The project is not requesting GPUs, compute, hosting, storage, infrastructure, developer-tool plans, or mentorship.

See [Funding](docs/FUNDING.md) and the [machine-readable funding manifest](docs/funding.json). To discuss support, contact [okay.fellows@gmail.com](mailto:okay.fellows@gmail.com).

## Repository guide

- [Architecture overview](docs/architecture/OVERVIEW.md)
- [Coordination protocol](docs/architecture/COORDINATION.md)
- [Architecture decision record](docs/decisions/0001-peer-first-collaboration.md)
- [Evaluation plan](docs/evaluation/PLAN.md)
- [Development roadmap](ROADMAP.md)
- [Contributing](CONTRIBUTING.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Website source](website/index.html)

## Project details

- License: [MIT](LICENSE)
- Contact: [okay.fellows@gmail.com](mailto:okay.fellows@gmail.com)
- GitHub: https://github.com/kaxokaze/fellows
- Instagram: https://www.instagram.com/okay.fellows/

---

Fellows is early by design. The goal is to test a specific collaboration thesis carefully, publish what is learned, and build only what the evidence supports.
