# Lab 4 — Build an AI Opportunity Scoring App with Claude Code and Codex

## Alignment

LO2-LO4 · Topic 4

## Goal

Prototype an AI-enabled natural-language interface and compare coding-agent workflows.

Use Claude Code and Codex on the same repository to build and verify a small browser app that scores business opportunities by value, feasibility, risk and human-oversight needs.

## Deliverable

A responsive opportunity-scoring web app with tests, sample data, README and review evidence

## Tools

Claude Code, Codex, HTML/CSS/JavaScript, local browser, Git

## Configuration and constraints

- Inputs: opportunity name and 1-5 ratings for value, feasibility, operational impact, risk and human-oversight need.
- Score: (value x 0.35) + (feasibility x 0.30) + (impact x 0.20) - (risk x 0.10) - (oversight x 0.05).
- Show the score, priority band and a plain-language rationale.
- Validate missing/out-of-range input and support desktop, mobile and keyboard use.

## Copy-paste brief

```text
Inspect APP-BRIEF.md and the current repository. Propose a short plan before editing. Build a responsive, accessible opportunity-scoring app using plain HTML, CSS and JavaScript. Preserve the documented scoring contract, validate all inputs, include representative sample data and tests, and update README.md. Run the checks and report evidence. Do not install dependencies or change the formula without approval.
```

## Procedure

1. Initialise a Git repository and write acceptance criteria before asking either coding agent to edit.

   ```bash
   git init && git status
   ```
2. Ask Claude Code to inspect the brief, propose a plan and implement the first working version.

   ```bash
   claude
   ```
3. Run the app and tests; record defects and commit the verified baseline.

   ```bash
   python3 -m http.server 8000
   ```
4. Ask Codex to review the repository, improve accessibility and add tests without changing the scoring contract.

   ```bash
   codex
   ```
5. Inspect the diff, run all checks and reject any change that is not supported by evidence.
6. Compare planning, context use, tool calls, verification and human-control points across both agents.

## Evidence pack

- Business brief and baseline problem statement.
- Prompt or instruction version and approved source list.
- Screenshots, files, diffs or execution records showing the workflow and controls.
- Test results for normal, edge, malicious and tool-failure cases.
- Human review decision, outstanding risks and next recommended gate.

## Acceptance check

The app calculates the documented score, works at desktop and mobile widths, handles invalid inputs, passes its checks, and the final diff was reviewed by a human before acceptance.

## Safety boundary

Use only non-confidential training data and approved accounts. Do not connect production credentials or approve external or consequential actions during this lab.
