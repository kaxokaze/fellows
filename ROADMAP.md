# Development Roadmap

This roadmap is organized around evidence and deliverables. A milestone is complete when its exit criteria are met—not when the planned tasks have merely been discussed.

## M0 — Research and system definition

**Objective:** establish what Fellows is trying to prove and what it will not attempt in the first release.

- [ ] Review relevant peer-based, orchestrated, and shared-workspace agent systems.
- [ ] Define the first software-engineering task and acceptance criteria.
- [ ] Finalize the initial project-state model and message envelope.
- [ ] Define trust boundaries and tool-permission requirements.
- [ ] Specify single-agent and orchestrated multi-agent baselines.
- [ ] Set a fixed model and resource budget for comparisons.

**Exit criteria:** reviewed architecture, protocol proposal, threat boundaries, and repeatable experiment definition.

## M1 — Collaboration kernel

**Objective:** demonstrate communication and shared state between a small number of independent agent sessions.

- [ ] Start and stop independent agent sessions.
- [ ] Persist typed messages with sender, recipient/scope, timestamp, and correlation metadata.
- [ ] Maintain a versioned project state.
- [ ] Record proposals, findings, challenges, and decisions.
- [ ] Expose an inspectable event history.
- [ ] Handle retries and duplicate message delivery safely.

**Exit criteria:** three agents can exchange messages and update a shared project without losing attribution or silently overwriting conflicting state.

## M2 — Work coordination

**Objective:** coordinate bounded work without a permanent supervisory model.

- [ ] Represent work items and dependency relationships.
- [ ] Support task offers, claims, leases, and completion reports.
- [ ] Prevent conflicting claims on exclusive work.
- [ ] Detect blocked tasks and dependency cycles.
- [ ] Define timeout, retry, and reassignment behavior.
- [ ] Make disagreement and unresolved decisions visible.

**Exit criteria:** agents can divide a project into bounded tasks, claim work, and recover from a stalled or failed task.

## M3 — Controlled execution and integration

**Objective:** allow agents to change project artifacts without making the workspace unsafe or unreviewable.

- [ ] Define isolated workspace and change-set behavior.
- [ ] Scope filesystem, shell, network, and provider-tool access.
- [ ] Track artifact ownership and changed paths.
- [ ] Detect overlapping changes.
- [ ] Integrate changes through a controlled path.
- [ ] Run acceptance and regression checks before completion.

**Exit criteria:** a small team can deliver an integrated software change with an auditable record and reproducible checks.

## M4 — Comparative evaluation

**Objective:** determine whether the peer-first approach is worth its additional coordination cost.

- [ ] Run the same tasks with a single-agent baseline.
- [ ] Run the same tasks with a conventional orchestrated baseline.
- [ ] Run the same tasks with Fellows.
- [ ] Keep model versions, prompts, tools, and budgets comparable.
- [ ] Repeat runs and report variance.
- [ ] Publish task definitions, configurations, raw measurements, and limitations.

**Exit criteria:** a reproducible report covering quality, latency, cost, coordination overhead, and human intervention.

## M5 — Developer experience

**Objective:** make the collaboration kernel usable by developers.

- [ ] Define a stable developer API.
- [ ] Add provider adapters based on demonstrated requirements.
- [ ] Add CLI workflows for creating and inspecting projects.
- [ ] Add local execution and configuration documentation.
- [ ] Add examples and integration tests.
- [ ] Document supported environments and limitations.

**Exit criteria:** an external developer can install the project, configure a supported model provider, run the example, and inspect the result.

---

## Prioritization rules

- Do not add a subsystem until a prototype or evaluation justifies it.
- Prefer explicit state transitions over hidden model-driven state.
- Keep provider-specific behavior behind adapters.
- Treat security, cost, and recovery as runtime requirements.
- Do not mark a milestone complete without evidence in the repository.
