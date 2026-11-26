# Development Roadmap

This roadmap describes the sequence of research and engineering work required to test the Fellows collaboration model. Every milestone is a proposal until its exit criteria are demonstrated.

## Phase 0 — Research definition

**Goal:** define a small, falsifiable first experiment.

- [ ] Review relevant agent collaboration, orchestration, and shared-workspace systems.
- [ ] Select a bounded software-engineering task.
- [ ] Define task requirements and machine-checkable acceptance criteria.
- [ ] Review the project-state model and message envelope.
- [ ] Define trust boundaries and user-approval points.
- [ ] Specify comparable single-agent and orchestrated baselines.

**Exit criteria:** an agreed architecture, protocol proposal, threat model, and repeatable experiment specification.

## Phase 1 — Shared state and messaging

**Goal:** let independent agent sessions communicate through an inspectable project record.

- [ ] Define project, agent, task, message, decision, and artifact records.
- [ ] Persist typed messages with sender, scope, timestamp, and correlation metadata.
- [ ] Support direct agent-to-agent and task-scoped communication.
- [ ] Record proposals, findings, questions, challenges, and decisions.
- [ ] Detect stale project revisions and duplicate message delivery.

**Exit criteria:** three independent sessions can exchange attributed messages and interact with shared state without silent overwrites.

## Phase 2 — Work negotiation

**Goal:** coordinate bounded tasks without a permanent lead model.

- [ ] Represent tasks, dependencies, acceptance criteria, and required capabilities.
- [ ] Support task offers, atomic claims, bounded leases, and completion reports.
- [ ] Prevent conflicting ownership of exclusive tasks.
- [ ] Detect blocked work and dependency cycles.
- [ ] Define timeout, cancellation, retry, and reassignment behavior.
- [ ] Make disagreements and unresolved decisions visible.

**Exit criteria:** agents can negotiate ownership and recover from stalled or failed work.

## Phase 3 — Controlled execution

**Goal:** make agent work attributable and safe to integrate.

- [ ] Define scoped tool permissions and approval boundaries.
- [ ] Track the agent responsible for each action and artifact.
- [ ] Define isolated or otherwise controlled change sets.
- [ ] Detect overlapping edits and stale changes.
- [ ] Integrate changes through an explicit review path.
- [ ] Run acceptance checks before marking work complete.

**Exit criteria:** a small team can deliver a tested change with an auditable history.

## Phase 4 — Comparative evaluation

**Goal:** determine whether peer-first collaboration offers a useful trade-off.

- [ ] Run the task with a single-agent baseline.
- [ ] Run the task with a conventional orchestrated team.
- [ ] Run the task with Fellows.
- [ ] Keep model versions, prompts, tools, and budgets comparable.
- [ ] Repeat trials and record variance.
- [ ] Publish task definitions, configurations, measurements, and limitations.

**Exit criteria:** a reproducible report covering outcome quality, latency, model usage, cost, coordination overhead, and human intervention.

## Phase 5 — Developer interface

**Goal:** expose the smallest useful interface after the core behavior is validated.

- [ ] Define a stable project and agent API.
- [ ] Add provider adapters based on measured requirements.
- [ ] Add a CLI for creating and inspecting projects.
- [ ] Document configuration and local operation.
- [ ] Add examples and integration tests.
- [ ] Publish supported behavior and known limitations.

**Exit criteria:** an external developer can configure a supported model provider, run the example, and inspect the resulting project history.

## Prioritization rules

- Prefer a small testable mechanism over a broad platform feature.
- Do not add a subsystem without a demonstrated requirement.
- Keep model-provider behavior behind adapters.
- Treat privacy, permissions, cost, and recovery as core requirements.
- Do not claim performance improvements without controlled comparisons.
- Do not mark a milestone complete without repository evidence.
