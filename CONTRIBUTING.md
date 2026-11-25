# Contributing to Fellows

Fellows is in the architecture and research phase. The project is not accepting broad implementation work yet; its first priority is to validate the collaboration model and define a small, testable runtime.

Contributions that improve the technical direction are welcome.

## Current areas of interest

- Peer-based agent coordination and task ownership
- Shared state, event logs, and context consistency
- Agent messaging and decision protocols
- Conflict-aware execution and artifact integration
- Tool isolation, permissions, and prompt-injection boundaries
- Evaluation methodology for multi-agent systems

## Proposing a design change

For substantial changes, open an issue before submitting a pull request. Include:

1. The problem and the scenario in which it occurs.
2. The proposed behavior or design.
3. Relevant prior work or existing implementations.
4. Alternatives considered.
5. Failure modes, security implications, and operational costs.
6. How the proposal could be tested.

A proposal should make clear whether it is a research question, an architectural decision, or an implementation request.

## Code contributions

The runtime implementation has not started. Build instructions, supported toolchains, test commands, and coding conventions will be added when those choices are made.

Until then, avoid introducing an arbitrary stack or a large implementation before its interfaces and acceptance criteria have been reviewed.

## Technical claims and benchmarks

Distinguish between a design proposal, implemented behavior, and measured results. Performance claims should include the task definition, model and provider versions, relevant configuration, resource limits, baseline, run count, and known limitations.

Do not use agent count, message volume, or a single successful demonstration as a substitute for a controlled comparison.

## Pull requests

Once implementation begins, pull requests should be focused and reviewable. Include tests for changed behavior, update the relevant design documents, and explain operational or compatibility implications. Do not include credentials, local configuration, generated artifacts, or unrelated changes.

## Discussion

Keep technical discussion specific and constructive. Disagreement is expected; explain the reasoning and evidence behind it.
