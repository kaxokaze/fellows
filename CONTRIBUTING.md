# Contributing to Fellows

Thank you for taking an interest in Fellows.

Fellows is currently in the design and research stage. The first priority is to test the peer-first collaboration thesis and define a small, measurable prototype. Contributions should improve the clarity, safety, or testability of that work.

## Useful contributions

- Research on peer-based and orchestrated agent systems
- Review of the architecture and coordination protocol
- Shared-state and event-history design
- Task ownership, leases, and dependency handling
- Permission boundaries and untrusted agent-output handling
- Evaluation design and reproducible task selection
- Precise documentation corrections

## Before making a substantial change

Open an issue or start a discussion before investing in a large proposal. Explain:

1. The problem and the scenario in which it appears.
2. The proposed change and expected behavior.
3. Relevant prior work or evidence.
4. Alternatives considered.
5. Failure modes, security implications, and cost.
6. How the proposal could be tested.

Do not present an architectural suggestion as an implemented capability.

## Pull requests

Keep changes focused and reviewable. Update the relevant specification when a design decision changes. Include tests when behavior exists to test, and explain compatibility or operational consequences.

Do not commit credentials, private data, local configuration, generated build output, or unrelated changes.

## Technical claims

Clearly distinguish between:

- **Proposed:** described in a design document.
- **Implemented:** present in source code.
- **Verified:** exercised by tests or a reproducible experiment.
- **Measured:** supported by recorded results and a stated methodology.

Benchmarks should identify the task, model and provider versions, configuration, budgets, baseline, run count, and limitations.

## Discussion

Be specific, respectful, and evidence-led. Disagreement is welcome; personal attacks are not. Follow the [Code of Conduct](CODE_OF_CONDUCT.md).

## License

By contributing, you agree that your contribution is made available under the repository's [MIT License](LICENSE).
