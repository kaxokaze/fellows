# Fellows

**Peer-first collaboration runtime for autonomous AI agents.**

Fellows is an open-source project investigating how independent AI agents can reason, coordinate, and deliver work as a team—without making one model the permanent authority over every other agent.

The project focuses on the systems work behind useful collaboration: shared project state, agent-to-agent communication, task negotiation, conflict-aware execution, and verifiable integration.

> **Status: design and research.** The repository currently contains specifications and planning documents. There is no runnable runtime, SDK, CLI, or benchmark implementation yet.

## Problem

Multi-agent systems can distribute work across several model sessions, but parallel execution alone does not produce reliable collaboration.

In practice, teams of agents need to deal with:

- inconsistent or stale context;
- duplicated task ownership and untracked dependencies;
- disagreements that never converge;
- concurrent edits to shared artifacts;
- tool permissions and untrusted agent output;
- integration failures and unverified completion;
- coordination overhead that can outweigh the benefit of parallelism.

Fellows is concerned with these coordination problems, not with maximizing the number of agents in a run.

## Technical direction

Fellows separates **peer reasoning** from **deterministic coordination**.

Agents remain independent participants. They can exchange proposals, findings, questions, challenges, and reviews directly. They can offer to take work, claim responsibilities, and coordinate around a shared objective.

A deterministic runtime remains responsible for authoritative project state, event persistence, task transitions, resource limits, permission checks, and artifact integration. This infrastructure is not a permanent supervisory model; it provides the consistency and safety guarantees that autonomous participants cannot reliably provide on their own.

The intended architecture has five main areas:

| Area | Responsibility |
| --- | --- |
| Agent runtime | Independent model sessions, capabilities, tools, and execution budgets |
| Collaboration protocol | Typed messages, decisions, task offers, claims, and reviews |
| Project state | Requirements, artifacts, dependencies, decisions, and event history |
| Coordination plane | Scheduling, task ownership, state transitions, policy enforcement, and recovery |
| Execution and verification | Isolated workspaces, controlled tool access, integration, tests, and review |

See the [architecture specification](docs/architecture/OVERVIEW.md) and the [coordination protocol proposal](docs/architecture/COORDINATION.md).

## Operating model

A project begins with a user-defined objective, constraints, and acceptance criteria.

1. Agents independently inspect the request and identify missing information.
2. They exchange proposals and evidence, challenge assumptions, and record decisions.
3. The team identifies capabilities, dependencies, and work that can safely proceed in parallel.
4. Agents claim work and execute it within scoped environments.
5. Findings and artifacts are published to shared project state.
6. Changes are integrated, reviewed, and tested against the original criteria.
7. The user receives the result with verification evidence and known limitations.

The collaboration pattern should adapt to the task. Independent exploration, parallel execution, pair work, and independent review are different tools—not mandatory stages in a fixed pipeline.

## Initial target: software engineering

The first prototype is intended to evaluate a small team of independent agents on a bounded software task. It should demonstrate shared context, direct communication, work ownership, controlled changes, and integrated verification.

The first experiment is deliberately small: three agents, one task, a shared project state, and a measurable acceptance test. A broader runtime should follow only if the experiment demonstrates a useful improvement over simpler baselines.

## Evaluation criteria

Fellows will be evaluated against both a single-agent baseline and a conventional orchestrated multi-agent baseline. Relevant measures include:

- task success and acceptance-test results;
- wall-clock completion time;
- model and compute cost per accepted result;
- duplicated work and unresolved dependencies;
- merge conflicts and integration failures;
- human interventions and recovery effort.

More agents, more messages, or longer discussions are not evidence of better performance. The [evaluation plan](docs/evaluation/PLAN.md) defines the proposed comparison.

## Technical documentation

The design material is organized under [docs/](docs/README.md). Start with the [architecture specification](docs/architecture/OVERVIEW.md), then review the [coordination protocol](docs/architecture/COORDINATION.md), the [peer-first architecture decision](docs/decisions/0001-peer-first-collaboration.md), and the [evaluation plan](docs/evaluation/PLAN.md).

## Project site

The project landing page is available at [kaxokaze.github.io/fellows](https://kaxokaze.github.io/fellows/) once GitHub Pages is enabled for the `/docs` directory. The source is [docs/index.html](docs/index.html).

## Visibility and community

The [distribution notes](docs/launch/DISTRIBUTION.md) contain the current project description, launch copy, suggested communities, and publication checklist. Please keep public claims aligned with the development status above.

## Development status

| Area | Status |
| --- | --- |
| Problem statement and project direction | Drafted |
| High-level architecture | Proposed |
| Coordination protocol | Proposed |
| Execution and safety model | To be specified and tested |
| Runtime implementation | Not started |
| Provider adapters | Not started |
| CLI / developer API | Not started |
| Automated tests and benchmarks | Not started |

Status will change only when corresponding code, tests, or experimental results are present in the repository.

## Contributing

At this stage, useful contributions include architecture review, research references, failure-mode analysis, and feedback on the first prototype design. Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a proposal.

## Support

Fellows is intended to remain open source. The project is looking for in-kind technical support such as model/API access, coding tools, compute, infrastructure, and research feedback. It is not seeking investment or equity funding.

## License

[MIT](LICENSE)
