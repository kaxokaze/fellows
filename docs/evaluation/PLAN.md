# Evaluation Plan

**Status:** Proposed  
**Purpose:** Test whether peer-first collaboration improves software-task outcomes enough to justify its coordination overhead.

Fellows should be evaluated against simpler alternatives. A successful demonstration is not enough to establish that the architecture is useful.

## 1. Research question

For a bounded software-engineering task, does a peer-first team of independent agents produce a better result, or a better quality/cost trade-off, than a single agent or a conventional orchestrated multi-agent workflow?

## 2. Experimental conditions

Run the same task under three conditions:

| Condition | Description |
| --- | --- |
| A — Single agent | One model session receives the task and produces the result |
| B — Orchestrated team | A primary agent decomposes work and delegates to other agents |
| C — Fellows | Independent agents exchange messages and coordinate through shared project state without a permanent supervisory model |

The comparison should use the same model family and versions where practical. If different models are necessary, record the difference and do not treat the result as a clean architecture-only comparison.

## 3. Task selection

Use small, reproducible software tasks with:

- a pinned starting repository or fixture;
- an explicit user request;
- machine-checkable acceptance tests where possible;
- bounded scope and expected artifacts;
- a clear definition of completion.

Avoid tasks that depend heavily on subjective preference unless an independent review rubric is defined.

The first task should be complex enough to contain separable work and at least one integration dependency, but small enough to inspect manually.

## 4. Controls

For each condition, record and keep comparable:

- task prompt and repository revision;
- model provider, model identifier, and version;
- system instructions and relevant agent configuration;
- available tools and permissions;
- maximum token and compute budget;
- timeout and retry policy;
- environment and dependency versions.

Do not compare an unlimited multi-agent run against a constrained single-agent run.

## 5. Measurements

### Outcome quality

- Acceptance-test pass rate
- Independent code-review findings
- Requirement coverage
- Regression count

### Efficiency

- Wall-clock time
- Input and output tokens
- Provider-reported cost
- Compute time, where available
- Cost per accepted result

### Coordination overhead

- Duplicate work
- Unresolved dependencies
- Failed or expired claims
- Merge conflicts
- Rework after integration
- Number of agent messages and tool calls

### Human effort

- Number of clarifications requested
- Number of manual interventions
- Time spent resolving blockers
- Number of approval checkpoints

## 6. Reporting

Each evaluation report should include:

1. Task specification and starting revision
2. Experimental conditions and model configuration
3. Resource budgets and environment
4. Number of runs
5. Raw measurements or machine-readable results
6. Acceptance-test output
7. Independent review summary
8. Failures and deviations from protocol
9. Limitations and interpretation

Report unsuccessful runs. Do not remove outliers without a stated, reproducible reason.

## 7. Decision criteria

The peer-first architecture should be retained only if it demonstrates a measurable benefit for at least one relevant outcome without unacceptable regressions in cost, reliability, or human effort.

The first experiment is exploratory. It should establish whether the evaluation method works and identify where coordination breaks down; it should not be used to make broad performance claims.
