# Fellows Roadmap

This roadmap describes intended exploration. Items are not complete until implementation and evidence are available in the repository.

## Stage 1 — Project foundations

- [ ] Define problem statement and system boundaries.
- [ ] Review existing multi-agent and peer-collaboration approaches.
- [ ] Define terminology: agent, peer, project context, decision, task, dependency.
- [ ] Write initial threat model and trust boundaries.
- [ ] Define evaluation tasks and baselines.

**Exit criteria:** reviewed architecture proposal, explicit non-goals, evaluation plan.

## Stage 2 — Shared project intelligence

- [ ] Define project state and context schema.
- [ ] Record requirements, discoveries, decisions, and open questions.
- [ ] Design agent messaging and event history.
- [ ] Define context ownership, freshness, and conflict resolution.
- [ ] Add inspection and replay tools for project decisions.

**Exit criteria:** multiple independent agents can read and update a consistent project context with traceable changes.

## Stage 3 — Peer coordination

- [ ] Allow agents to propose and discover work.
- [ ] Represent dependencies and resource requirements.
- [ ] Design responsibility negotiation and task claiming.
- [ ] Support discussion, challenge, and decision finalization.
- [ ] Prevent circular discussion and unproductive contention.

**Exit criteria:** agents coordinate a bounded task without requiring every action to be delegated by one central agent.

## Stage 4 — Safe collaborative execution

- [ ] Define isolated workspace strategy.
- [ ] Detect file and resource conflicts.
- [ ] Integrate independent changes.
- [ ] Add review and verification checkpoints.
- [ ] Define tool permissions and human approval boundaries.

**Exit criteria:** a small team can make coordinated changes and produce a verifiable integrated result.

## Stage 5 — Evaluation

- [ ] Establish single-agent baseline.
- [ ] Establish conventional orchestrated multi-agent baseline.
- [ ] Run identical tasks with comparable model and resource budgets.
- [ ] Measure quality, completion time, token/compute cost, duplicate work, and integration failures.
- [ ] Publish configurations, results, and limitations.

**Exit criteria:** reproducible evaluation report with honest comparisons.

## Stage 6 — Developer experience

- [ ] CLI or developer API.
- [ ] Project/team inspection interface.
- [ ] Provider and model adapters.
- [ ] Local and hosted execution options.
- [ ] Documentation and examples.

## Principles for roadmap changes

- Prioritize verified user value over feature count.
- Prefer measurable experiments over unsupported claims.
- Keep security, privacy, cost, and failure recovery in scope.
- Update this roadmap when priorities change; preserve completed work and explain meaningful changes.
