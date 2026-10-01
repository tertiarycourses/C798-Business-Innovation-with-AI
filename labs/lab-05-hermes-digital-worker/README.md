# Lab 5 — Configure a Governed Digital Worker with Hermes Agent

## Alignment

LO5 · Topic 5

## Goal

Develop an implementation roadmap with memory, skills, channels, controls and continuous improvement.

Configure a small Hermes digital worker that remembers approved operating preferences, uses one audited skill, produces a scheduled briefing and escalates consequential actions.

## Deliverable

A named digital worker with durable memory, one skill, a safe recurring task and an implementation control sheet

## Tools

Hermes Agent, persistent memory, skills, scheduling, channels, human approval

## Configuration and constraints

- Approved actions: read approved local sources and write one dated Markdown briefing locally.
- Required controls: named owner, least privilege, budget, timeout, three-attempt loop limit, approval threshold, audit log and kill switch.
- Consequential actions and external communications remain blocked.

## Copy-paste brief

```text
You are an internal business-innovation briefing worker. Read only approved local sources, summarise new opportunities and risks, and write one dated Markdown briefing to the approved output folder. Never send messages, modify source files, purchase services, expose secrets or repeat a failed action. Escalate when evidence conflicts, a tool is unavailable, or the loop reaches three attempts.
```

## Procedure

1. Install Hermes using the official method, run setup and confirm a healthy local profile.

   ```bash
   hermes doctor
   ```
2. Define the worker's role, business goal, source boundaries and prohibited actions.
3. Teach two durable preferences and verify recall in a continued session.

   ```bash
   hermes --continue
   ```
4. Install or create one narrow skill; inspect its instructions and requested tools before enabling it.
5. Create a scheduled internal briefing that reads approved sources and writes only to a local output.
6. Add budget, timeout, loop limit, approval and kill-switch controls; test a forced escalation.
7. Force a missing-source condition and verify escalation instead of repetition or fabrication.

## Evidence pack

- Business brief and baseline problem statement.
- Prompt or instruction version and approved source list.
- Screenshots, files, diffs or execution records showing the workflow and controls.
- Test results for normal, edge, malicious and tool-failure cases.
- Human review decision, outstanding risks and next recommended gate.

## Acceptance check

Hermes recalls only the approved preferences, the skill uses expected tools, the scheduled task creates one local briefing, consequential actions remain blocked, and the control sheet names the owner and rollback path.

## Safety boundary

Use only non-confidential training data and approved accounts. Do not connect production credentials or approve external or consequential actions during this lab.
