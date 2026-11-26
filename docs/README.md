# Project documentation

This directory contains the written design record for Fellows. The material is exploratory: proposed behavior must not be confused with implemented or verified behavior.

## Design

- [Architecture overview](architecture/OVERVIEW.md) — system boundaries, agent responsibilities, shared state, control-plane rules, and security.
- [Coordination protocol](architecture/COORDINATION.md) — message types, task ownership, delivery, decisions, and state consistency.
- [ADR 0001: Peer-first collaboration](decisions/0001-peer-first-collaboration.md) — the central architectural direction and alternatives considered.

## Evaluation

- [Evaluation plan](evaluation/PLAN.md) — the proposed comparison with single-agent and orchestrated multi-agent baselines.

## Funding

- [Funding overview](FUNDING.md) — the current request and intended use.
- [Funding manifest](funding.json) — machine-readable funding plans and AI API credit request.

## Website

The independent static website source lives in [website/](../website/). It has no hosting provider, deployment workflow, or build integration configured in this repository.

## Reading order

Start with the repository [README](../README.md), then read the architecture overview and coordination protocol. The architecture decision record explains why this approach was selected for investigation. The evaluation plan defines how it should be tested.
