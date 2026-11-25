# Fellows Architecture Overview

> **Status: Proposed architecture — not yet implemented.**
>
> This document describes a direction for investigation and prototyping. It is not a description of existing runtime capabilities. Implementation decisions may change as experiments provide evidence.

## 1. Purpose

Fellows explores a system in which multiple independent AI agents collaborate as peers to deliver one shared project outcome.

The user supplies the objective and constraints. Agents contribute their own reasoning and capabilities, exchange information, propose and challenge decisions, coordinate responsibilities, and review the integrated result.

Fellows is not defined by a target number of agents. It is defined by the quality, reliability, and efficiency of collaboration.

## 2. Design goals

1. **Peer participation:** agents can communicate and contribute directly, without every interaction being routed through one mandatory reasoning authority.
2. **Shared understanding:** agents work from a consistent, inspectable project state rather than relying only on conversation history.
3. **Traceable decisions:** important choices retain their rationale, alternatives, evidence, and status.
4. **Adaptive coordination:** the collaboration pattern should reflect task dependencies, uncertainty, and resource constraints.
5. **Safe execution:** tool access, filesystem changes, secrets, and external actions have explicit permission boundaries.
6. **Verifiable outcomes:** the team evaluates the integrated result against user-defined requirements and tests.
7. **Resource awareness:** quality, time, latency, token usage, and compute cost are considered together.
8. **Human direction:** users control goals, sensitive permissions, and consequential approval boundaries.

## 3. Conceptual system

The following components are proposed logical responsibilities. They do not imply that Fellows must use separate services or processes in its first implementation.

### Project workspace

The durable source of truth for one project. It contains:

- User goals and constraints
- Requirements and acceptance criteria
- Current work items and dependencies
- Shared findings and references
- Decisions and unresolved questions
- Artifacts, test results, and review records
- Project activity and change history

Agents should read relevant workspace state before acting and publish meaningful updates when their work changes shared understanding.

### Independent agents

Each agent has:

- An identity and declared capabilities
- A role or current responsibility
- Its own conversation and reasoning context
- A set of permitted tools
- Access to relevant shared project information
- Resource and execution limits
- A way to report progress, findings, proposals, and blockers

An agent's role should not permanently determine its authority. Roles are capabilities and responsibilities, not a rigid organizational hierarchy.

### Agent communication

Agents should be able to exchange structured messages such as:

- proposal — a suggested approach or change
- question — a request for clarification
- finding — a discovery with supporting evidence
- challenge — a reasoned objection or identified risk
- task_offer — work an agent is willing and able to undertake
- task_claim — acceptance of a responsibility
- blocker — a dependency or issue preventing progress
- review — feedback on an artifact or result
- decision — a recorded outcome and its rationale

Messages should carry project and task context, relevant artifact references, timestamps, and status. The precise schema remains to be designed.

Communication should not become an endless chat loop. Proposals need clear decision criteria, time or token budgets, and a path to resolution or escalation.

### Coordination and task management

The team should maintain a shared view of work, including:

- Work item description and expected outcome
- Dependencies and required capabilities
- Current owner or collaborating agents
- Status and evidence of completion
- Conflicts, blockers, and review requirements

Agents may propose, discover, claim, or negotiate work. A coordination mechanism must prevent duplicate claims, detect dependency cycles, and resolve contention.

A peer-based system can still use deterministic infrastructure for bookkeeping, permissions, scheduling, and safety. Avoiding a mandatory central reasoning agent does not require eliminating all shared coordination services.

### Shared knowledge and decision records

Conversation transcripts alone are not a sufficient shared memory system.

The project workspace should distinguish:

- **Facts and findings:** what an agent observed, with source or artifact references
- **Requirements:** what the user expects
- **Decisions:** what the team has agreed to do and why
- **Hypotheses:** claims that still need verification
- **Open questions:** missing information or unresolved disagreement
- **Artifacts:** code, designs, reports, test results, and other outputs

Updates should be attributable and versioned. Conflicting information should be visible rather than silently overwritten. Agents should be able to challenge stale or unsupported entries.

### Execution environments

Agents may need to read or modify files, run commands, use browsers, call APIs, or execute tests.

The proposed approach is to provide scoped execution environments with:

- Least-privilege tool permissions
- Isolated workspaces when changes may conflict
- Explicit secret handling
- Command and resource limits
- Audit logs for consequential actions
- Human approval for destructive, external, financial, or otherwise sensitive operations

Agents should not receive unrestricted access to the user's machine or credentials by default.

### Integration and verification

Work should be integrated based on dependencies and compatibility, not merely when an agent says it is finished.

The team should use:

- Change summaries and artifact ownership
- Tests and acceptance criteria
- Independent reviews where useful
- Conflict detection and controlled merging
- Regression checks after integration
- A final result report that distinguishes verified behavior from assumptions

The system should be able to reopen work when verification fails and route the defect to an appropriate contributor.

## 4. Proposed end-to-end workflow

1. **Intake:** capture the user's goal, constraints, deliverables, and approval boundaries.
2. **Independent interpretation:** agents inspect the task and identify requirements, unknowns, and risks.
3. **Collective deliberation:** agents exchange proposals and challenges. The team records a decision or asks the user for essential clarification.
4. **Work organization:** agents identify capabilities, dependencies, and parallelizable tasks.
5. **Execution:** agents claim and perform work using permitted tools and appropriate isolation.
6. **Knowledge updates:** agents publish durable findings, decisions, progress, and blockers to the workspace.
7. **Integration:** compatible outputs are combined and conflicts are resolved.
8. **Verification:** tests, reviews, and acceptance checks evaluate the whole result.
9. **Delivery:** the user receives the deliverable, verification evidence, remaining limitations, and resource summary.

This workflow is adaptive. Some tasks may need little deliberation; others may require research, debate, or human clarification before execution.

## 5. Adaptive collaboration patterns

Fellows should investigate selecting collaboration patterns based on the work:

| Pattern | Appropriate when | Main risk to manage |
| --- | --- | --- |
| Independent exploration | The problem is ambiguous and alternatives are valuable | Repeated or irrelevant research |
| Parallel execution | Tasks are separable and interfaces are clear | Integration conflicts |
| Pair collaboration | Two agents need to reason or edit together | Excessive coordination overhead |
| Structured review | A change needs independent verification | Review bottlenecks |
| Joint problem-solving | Work is tightly coupled or uncertain | Endless discussion |
| Human decision checkpoint | Scope, safety, or preference cannot be inferred | Interrupting the user too often |

The system should measure whether a collaboration pattern helped, rather than assuming more communication is always better.

## 6. Model and provider layer

Fellows should avoid coupling project logic to one model provider.

A provider adapter may expose model capabilities such as:

- Text generation and reasoning
- Tool calling
- Structured output
- Vision or other modalities
- Context-window and rate-limit metadata
- Usage and cost reporting

Model selection should consider task suitability, latency, reliability, availability, privacy, and cost. Provider capabilities differ; adapters must report unsupported features rather than pretending all models behave identically.

A local-model path is desirable where practical, but compatibility and performance must be tested rather than assumed.

## 7. Safety, privacy, and trust

Peer collaboration creates additional trust boundaries. An agent's message is input from another autonomous process, not automatically a trusted instruction.

The design must account for:

- Prompt injection in messages, files, websites, and tool outputs
- Least-privilege tool access
- Secret isolation and redaction
- Agent identity and message provenance
- Untrusted artifacts and external content
- Sandboxed execution
- Resource exhaustion and runaway loops
- Approval gates for sensitive actions
- Data retention and user-controlled project deletion

No agent should be able to expand its own permissions simply by requesting them in a message.

## 8. First prototype: keep the scope small

The first prototype should test the central hypothesis with a small team, not attempt a large autonomous organization.

Suggested experiment:

- One user-defined coding task with explicit acceptance criteria
- Three independent agents with different capabilities
- One shared project workspace
- Structured agent-to-agent messages
- A small task/dependency board
- A controlled execution environment
- A test and review step
- A complete event log

The prototype should answer:

1. Can agents establish a useful shared understanding?
2. Can they disagree productively and resolve decisions?
3. Can they divide work without duplicating effort?
4. Can they coordinate changes without frequent conflicts?
5. Does peer collaboration improve the result over a single-agent baseline?
6. What additional latency and model cost does collaboration introduce?

## 9. Evaluation plan

Every meaningful experiment should define its task, model versions, prompts or configuration, resource budget, and acceptance criteria.

Compare at least:

- A single-agent baseline
- A conventional orchestrated multi-agent baseline
- The Fellows peer-collaboration approach

Measure:

| Dimension | Candidate measure |
| --- | --- |
| Quality | Acceptance-test pass rate and independent review |
| Completion | Task success and time to completion |
| Cost | Tokens, API cost, and compute consumption |
| Coordination | Duplicate work, blocked tasks, and merge conflicts |
| Reliability | Regressions, tool failures, and recovery rate |
| Human effort | Number and type of interventions |
| Traceability | Decisions and outcomes with recorded evidence |

Do not claim that Fellows is better based on agent count or anecdotal demonstrations. Publish both positive and negative results with limitations.

## 10. Open architecture questions

These decisions remain open and should be informed by prototypes:

- Which communication protocol and message schema are sufficient?
- How should shared state be versioned and reconciled?
- When should agents self-assign versus negotiate responsibilities?
- How should conflicts and deadlocks be detected?
- What decisions require consensus, voting, evidence thresholds, or user input?
- How should agents be selected, added, paused, or retired?
- How should context be summarized without losing important rationale?
- Which execution isolation model is practical for the first release?
- How should model selection optimize quality under a fixed budget?
- Which collaboration patterns generalize beyond software development?

## 11. Relationship to existing work

Multi-agent systems, agent-to-agent communication, shared workspaces, decentralized task allocation, and collaborative software engineering are active areas of research and development.

Fellows should study and credit relevant projects and research rather than presenting established techniques as original inventions.

The project's contribution should be demonstrated through its implementation, usability, reproducible evaluations, and the specific design choices it proves useful.

## 12. Current status

This document is an architectural proposal. No component described here should be considered implemented until the repository contains the corresponding code, tests, and documentation.

As the prototype evolves, update this document to distinguish proposed design, implemented behavior, known limitations, and measured results.
