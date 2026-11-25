# Architecture

**Status: proposal.** Fellows has no implementation yet. This document records the design direction for the first prototype; it is expected to change as the idea is tested.

## The central idea

A user gives a team one goal. Several independent agents work on it as peers.

An agent is not simply a child process that receives a task from a permanent lead agent. It has its own context, capabilities, and tools. It can share findings with the team, challenge a proposal, offer to take work, and review another agent's result.

This does not mean removing all coordination. The system still needs reliable ways to store project state, track work, enforce permissions, and prevent conflicts. Those jobs can be handled by ordinary software rather than another model acting as the team's boss.

## Proposed components

The first design has five parts. They do not need to be separate services.

### 1. Agents

Each agent has an identity, a set of capabilities, its own working context, permitted tools, and resource limits. Roles such as design, research, implementation, or testing describe what an agent can contribute; they should not create a fixed hierarchy.

Agents should be able to communicate directly. They should also be able to work independently when there is no reason to coordinate.

### 2. Shared project state

The team needs one durable place for information that matters beyond a single conversation:

- the user's goal and constraints
- requirements and acceptance criteria
- work items and dependencies
- findings and references
- decisions and the reasons behind them
- open questions and blockers
- artifacts, reviews, and test results

A conversation transcript is not a substitute for this. Shared state should be structured, attributable, and versioned. Conflicting updates should be visible rather than silently overwritten.

### 3. Communication and decisions

Agents need a way to exchange useful messages, not just chat freely. The initial message types can be kept small:

- **Proposal:** a suggested approach
- **Finding:** information with a source or artifact
- **Question:** something the agent needs to know
- **Challenge:** a reasoned objection or risk
- **Work offer / claim:** an agent offering to take work or accepting it
- **Blocker:** something preventing progress
- **Review:** feedback on a change
- **Decision:** the outcome and its rationale

A discussion should end in a decision, a recorded disagreement, or a question for the user. It should not continue indefinitely. Time and token budgets will matter.

### 4. Coordination and execution

Work items should describe an expected result, dependencies, and the agents involved. Agents may suggest or claim work, but the system must prevent two agents from unknowingly taking the same exclusive task.

Code changes need similar care. Independent work can happen in separate workspaces; tightly related work may need a shared workspace or an explicit hand-off. The first prototype should choose the simplest approach that makes conflicts visible and recoverable.

Tool access should be limited to what an agent needs. Shell commands, file access, external services, and credentials must not be unrestricted by default. Destructive or external actions should have clear approval rules.

### 5. Integration and review

An agent saying a task is complete is not enough. The team should check the result against the original requirements.

For a software task, that may mean running tests, reviewing changes, checking that components work together, and reporting anything that remains unverified. Failed checks should create follow-up work rather than being hidden in a final summary.

## First prototype

Keep the first experiment deliberately small:

- Three independent agents
- One software task with clear acceptance criteria
- A shared project state
- Direct agent messages
- A simple way to propose and claim work
- A controlled environment for code changes
- A test and review step
- An event log showing who did what and why

Do not start with a large team, a complex dashboard, or a fully general-purpose agent marketplace. First find out whether a small peer team can coordinate better than the alternatives.

## How to evaluate it

Run the same task under three setups:

1. One agent.
2. A conventional orchestrated team.
3. The Fellows peer approach.

Keep the models and resource budgets as comparable as practical. Record the task definition, model versions, settings, and results.

Measure:

- whether the result passes the task's acceptance tests
- time to completion
- token and compute cost
- duplicated or abandoned work
- merge conflicts and failed dependencies
- human interventions required

A larger team or longer discussion is not evidence of a better result. If the peer approach does not improve quality or reliability enough to justify its cost, the design needs to change.

## Decisions still open

The prototype should help answer these questions:

- How should agents claim work and resolve competing claims?
- Which project facts belong in shared state, and how are they updated?
- How should the team handle disagreement when there is no obvious answer?
- When should agents work in isolation and when should they share a workspace?
- How should the system stop circular discussion?
- Which actions need user approval?
- Does the collaboration pattern change with the task?

## Existing work

Multi-agent collaboration, agent messaging, shared workspaces, and decentralized task allocation are already active areas of research and development. Fellows should build on that work and give credit to relevant projects.

The project will need to show its value through a working implementation and repeatable comparisons, not through claims that the underlying ideas are new.
