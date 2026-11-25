# Fellows

**Independent AI agents, working together on one project.**

Fellows is an open-source project exploring a different way to build with AI agents. Instead of treating every additional agent as a subagent managed by one primary model, Fellows asks what happens when several independent agents can share context, discuss the work, make decisions, and coordinate as peers.

The goal is a team that can take a project from an initial request to a reviewed result, while keeping the user in control.

## Why

Running several agents at once is easy to describe and hard to make useful. Agents can repeat work, lose important context, disagree without resolving anything, or make changes that conflict with each other. More agents do not necessarily produce a better result.

Fellows is focused on the parts that make collaboration work: shared project context, direct communication, clear decisions, coordination around dependencies, and verification of the finished work.

## How it should work

A user gives the team an objective and its constraints.

The agents examine the task, share what they know, and discuss important choices. They then agree on a plan, divide work where that makes sense, and coordinate when their work overlaps. Before delivery, the team checks that the pieces fit together and that the result meets the original requirements.

The team should be able to change its working style as the project changes. Some tasks need parallel work; others need a closer discussion or an independent review.

## First use case

The first area to explore is software development.

For example, a request to build a portfolio site might involve agents looking at product requirements, design, implementation, and testing. Those are areas of responsibility, not permanent ranks. The agents should be able to share findings and work together when a decision affects more than one area.

## Current status

**Fellows is at the design and research stage. There is no working implementation in this repository yet.**

The repository currently contains the project overview, a proposed architecture, and a development roadmap. The next step is to narrow the design into a small prototype and test whether peer collaboration improves results over a single agent and a conventional orchestrated team.

- [Proposed architecture](docs/architecture/OVERVIEW.md)
- [Roadmap](ROADMAP.md)
- [Contributing](CONTRIBUTING.md)

## What the first prototype needs to test

- A small group of independent agents can discuss and plan one shared task.
- Agents can read and update a common project state without losing the history of decisions.
- Work can be divided without unnecessary duplication.
- Changes can be integrated and checked safely.
- Any improvement is worth the extra time and model cost.

We will update this section as the design becomes an implementation. Planned work should not be read as an existing feature.

## Support and collaboration

Fellows is being developed as an open-source project. Help with model access, API credits, coding tools, compute, infrastructure, or technical feedback would be useful. This is a request for in-kind developer support, not investment or equity funding.

## License

Fellows is available under the [MIT License](LICENSE).
