# Security Policy

Fellows is an early-stage open-source project. Security controls and supported deployment configurations may not yet be implemented.

## Reporting a vulnerability

Please do not publish exploitable vulnerability details in a public issue.

Use GitHub's private vulnerability reporting feature for this repository if available. Include:

- Affected commit, version, or file.
- Impact and prerequisites.
- Reproduction steps or a proof of concept.
- Any suggested mitigation.

Do not include real credentials, personal data, or secrets in reports.

## Scope

As the project develops, security review should cover agent tool permissions, command execution, filesystem access, shared workspace isolation, prompt injection, inter-agent message trust, secret handling, and external provider integrations.

Do not assume an item is protected until the implementation and tests demonstrate it.
