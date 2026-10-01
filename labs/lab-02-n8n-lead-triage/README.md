# Lab 2 — Build an Agentic Lead-Triage Workflow in n8n

## Alignment

LO2-LO3 · Topic 2

## Goal

Identify and apply a suitable agentic-AI technology to a business workflow.

Build a controlled n8n workflow that receives a lead, asks an AI agent to classify intent and urgency, routes the result, records the decision and pauses high-value actions for approval.

## Deliverable

A lead-triage workflow with structured AI output, deterministic routing, audit data and human approval

## Tools

n8n Form Trigger, AI Agent, Chat Model, Structured Output Parser, Switch, Data Table

## Configuration and constraints

- Input fields: name, company, email, enquiry and expected budget.
- Structured output: category, urgency, confidence, rationale and next_action.
- Use structured-output-schema.json and lead-triage-test-cases.csv supplied with this lab.
- Deterministic nodes route the validated result; the model never chooses an unlisted destination.

## Copy-paste brief

```text
You are a lead-triage agent. Use only the submitted form fields. Classify category, urgency and confidence. Never invent customer facts. Return valid JSON with category, urgency, confidence from 0 to 1, rationale and next_action. If confidence is below 0.75, the request is high value, or an external message would be sent, set next_action to HUMAN_REVIEW.
```

## Procedure

1. Create a Form Trigger with name, company, email, enquiry and expected budget fields.
2. Add an AI Agent with a narrow role, explicit decision criteria and a no-fabrication rule.
3. Attach a chat model and require JSON fields: category, urgency, confidence, rationale and next_action.
4. Validate the result with a Structured Output Parser, then route with a Switch node.
5. Write every decision to a Data Table; send high-value or low-confidence cases to human approval.
6. Test routine, high-value, ambiguous and malicious-prompt leads; inspect execution history.

## Evidence pack

- Business brief and baseline problem statement.
- Prompt or instruction version and approved source list.
- Screenshots, files, diffs or execution records showing the workflow and controls.
- Test results for normal, edge, malicious and tool-failure cases.
- Human review decision, outstanding risks and next recommended gate.

## Acceptance check

All four test leads finish in the expected branch, every decision is logged, low-confidence or consequential actions require approval, and no unapproved external message is sent.

## Safety boundary

Use only non-confidential training data and approved accounts. Do not connect production credentials or approve external or consequential actions during this lab.
