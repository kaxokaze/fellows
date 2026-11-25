<div align="center">

# Fellows

### Independent minds. Shared intelligence. Collective execution.

**An open-source exploration of peer-based AI collaboration.**

[Vision](#the-vision) · [How it works](#how-it-works) · [Roadmap](#project-status--roadmap) · [Contributing](CONTRIBUTING.md)

</div>

---

> **Project stage: Early concept and research.** Fellows is being developed in the open. The architecture, prototype, and capabilities described below are goals under investigation—not claims that a finished platform already exists.

## The vision

Most AI workflows begin with one primary agent. Other agents, when present, are often organized around that agent as delegated workers.

**Fellows explores a different approach: independent AI agents collaborating as peers around one shared objective.**

A user describes the outcome they want. A team of agents should be able to interpret the goal, exchange knowledge, challenge assumptions, develop a shared plan, coordinate work, and collectively review the result.

The aim is not simply to run more agents in parallel. It is to make collaboration itself a first-class part of the system.

## Why Fellows?

Complex work benefits from different perspectives and specialized skills. But adding agents does not automatically create a good team: agents can duplicate work, contradict decisions, collide over shared files, lose context, or spend more resources communicating than producing useful work.

Fellows is being shaped around these research and engineering questions:

- How can independent agents build and maintain a shared understanding of a project?
- How should agents communicate, disagree, and reach traceable decisions?
- How can a team organize and adapt its responsibilities without relying on a rigid hierarchy?
- How can parallel work be coordinated while preventing conflicting changes?
- How can the system measure quality, latency, reliability, and cost—not just agent count?

## How it should work

1. **Understand** — agents independently interpret the objective and identify unknowns.
2. **Deliberate** — they exchange proposals, question assumptions, and record decisions.
3. **Organize** — the team identifies responsibilities, dependencies, and useful specialists.
4. **Execute** — agents work independently or collaboratively according to task dependencies.
5. **Integrate** — changes are reviewed and combined into one coherent result.
6. **Verify** — the team tests the outcome and uses evidence to decide what needs improvement.

This is the intended workflow. The implementation will evolve as the project is researched and built.

## Design principles

| Principle | What it means |
| --- | --- |
| Peer collaboration | Agents contribute as independent participants, not merely as a fixed chain of delegated workers. |
| Shared project context | Requirements, discoveries, decisions, and dependencies remain accessible to the team. |
| Evidence-based decisions | Important choices should have recorded reasoning, alternatives, and supporting evidence. |
| Adaptive teamwork | Team composition and collaboration patterns should respond to the work. |
| Safe coordination | Shared resources, tool permissions, and code changes need explicit boundaries. |
| Measurable efficiency | Quality should be evaluated alongside time, compute, and token cost. |
| Human direction | People define goals, constraints, and approval boundaries. |

## Initial application: software development

A user might ask Fellows to build a portfolio website.

A design-focused agent could explore the visual direction; an engineering-focused agent could assess architecture; a research-focused agent could investigate relevant approaches; and a testing-focused agent could identify quality risks.

Those agents should share their findings, challenge decisions, agree on an implementation direction, coordinate changes, and verify the final website.

The roles are examples, not fixed built-in agents. The system should be able to adapt the team to the task.

## Project status & roadmap

Fellows is at an early stage. The following roadmap describes intended work, not completed features.

- [ ] **Stage 1 — Foundations:** define the system boundaries, goals, terminology, and evaluation criteria.
- [ ] **Stage 2 — Shared context:** design project memory, decision records, and agent-to-agent messaging.
- [ ] **Stage 3 — Peer coordination:** prototype task discovery, responsibility negotiation, and dependency handling.
- [ ] **Stage 4 — Execution:** support isolated and shared workspaces with safe integration.
- [ ] **Stage 5 — Evaluation:** compare Fellows with a single-agent baseline and conventional orchestrated multi-agent workflows.
- [ ] **Stage 6 — Usability:** build a practical interface for creating, observing, and steering teams.

Progress will be reflected here as work becomes real and verifiable.

## How we plan to evaluate it

We do not consider a larger number of agents proof of better collaboration. Evaluation should use reproducible tasks and comparable model/resource budgets.

| Dimension | Example measurements |
| --- | --- |
| Outcome quality | Acceptance tests, task completion, review findings |
| Efficiency | Time to completion, tokens, compute cost |
| Coordination | Duplicate work, merge conflicts, dependency failures |
| Reliability | Regressions, recovery from failed tasks |
| Autonomy | Human interventions required |
| Collaboration | Useful information sharing and decision traceability |

Results will only be published when experiments have actually been run. We will document task definitions, configurations, baselines, and limitations.

## Open source and collaboration

Fellows is intended to be developed openly. We welcome thoughtful feedback, research references, architecture discussions, issue reports, and contributions.

Before proposing a major implementation, please open an issue describing the problem and proposed approach. See [CONTRIBUTING.md](CONTRIBUTING.md).

The project currently uses the [MIT License](LICENSE).

## Support and technology collaboration

Fellows is an independent open-source effort. We are interested in technical collaboration and in-kind developer support that can help us research, build, and evaluate the project.

Relevant support may include:

- API credits or access to AI models
- Coding and agent-development tools
- GPU, inference, and cloud compute
- Storage, databases, CI, and testing infrastructure
- Research feedback, mentorship, and early developer access

We are **not seeking investment or equity funding** through this project. Any supported integration or contribution will be documented transparently.

## Stay connected

- **Repository:** https://github.com/kaxokaze/fellows
- **Issues and discussions:** use the repository's GitHub tabs
- **License:** [MIT](LICENSE)

---

<div align="center">

**Fellows**

*Better together, by design.*

</div>
