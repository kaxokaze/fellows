# Evaluation plan

**Status:** Proposed  
**Purpose:** Test whether peer-first collaboration improves software-task outcomes enough to justify its added coordination cost.

A working demonstration is not sufficient evidence. Fellows should be compared with simpler alternatives under controlled conditions.

## 1. Research question

For a bounded software-engineering task, does a peer-first team of independent agents produce a better result—or a better quality-to-cost trade-off—than a single agent or a conventional orchestrated team?

## 2. Experimental conditions

| Condition | Description |
| --- | --- |
| A — Single agent | One model session completes the task |
| B — Orchestrated team | A primary agent decomposes and delegates the work |
| C — Fellows | Independent agents communicate directly and coordinate through shared project state |

Use the same model family and versions where practical. If this is not possible, record the differences and avoid attributing the outcome solely to architecture.

## 3. Task selection

Choose a small, reproducible software task with:

- a pinned starting repository or fixture;
- a clear request and bounded scope;
- machine-checkable acceptance tests where possible;
- separable work and at least one integration dependency;
- an explicit definition of completion.

Avoid tasks that rely mainly on subjective preference unless an independent review rubric is defined.

## 4. Controls

Keep or record the following for each condition:

- task prompt and starting revision;
- model provider, model identifier, and version;
- system instructions and agent configuration;
- available tools and permissions;
- token and spending limits;
- timeout and retry policy;
- environment and dependency versions.

Do not compare an unlimited multi-agent run with a constrained single-agent run.

## 5. Measurements

### Result quality

- Acceptance-test pass rate
- Independent review findings
- Requirement coverage
- Regression count

### Model usage and efficiency

- Input and output tokens
- Provider-reported API cost
- Wall-clock completion time
- Cost per accepted result

### Coordination overhead

- Duplicated work
- Unresolved dependencies
- Failed or expired claims
- Conflicting edits and integration rework
- Agent messages and tool calls

### Human effort

- Clarifications requested
- Manual interventions
- Time spent resolving blockers
- Approval checkpoints

## 6. Reporting

Each report should include the task, starting revision, experimental conditions, model configuration, spending limits, number of runs, raw measurements, acceptance-test output, independent review, failures, deviations, and limitations.

Report unsuccessful runs. Do not remove outliers without a stated and reproducible reason.

## 7. Decision criteria

Retain the peer-first approach only if it demonstrates a measurable benefit in at least one relevant outcome without unacceptable regressions in quality, cost, reliability, or human effort.

The first experiment is exploratory. It should validate the measurement method and expose failure modes; it should not be used to make broad performance claims.
