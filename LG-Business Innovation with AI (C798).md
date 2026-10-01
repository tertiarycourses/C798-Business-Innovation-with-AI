# Learner Guide — Business Innovation with AI (C798)

Tertiary Infotech Academy Pte Ltd · Version v1.0 · 1 October 2026

## How to Use This Guide

| Purpose: This guide supports the course Business Innovation with AI (C798). It is designed for concept study, facilitated discussion and practical work. |
|---|

- Read each topic's core explanations before attempting its case and lab.
- Use the worksheets to apply the concepts to a real but non-confidential workflow.
- Treat every tool output as evidence to review, not as an automatically correct answer.
- Keep prompts, source lists, screenshots, test results and approval decisions as your evidence pack.
- Verify the current product interface, access and pricing before a facilitated activity.

| Safety rule: Never use production credentials, customer data, confidential files or real external communications in a training lab. |
|---|

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |

COURSE ROADMAP

Learning Journey and Page Map

| Topic | Business capability |
|---|---|
| Topic 1 | Evolution of Business AI from Generative AI to Autonomous AI Agents |
| Topic 2 | Generative AI, Agentic AI and AI Agent Technologies |
| Topic 3 | Context, Harness and Loop Engineering for AI Agents |
| Topic 4 | Business Opportunities and Innovative Agentic AI Use Cases |
| Topic 5 | Evaluating and Implementing AI-Driven Business Innovation |

Each topic moves through explanation, application, frameworks, cases, a guided lab, knowledge checks and an action plan. The sequence helps you connect technology features to business design and governance.

- Lab 1: Create a Business Story Video with Gemini
- Lab 2: Build an Agentic Lead-Triage Workflow in n8n
- Lab 3: Delegate Knowledge Work with Claude Cowork and ChatGPT Work
- Lab 4: Build an AI Opportunity Scoring App with Claude Code and Codex
- Lab 5: Configure a Governed Digital Worker with Hermes Agent
LO1-LO5

Learning Outcomes and Alignment

- LO1: Compare traditional business models with AI-enabled models and explain the 2023-2026 shift from generative AI to autonomous agents.
- LO2: Identify high-value business opportunities for generative AI, agentic AI and AI agents across functions.
- LO3: Select suitable LLMs and AI technologies and explain reasoning, memory, tools, skills, channels and task execution.
- LO4: Evaluate AI opportunities using value, feasibility, cost, risk, operational impact and human oversight.
- LO5: Design an implementation roadmap using context, harness and loop engineering with governance and continuous improvement.

| Outcome | Topics and labs |
|---|---|
| LO1 | Topics 1; Labs 1. Business-AI evolution and traditional versus AI-enabled business models. |
| LO2 | Topics 2, 4; Labs 2, 4. High-value opportunities and agentic-AI use cases across business functions. |
| LO3 | Topics 2, 3; Labs 2, 3, 4. LLM and technology selection, agent architecture, context, harness and loop design. |
| LO4 | Topics 3, 5; Labs 3, 4. Value, feasibility, risk, controls, testing and human oversight. |
| LO5 | Topics 5; Labs 5. Implementation roadmap, governance, measurement and continuous improvement. |

| Practice: Use the case worksheets and topic knowledge checks to practise justified business decisions, not memorised product descriptions. |
|---|

CORE MODEL

Large Language Models (LLMs)

| Definition: A large language model (LLM) is a trained mathematical model that represents language as tokens, learns statistical relationships in large text and code collections, and generates output by repeatedly estimating the next token. |
|---|

Use this model to analyse the course examples and your own workplace opportunities. A component is present only when it can be observed in instructions, configuration, tool access, workflow state, logs or operating responsibilities.

- Large: Learns patterns from very large collections of text and code.
- Language: Represents text as tokens and learns relationships among them in context.
- Model: A trained mathematical system whose parameters encode learned statistical patterns.
- Inference: Given context, estimates probabilities for the next token and generates one token at a time.
- Transformer: Attention helps the model relate relevant tokens across the supplied context.
- Important limit: A fluent answer is a generated prediction, not automatic proof that the answer is true.

| Design question | Required evidence |
|---|---|
| What outcome is pursued? | Business metric and acceptance criterion |
| What may the system do? | Permission and tool contract |
| How is quality evaluated? | Tests, evaluator and human review |
| When does it stop? | Completion, escalation, budget and kill-switch rules |

| Notes 1: |
|---|
| Notes 2: |

CORE MODEL

Choosing an LLM for Business Use

| Definition: Select the model against the business requirement and evaluate it on representative work. |
|---|

Use this model to analyse the course examples and your own workplace opportunities. A component is present only when it can be observed in instructions, configuration, tool access, workflow state, logs or operating responsibilities.

- Task quality: Evaluate on representative cases and failure modes, not a generic leaderboard alone.
- Context capacity: Fit the instructions, evidence and working state needed for the task.
- Speed and cost: Balance response time, volume, model price and total workflow cost.
- Input and output: Check required text, image, audio, video, code and structured-data capabilities.
- Tool reliability: Test tool calling, schema compliance and recovery from failed actions.
- Risk boundary: Match privacy, security, residency, deployment and vendor controls to the data.

| Design question | Required evidence |
|---|---|
| What outcome is pursued? | Business metric and acceptance criterion |
| What may the system do? | Permission and tool contract |
| How is quality evaluated? | Tests, evaluator and human review |
| When does it stop? | Completion, escalation, budget and kill-switch rules |

| Notes 1: |
|---|
| Notes 2: |

### Generative AI, Agentic AI and AI Agents

| Definition: Generative AI creates content or code. Agentic AI describes goal-directed behaviour across steps. An AI agent is the deployed system combining model, instructions, context, memory, tools, skills, channels, loop and oversight. |
|---|

Use this model to analyse the course examples and your own workplace opportunities. A component is present only when it can be observed in instructions, configuration, tool access, workflow state, logs or operating responsibilities.

- Ask whether the system has a goal and state.
- Inspect what tools can change external systems.
- Check persistence, memory and stop conditions.
- Identify the accountable human owner.

| Design question | Required evidence |
|---|---|
| What outcome is pursued? | Business metric and acceptance criterion |
| What may the system do? | Permission and tool contract |
| How is quality evaluated? | Tests, evaluator and human review |
| When does it stop? | Completion, escalation, budget and kill-switch rules |

| Notes 1: |
|---|
| Notes 2: |

CORE MODEL

The Agent Architecture

| Definition: A reliable agent is an engineered system rather than a model in isolation. Each component has a distinct responsibility and failure mode. |
|---|

Use this model to analyse the course examples and your own workplace opportunities. A component is present only when it can be observed in instructions, configuration, tool access, workflow state, logs or operating responsibilities.

- Reasoning selects a next step.
- Instructions establish role and constraints.
- Memory retains approved information.
- Tools read or change external state.
- Skills package bounded procedures.
- Channels connect users and systems.

| Design question | Required evidence |
|---|---|
| What outcome is pursued? | Business metric and acceptance criterion |
| What may the system do? | Permission and tool contract |
| How is quality evaluated? | Tests, evaluator and human review |
| When does it stop? | Completion, escalation, budget and kill-switch rules |

| Notes 1: |
|---|
| Notes 2: |

CORE MODEL

The Agentic Loop

| Definition: A useful loop plans, acts, observes, evaluates and then completes, improves, retries or escalates. The transition rules matter more than the diagram. |
|---|

Use this model to analyse the course examples and your own workplace opportunities. A component is present only when it can be observed in instructions, configuration, tool access, workflow state, logs or operating responsibilities.

- Define observable success.
- Separate retryable from consequential actions.
- Limit attempts, time and cost.
- Record evidence at every transition.

| Design question | Required evidence |
|---|---|
| What outcome is pursued? | Business metric and acceptance criterion |
| What may the system do? | Permission and tool contract |
| How is quality evaluated? | Tests, evaluator and human review |
| When does it stop? | Completion, escalation, budget and kill-switch rules |

| Notes 1: |
|---|
| Notes 2: |

### Context Engineering

| Definition: Context engineering selects the smallest sufficient working set for the current decision: goal, constraints, knowledge, current state, memory, examples and tool results. |
|---|

Use this model to analyse the course examples and your own workplace opportunities. A component is present only when it can be observed in instructions, configuration, tool access, workflow state, logs or operating responsibilities.

- Prioritise authoritative and current sources.
- Expose conflicts rather than blending them.
- Keep temporary state separate from durable memory.
- Remove irrelevant material.

| Design question | Required evidence |
|---|---|
| What outcome is pursued? | Business metric and acceptance criterion |
| What may the system do? | Permission and tool contract |
| How is quality evaluated? | Tests, evaluator and human review |
| When does it stop? | Completion, escalation, budget and kill-switch rules |

| Notes 1: |
|---|
| Notes 2: |

### Harness Engineering

| Definition: The harness shapes the environment: permissions, tool schemas, workflow state, tests, evaluators, logs, approvals, sandboxes and recovery paths. |
|---|

Use this model to analyse the course examples and your own workplace opportunities. A component is present only when it can be observed in instructions, configuration, tool access, workflow state, logs or operating responsibilities.

- Make safe actions easy.
- Make prohibited actions impossible where practical.
- Require evidence before completion.
- Provide rollback and a kill switch.

| Design question | Required evidence |
|---|---|
| What outcome is pursued? | Business metric and acceptance criterion |
| What may the system do? | Permission and tool contract |
| How is quality evaluated? | Tests, evaluator and human review |
| When does it stop? | Completion, escalation, budget and kill-switch rules |

| Notes 1: |
|---|
| Notes 2: |

CORE MODEL

Human Accountability

| Definition: People set intent, approve consequential actions, resolve ambiguity, own business outcomes and decide whether a system should continue operating. |
|---|

Use this model to analyse the course examples and your own workplace opportunities. A component is present only when it can be observed in instructions, configuration, tool access, workflow state, logs or operating responsibilities.

- Name owners before the pilot.
- Define approval thresholds.
- Design escalation paths.
- Review incidents and overrides.

| Design question | Required evidence |
|---|---|
| What outcome is pursued? | Business metric and acceptance criterion |
| What may the system do? | Permission and tool contract |
| How is quality evaluated? | Tests, evaluator and human review |
| When does it stop? | Completion, escalation, budget and kill-switch rules |

| Notes 1: |
|---|
| Notes 2: |

## Topic 1 - Evolution of Business AI from Generative AI to Autonomous AI Agents

| Topic purpose: This topic develops the ability to 2023-2026 timeline · prompt to context to harness · ai-enabled business models and apply the ideas to a governed business innovation decision. |
|---|

- 2023 — generate: Copilots and chat interfaces made content generation broadly usable.
- 2024 — connect: Tool use, retrieval and multimodal models connected AI to business knowledge.
- 2025 — act: Agentic systems planned and executed multi-step work with tools and approvals.
- 2026 — operate: Persistent agents, digital workers and orchestration systems coordinate ongoing work.
- Engineering progression: Prompt engineering → context engineering → harness engineering.
- Business progression: AI feature → redesigned workflow → AI-enabled operating model.
Evidence of learning includes a completed comparison or decision worksheet, a case recommendation, the lab evidence pack and the two knowledge checks.

| Guiding question: What business decision becomes clearer after learning this topic, and what evidence would support that decision? |
|---|

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |

### 1.1 2023 — generate

| Core idea: Copilots and chat interfaces made content generation broadly usable. |
|---|

2023 — generate is useful only when it changes how a team frames a business decision. In this topic, the concept connects directly to 2023-2026 timeline · prompt to context to harness · ai-enabled business models. It gives managers a vocabulary for separating a promising demonstration from a reliable operating capability. The practical test is whether the concept helps the team describe the goal, evidence, boundary and accountable owner more precisely.

The organisation should translate the idea into process decisions: what information is needed, who supplies it, what the AI may produce or change, which outcome is measured, and where a person must approve or resolve ambiguity. This prevents technology features from becoming disconnected experiments.

- Ask what evidence would demonstrate that '2023 — generate' improves a real outcome.
- Identify the business record, system or stakeholder affected by the decision.
- Separate a reversible draft from a consequential external action.
- Name the owner who can pause, change or retire the workflow.

| Manager takeaway: Treat the concept as a design decision with evidence and ownership, not as a label. |
|---|

APPLICATION WORKSHEET

1.1 Apply 2023 — generate

Apply 2023 — generate to a workflow you know. Start with the current process before describing any AI solution. Record the trigger, inputs, decisions, systems, hand-offs, exceptions, outputs and measures. Then use the concept to propose one controlled change.

| Current workflow | AI-enabled redesign |
|---|---|
| Trigger and customer need | How intent will enter the workflow |
| Information and evidence | What context the system may use |
| Human decisions and hand-offs | What the AI prepares, recommends or executes |
| Systems and records | Tools and permissions required |
| Exceptions and failures | Escalation, retry and stop behaviour |
| Outcome and baseline | Target metric and acceptance threshold |

Application questions:

- Where does 2023 — generate create value, and where could it create new risk?
- What must be true about data, process stability and user behaviour?
- What evidence would cause the team to continue, revise or stop?
- How will the human owner understand and challenge the system's output?

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |

CONCEPT EXPLANATION

1.2 2024 — connect

| Core idea: Tool use, retrieval and multimodal models connected AI to business knowledge. |
|---|

2024 — connect is useful only when it changes how a team frames a business decision. In this topic, the concept connects directly to 2023-2026 timeline · prompt to context to harness · ai-enabled business models. It gives managers a vocabulary for separating a promising demonstration from a reliable operating capability. The practical test is whether the concept helps the team describe the goal, evidence, boundary and accountable owner more precisely.

The organisation should translate the idea into process decisions: what information is needed, who supplies it, what the AI may produce or change, which outcome is measured, and where a person must approve or resolve ambiguity. This prevents technology features from becoming disconnected experiments.

- Ask what evidence would demonstrate that '2024 — connect' improves a real outcome.
- Identify the business record, system or stakeholder affected by the decision.
- Separate a reversible draft from a consequential external action.
- Name the owner who can pause, change or retire the workflow.

| Manager takeaway: Treat the concept as a design decision with evidence and ownership, not as a label. |
|---|

APPLICATION WORKSHEET

1.2 Apply 2024 — connect

Apply 2024 — connect to a workflow you know. Start with the current process before describing any AI solution. Record the trigger, inputs, decisions, systems, hand-offs, exceptions, outputs and measures. Then use the concept to propose one controlled change.

| Current workflow | AI-enabled redesign |
|---|---|
| Trigger and customer need | How intent will enter the workflow |
| Information and evidence | What context the system may use |
| Human decisions and hand-offs | What the AI prepares, recommends or executes |
| Systems and records | Tools and permissions required |
| Exceptions and failures | Escalation, retry and stop behaviour |
| Outcome and baseline | Target metric and acceptance threshold |

Application questions:

- Where does 2024 — connect create value, and where could it create new risk?
- What must be true about data, process stability and user behaviour?
- What evidence would cause the team to continue, revise or stop?
- How will the human owner understand and challenge the system's output?

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |

CONCEPT EXPLANATION

1.3 2025 — act

| Core idea: Agentic systems planned and executed multi-step work with tools and approvals. |
|---|

2025 — act is useful only when it changes how a team frames a business decision. In this topic, the concept connects directly to 2023-2026 timeline · prompt to context to harness · ai-enabled business models. It gives managers a vocabulary for separating a promising demonstration from a reliable operating capability. The practical test is whether the concept helps the team describe the goal, evidence, boundary and accountable owner more precisely.

The organisation should translate the idea into process decisions: what information is needed, who supplies it, what the AI may produce or change, which outcome is measured, and where a person must approve or resolve ambiguity. This prevents technology features from becoming disconnected experiments.

- Ask what evidence would demonstrate that '2025 — act' improves a real outcome.
- Identify the business record, system or stakeholder affected by the decision.
- Separate a reversible draft from a consequential external action.
- Name the owner who can pause, change or retire the workflow.

| Manager takeaway: Treat the concept as a design decision with evidence and ownership, not as a label. |
|---|

APPLICATION WORKSHEET

1.3 Apply 2025 — act

Apply 2025 — act to a workflow you know. Start with the current process before describing any AI solution. Record the trigger, inputs, decisions, systems, hand-offs, exceptions, outputs and measures. Then use the concept to propose one controlled change.

| Current workflow | AI-enabled redesign |
|---|---|
| Trigger and customer need | How intent will enter the workflow |
| Information and evidence | What context the system may use |
| Human decisions and hand-offs | What the AI prepares, recommends or executes |
| Systems and records | Tools and permissions required |
| Exceptions and failures | Escalation, retry and stop behaviour |
| Outcome and baseline | Target metric and acceptance threshold |

Application questions:

- Where does 2025 — act create value, and where could it create new risk?
- What must be true about data, process stability and user behaviour?
- What evidence would cause the team to continue, revise or stop?
- How will the human owner understand and challenge the system's output?

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |

CONCEPT EXPLANATION

1.4 2026 — operate

| Core idea: Persistent agents, digital workers and orchestration systems coordinate ongoing work. |
|---|

2026 — operate is useful only when it changes how a team frames a business decision. In this topic, the concept connects directly to 2023-2026 timeline · prompt to context to harness · ai-enabled business models. It gives managers a vocabulary for separating a promising demonstration from a reliable operating capability. The practical test is whether the concept helps the team describe the goal, evidence, boundary and accountable owner more precisely.

The organisation should translate the idea into process decisions: what information is needed, who supplies it, what the AI may produce or change, which outcome is measured, and where a person must approve or resolve ambiguity. This prevents technology features from becoming disconnected experiments.

- Ask what evidence would demonstrate that '2026 — operate' improves a real outcome.
- Identify the business record, system or stakeholder affected by the decision.
- Separate a reversible draft from a consequential external action.
- Name the owner who can pause, change or retire the workflow.

| Manager takeaway: Treat the concept as a design decision with evidence and ownership, not as a label. |
|---|

APPLICATION WORKSHEET

1.4 Apply 2026 — operate

Apply 2026 — operate to a workflow you know. Start with the current process before describing any AI solution. Record the trigger, inputs, decisions, systems, hand-offs, exceptions, outputs and measures. Then use the concept to propose one controlled change.

| Current workflow | AI-enabled redesign |
|---|---|
| Trigger and customer need | How intent will enter the workflow |
| Information and evidence | What context the system may use |
| Human decisions and hand-offs | What the AI prepares, recommends or executes |
| Systems and records | Tools and permissions required |
| Exceptions and failures | Escalation, retry and stop behaviour |
| Outcome and baseline | Target metric and acceptance threshold |

Application questions:

- Where does 2026 — operate create value, and where could it create new risk?
- What must be true about data, process stability and user behaviour?
- What evidence would cause the team to continue, revise or stop?
- How will the human owner understand and challenge the system's output?

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |

CONCEPT EXPLANATION

1.5 Engineering progression

| Core idea: Prompt engineering → context engineering → harness engineering. |
|---|

Engineering progression is useful only when it changes how a team frames a business decision. In this topic, the concept connects directly to 2023-2026 timeline · prompt to context to harness · ai-enabled business models. It gives managers a vocabulary for separating a promising demonstration from a reliable operating capability. The practical test is whether the concept helps the team describe the goal, evidence, boundary and accountable owner more precisely.

The organisation should translate the idea into process decisions: what information is needed, who supplies it, what the AI may produce or change, which outcome is measured, and where a person must approve or resolve ambiguity. This prevents technology features from becoming disconnected experiments.

- Ask what evidence would demonstrate that 'Engineering progression' improves a real outcome.
- Identify the business record, system or stakeholder affected by the decision.
- Separate a reversible draft from a consequential external action.
- Name the owner who can pause, change or retire the workflow.

| Manager takeaway: Treat the concept as a design decision with evidence and ownership, not as a label. |
|---|

APPLICATION WORKSHEET

1.5 Apply Engineering progression

Apply engineering progression to a workflow you know. Start with the current process before describing any AI solution. Record the trigger, inputs, decisions, systems, hand-offs, exceptions, outputs and measures. Then use the concept to propose one controlled change.

| Current workflow | AI-enabled redesign |
|---|---|
| Trigger and customer need | How intent will enter the workflow |
| Information and evidence | What context the system may use |
| Human decisions and hand-offs | What the AI prepares, recommends or executes |
| Systems and records | Tools and permissions required |
| Exceptions and failures | Escalation, retry and stop behaviour |
| Outcome and baseline | Target metric and acceptance threshold |

Application questions:

- Where does engineering progression create value, and where could it create new risk?
- What must be true about data, process stability and user behaviour?
- What evidence would cause the team to continue, revise or stop?
- How will the human owner understand and challenge the system's output?

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |

CONCEPT EXPLANATION

1.6 Business progression

| Core idea: AI feature → redesigned workflow → AI-enabled operating model. |
|---|

Business progression is useful only when it changes how a team frames a business decision. In this topic, the concept connects directly to 2023-2026 timeline · prompt to context to harness · ai-enabled business models. It gives managers a vocabulary for separating a promising demonstration from a reliable operating capability. The practical test is whether the concept helps the team describe the goal, evidence, boundary and accountable owner more precisely.

The organisation should translate the idea into process decisions: what information is needed, who supplies it, what the AI may produce or change, which outcome is measured, and where a person must approve or resolve ambiguity. This prevents technology features from becoming disconnected experiments.

- Ask what evidence would demonstrate that 'Business progression' improves a real outcome.
- Identify the business record, system or stakeholder affected by the decision.
- Separate a reversible draft from a consequential external action.
- Name the owner who can pause, change or retire the workflow.

| Manager takeaway: Treat the concept as a design decision with evidence and ownership, not as a label. |
|---|

APPLICATION WORKSHEET

1.6 Apply Business progression

Apply business progression to a workflow you know. Start with the current process before describing any AI solution. Record the trigger, inputs, decisions, systems, hand-offs, exceptions, outputs and measures. Then use the concept to propose one controlled change.

| Current workflow | AI-enabled redesign |
|---|---|
| Trigger and customer need | How intent will enter the workflow |
| Information and evidence | What context the system may use |
| Human decisions and hand-offs | What the AI prepares, recommends or executes |
| Systems and records | Tools and permissions required |
| Exceptions and failures | Escalation, retry and stop behaviour |
| Outcome and baseline | Target metric and acceptance threshold |

Application questions:

- Where does business progression create value, and where could it create new risk?
- What must be true about data, process stability and user behaviour?
- What evidence would cause the team to continue, revise or stop?
- How will the human owner understand and challenge the system's output?

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |

### 1.F1 AI maturity ladder

| Framework definition: Classify an initiative as assistive, connected, agentic or operational. Maturity is determined by responsibility, access and persistence - not by marketing language. |
|---|

When to use it: Use the ladder to prevent a content-generation pilot from being governed as if it could change business records.

Watch for: A common failure is granting autonomy before the process, data and escalation path are stable.

A useful framework reduces ambiguity. It should allow two people to examine the same opportunity, state their assumptions and reach a traceable decision. Apply it with representative examples rather than idealised demonstrations.

- Define the unit of analysis: task, workflow, customer journey or operating model.
- Record assumptions separately from verified evidence.
- Use a simple rating scale with written justification.
- Review disagreements; they often reveal missing data or different risk tolerances.
- Assign a next action and owner before closing the discussion.

| Diagnostic question | Evidence to collect |
|---|---|
| What problem does this framework clarify? | Baseline process map, delay, error or cost data |
| What decision follows? | Pilot, preparation, redesign, defer or stop |
| Who owns the decision? | Named business and technology owners |
| When is it reviewed? | Gate date, metric threshold and review cadence |

BUSINESS FRAMEWORK

1.F2 Engineering progression

| Framework definition: Prompt engineering shapes a request; context engineering curates the working set; harness engineering shapes the environment in which an agent acts. |
|---|

When to use it: Use the progression to diagnose whether a weak result comes from wording, missing context or an unsafe execution environment.

Watch for: A longer prompt cannot compensate for missing evidence, unclear tool contracts or absent approvals.

A useful framework reduces ambiguity. It should allow two people to examine the same opportunity, state their assumptions and reach a traceable decision. Apply it with representative examples rather than idealised demonstrations.

- Define the unit of analysis: task, workflow, customer journey or operating model.
- Record assumptions separately from verified evidence.
- Use a simple rating scale with written justification.
- Review disagreements; they often reveal missing data or different risk tolerances.
- Assign a next action and owner before closing the discussion.

| Diagnostic question | Evidence to collect |
|---|---|
| What problem does this framework clarify? | Baseline process map, delay, error or cost data |
| What decision follows? | Pilot, preparation, redesign, defer or stop |
| Who owns the decision? | Named business and technology owners |
| When is it reviewed? | Gate date, metric threshold and review cadence |

BUSINESS FRAMEWORK

1.F3 Business-model redesign

| Framework definition: Examine value proposition, customer interface, key activities, resources, partners, revenue and cost through an AI-enabled lens. |
|---|

When to use it: Use this framework when AI changes how value is delivered rather than merely making one task faster.

Watch for: Do not automate an inefficient hand-off and call it innovation; redesign the flow and ownership.

A useful framework reduces ambiguity. It should allow two people to examine the same opportunity, state their assumptions and reach a traceable decision. Apply it with representative examples rather than idealised demonstrations.

- Define the unit of analysis: task, workflow, customer journey or operating model.
- Record assumptions separately from verified evidence.
- Use a simple rating scale with written justification.
- Review disagreements; they often reveal missing data or different risk tolerances.
- Assign a next action and owner before closing the discussion.

| Diagnostic question | Evidence to collect |
|---|---|
| What problem does this framework clarify? | Baseline process map, delay, error or cost data |
| What decision follows? | Pilot, preparation, redesign, defer or stop |
| Who owns the decision? | Named business and technology owners |
| When is it reviewed? | Gate date, metric threshold and review cadence |

BUSINESS FRAMEWORK

1.F4 Human-AI operating model

| Framework definition: Allocate intent, judgement, repetition, approval, exception handling and accountability deliberately between people and systems. |
|---|

When to use it: Use role clarity to show where an agent may recommend, prepare, execute or escalate.

Watch for: Avoid vague statements such as 'the AI handles it'; name the owner and approval threshold.

A useful framework reduces ambiguity. It should allow two people to examine the same opportunity, state their assumptions and reach a traceable decision. Apply it with representative examples rather than idealised demonstrations.

- Define the unit of analysis: task, workflow, customer journey or operating model.
- Record assumptions separately from verified evidence.
- Use a simple rating scale with written justification.
- Review disagreements; they often reveal missing data or different risk tolerances.
- Assign a next action and owner before closing the discussion.

| Diagnostic question | Evidence to collect |
|---|---|
| What problem does this framework clarify? | Baseline process map, delay, error or cost data |
| What decision follows? | Pilot, preparation, redesign, defer or stop |
| Who owns the decision? | Named business and technology owners |
| When is it reviewed? | Gate date, metric threshold and review cadence |

### Case 1.1 - From campaign brief to approved video

| Scenario: A retail SME needs weekly product videos but has a two-week agency cycle. The team trials Gemini/Veo for first drafts while brand and legal reviewers retain approval. |
|---|

Your assignment: Map the old and AI-enabled value chains. Identify new capabilities, costs, risks and human decisions.

- State the business outcome in one sentence without naming a technology.
- Identify the current bottleneck and quantify it with a baseline or a measurement plan.
- Choose the appropriate AI approach and justify the boundary of action.
- Specify context, tools, memory and human oversight only if the workflow requires them.
- List one normal case, one edge case, one malicious case and one tool-failure case.
- Recommend pilot, prepare, redesign, defer or stop, with evidence required for the next decision.

| Decision area | Your analysis |
|---|---|
| Value and stakeholder impact |  |
| Feasibility and dependencies |  |
| Risks and prohibited actions |  |
| Controls and human owner |  |
| Measures and gate decision |  |

| Discussion prompt: How would the recommendation change if the workflow moved from internal use to a customer-facing channel? Relate your answer to Topic 1. |
|---|

WORKED BUSINESS CASE

Case 1.2 - Service operations redesign

| Scenario: A facilities company receives requests by email and relies on coordinators to copy data into three systems. |
|---|

Your assignment: Describe the difference between adding a drafting assistant and redesigning the operating model around a governed agent.

- State the business outcome in one sentence without naming a technology.
- Identify the current bottleneck and quantify it with a baseline or a measurement plan.
- Choose the appropriate AI approach and justify the boundary of action.
- Specify context, tools, memory and human oversight only if the workflow requires them.
- List one normal case, one edge case, one malicious case and one tool-failure case.
- Recommend pilot, prepare, redesign, defer or stop, with evidence required for the next decision.

| Decision area | Your analysis |
|---|---|
| Value and stakeholder impact |  |
| Feasibility and dependencies |  |
| Risks and prohibited actions |  |
| Controls and human owner |  |
| Measures and gate decision |  |

| Discussion prompt: How would the recommendation change if the workflow moved from internal use to a customer-facing channel? Relate your answer to Topic 1. |
|---|

WORKED BUSINESS CASE

Case 1.3 - The autonomy claim

| Scenario: A vendor calls its chatbot an autonomous digital employee, but it has no tools, memory or persistent task state. |
|---|

Your assignment: Use the maturity ladder and agent definition to challenge the claim with evidence.

- State the business outcome in one sentence without naming a technology.
- Identify the current bottleneck and quantify it with a baseline or a measurement plan.
- Choose the appropriate AI approach and justify the boundary of action.
- Specify context, tools, memory and human oversight only if the workflow requires them.
- List one normal case, one edge case, one malicious case and one tool-failure case.
- Recommend pilot, prepare, redesign, defer or stop, with evidence required for the next decision.

| Decision area | Your analysis |
|---|---|
| Value and stakeholder impact |  |
| Feasibility and dependencies |  |
| Risks and prohibited actions |  |
| Controls and human owner |  |
| Measures and gate decision |  |

| Discussion prompt: How would the recommendation change if the workflow moved from internal use to a customer-facing channel? Relate your answer to Topic 1. |
|---|

### Lab 1 - Create a Business Story Video with Gemini

| Goal: Create a short business-innovation video with Gemini/Veo, then compare the human decisions, cycle time and controls with a conventional production process. |
|---|

Alignment: LO1 · Topic 1

Deliverable: A 6–8 second business story video, prompt record and before/after workflow comparison

Tools: Gemini, Veo video generation, browser download

| Configuration / constraint | Required evidence |
|---|---|
| Output: 16:9 video lasting approximately 6-8 seconds. | Record the configured value or resulting evidence. |
| Review people, text, logos, claims, brand fit and unintended personal data before approval. | Record the configured value or resulting evidence. |
| Record the prompt, model/service, date, reviewer and approval decision. | Record the configured value or resulting evidence. |

- Use only non-confidential training data and approved accounts.
- Record the source, model or service, date, prompt or instruction, tool actions and human approval.
- Stop if access, permissions, pricing or the active interface differs materially from the guide.
- Do not connect production credentials or send external communications during the lab.

| Acceptance standard: The clip plays, matches the brief, contains no invented brand claims, and the comparison explains how generative AI changes cycle time without removing human accountability. |
|---|

LAB DESIGN

Lab 1 - Workflow and Control Design

| Stage | Lab decision |
|---|---|
| Intent | State the business outcome and exclusions |
| Context | Supply only relevant, approved information |
| Action | Generate, reason or call a scoped tool |
| Observation | Capture output, status and evidence |
| Evaluation | Compare with acceptance criteria |
| Decision | Complete, improve, stop or escalate |

Control boundary:

| Control boundary: The learner may generate and download a draft, but a person approves claims, brand fit and final use. |
|---|

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |

STEP-BY-STEP

Lab 1 - Guided Procedure 1 of 3

#### Step 1

Open Gemini, choose video generation and confirm your account has Veo access.

- Expected result: the interface or command reports a successful, reviewable state.
- Evidence: capture the relevant screen, execution record, file or diff without exposing secrets.
- If different: stop, confirm the current product interface and resolve permissions before continuing.

#### Step 2

Write a shot brief covering subject, setting, action, camera, lighting, audio and exclusions.

- Expected result: the interface or command reports a successful, reviewable state.
- Evidence: capture the relevant screen, execution record, file or diff without exposing secrets.
- If different: stop, confirm the current product interface and resolve permissions before continuing.

| Checkpoint: Explain what changed, what evidence proves it, and whether any external state was affected. |
|---|

STEP-BY-STEP

Lab 1 - Guided Procedure 2 of 3

#### Step 3

Generate a 16:9 video for a Singapore SME introducing an AI-assisted service workflow.

- Expected result: the interface or command reports a successful, reviewable state.
- Evidence: capture the relevant screen, execution record, file or diff without exposing secrets.
- If different: stop, confirm the current product interface and resolve permissions before continuing.

#### Step 4

Review accuracy, brand safety and unwanted text; revise one variable at a time.

- Expected result: the interface or command reports a successful, reviewable state.
- Evidence: capture the relevant screen, execution record, file or diff without exposing secrets.
- If different: stop, confirm the current product interface and resolve permissions before continuing.

| Checkpoint: Explain what changed, what evidence proves it, and whether any external state was affected. |
|---|

STEP-BY-STEP

Lab 1 - Guided Procedure 3 of 3

#### Step 5

Download the final clip and record the prompt, model, date and human approval decision.

- Expected result: the interface or command reports a successful, reviewable state.
- Evidence: capture the relevant screen, execution record, file or diff without exposing secrets.
- If different: stop, confirm the current product interface and resolve permissions before continuing.

#### Step 6

Map the old and AI-enabled production workflows, including where human judgement remains.

- Expected result: the interface or command reports a successful, reviewable state.
- Evidence: capture the relevant screen, execution record, file or diff without exposing secrets.
- If different: stop, confirm the current product interface and resolve permissions before continuing.

| Checkpoint: Explain what changed, what evidence proves it, and whether any external state was affected. |
|---|

COPY-PASTE BRIEF

Lab 1 - Instructions, Prompt and Source Boundary

| Copy-paste prompt: Create a 16:9, 6-8 second cinematic video for a Singapore SME. Show an operations coordinator reviewing an AI-assisted service dashboard, then approving a customer update. Use natural daylight, realistic people and calm camera movement. Do not show logos, readable personal data, invented performance claims, distorted hands or unreadable text. |
|---|

Review the brief before use. Replace only the scenario-specific details; preserve the source boundary, prohibited actions, output contract and escalation rule.

| Instruction component | Why it matters |
|---|---|
| Outcome and audience | Prevents a fluent but unusable deliverable |
| Approved source boundary | Reduces unsupported claims and privacy exposure |
| Required output structure | Makes results reviewable and machine-checkable |
| Prohibited actions | Blocks unsafe interpretation of a broad goal |
| Approval and stop conditions | Keeps accountability with the named person |

| Notes 1: |
|---|
| Notes 2: |

VERIFY BEFORE ACCEPTING

Lab 1 - Test Plan and Failure Cases

| Test case | Expected controlled behaviour |
|---|---|
| Normal | Clear SME scene with no sensitive information |
| Edge | Complex action or small text that may distort |
| Risk | Invented brand claim or recognisable personal data |
| Service failure | Video generation unavailable or quota exceeded |

- Record actual result, evidence and pass/fail status for every test.
- A failure is useful evidence; do not hide it by changing the expected result after the run.
- Do not retry a consequential action unless the system proves the first attempt had no effect.
- Escalate when the result is uncertain or the acceptance criterion cannot be observed.

| Acceptance criterion: The clip plays, matches the brief, contains no invented brand claims, and the comparison explains how generative AI changes cycle time without removing human accountability. |
|---|

COMPLETE THE ACTIVITY

Lab 1 - Evidence Pack and Reflection

- Business brief and baseline problem statement.
- Prompt or instruction version and approved source list.
- Screenshots or execution records showing the workflow and controls.
- Test results for normal, edge, malicious and tool-failure cases.
- Human review decision, outstanding risks and next recommended gate.
Reference tool view for Lab 1

| Reflection: Which part was generation, which part was agentic behaviour, and which part belonged to the harness? What would need to change before production use? |
|---|

| Notes 1: |
|---|
| Notes 2: |

RETRIEVAL PRACTICE

Topic 1 - Knowledge Check

1. Explain the central business decision in evolution of business ai from generative ai to autonomous ai agents.

Response: ______________________________________________________________________

________________________________________________________________________________

2. Distinguish the AI capability from the workflow and the deployed agent system.

Response: ______________________________________________________________________

________________________________________________________________________________

3. Name two forms of evidence that would support a pilot decision.

Response: ______________________________________________________________________

________________________________________________________________________________

4. Identify one consequential action and the human approval it requires.

Response: ______________________________________________________________________

________________________________________________________________________________

5. Describe one failure case and the control that should contain it.

Response: ______________________________________________________________________

________________________________________________________________________________

6. State one metric that measures business value and one that measures operational safety.

Response: ______________________________________________________________________

________________________________________________________________________________

SCENARIO QUESTIONS

Topic 1 - Applied Review

| Scenario: A retail SME needs weekly product videos but has a two-week agency cycle. The team trials Gemini/Veo for first drafts while brand and legal reviewers retain approval. |
|---|

- What outcome should be measured before any technology is selected?
- Which AI approach is proportionate to the task and why?
- What context and evidence are necessary? What information should be excluded?
- Which tool actions are reversible, and which require explicit approval?
- What should the agent do after an ambiguous result or failed tool call?
- Which gate should the initiative pass next, and what evidence is still missing?

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |
| Notes 4: |
| Notes 5: |

TRANSFER TO PRACTICE

Topic 1 - Workplace Action Plan

| Action: Choose one non-confidential workflow and identify a small, measurable next step that applies this topic without granting unnecessary authority. |
|---|

| Planning field | Your decision |
|---|---|
| Workflow and owner |  |
| Current baseline |  |
| Proposed AI contribution |  |
| Source and tool boundary |  |
| Human approval |  |
| Test and success measure |  |
| Next review date |  |

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |

## Topic 2 - Generative AI, Agentic AI and AI Agent Technologies

| Topic purpose: This topic develops the ability to llms · models, workflows and agents · n8n · claude code · codex · openclaw · hermes · paperclip and apply the ideas to a governed business innovation decision. |
|---|

- Generative AI: Produces a response or artifact from a prompt; the user drives each turn.
- Agentic AI: Uses goals, state, tools and feedback to complete a multi-step outcome.
- AI agent: A deployed system with model, instructions, memory, tools, skills and execution loop.
- Workflow agent: n8n combines deterministic nodes, AI decisions and human approvals.
- Coding agents: Claude Code and Codex inspect repositories, edit files, run tools and verify results.
- Autonomous runtimes: OpenClaw and Hermes persist across channels; Paperclip coordinates teams of agents.
Evidence of learning includes a completed comparison or decision worksheet, a case recommendation, the lab evidence pack and the two knowledge checks.

| Guiding question: What business decision becomes clearer after learning this topic, and what evidence would support that decision? |
|---|

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |

### 2.1 Generative AI

| Core idea: Produces a response or artifact from a prompt; the user drives each turn. |
|---|

Generative AI is useful only when it changes how a team frames a business decision. In this topic, the concept connects directly to llms · models, workflows and agents · n8n · claude code · codex · openclaw · hermes · paperclip. It gives managers a vocabulary for separating a promising demonstration from a reliable operating capability. The practical test is whether the concept helps the team describe the goal, evidence, boundary and accountable owner more precisely.

The organisation should translate the idea into process decisions: what information is needed, who supplies it, what the AI may produce or change, which outcome is measured, and where a person must approve or resolve ambiguity. This prevents technology features from becoming disconnected experiments.

- Ask what evidence would demonstrate that 'Generative AI' improves a real outcome.
- Identify the business record, system or stakeholder affected by the decision.
- Separate a reversible draft from a consequential external action.
- Name the owner who can pause, change or retire the workflow.

| Manager takeaway: Treat the concept as a design decision with evidence and ownership, not as a label. |
|---|

APPLICATION WORKSHEET

2.1 Apply Generative AI

Apply generative ai to a workflow you know. Start with the current process before describing any AI solution. Record the trigger, inputs, decisions, systems, hand-offs, exceptions, outputs and measures. Then use the concept to propose one controlled change.

| Current workflow | AI-enabled redesign |
|---|---|
| Trigger and customer need | How intent will enter the workflow |
| Information and evidence | What context the system may use |
| Human decisions and hand-offs | What the AI prepares, recommends or executes |
| Systems and records | Tools and permissions required |
| Exceptions and failures | Escalation, retry and stop behaviour |
| Outcome and baseline | Target metric and acceptance threshold |

Application questions:

- Where does generative ai create value, and where could it create new risk?
- What must be true about data, process stability and user behaviour?
- What evidence would cause the team to continue, revise or stop?
- How will the human owner understand and challenge the system's output?

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |

CONCEPT EXPLANATION

2.2 Agentic AI

| Core idea: Uses goals, state, tools and feedback to complete a multi-step outcome. |
|---|

Agentic AI is useful only when it changes how a team frames a business decision. In this topic, the concept connects directly to llms · models, workflows and agents · n8n · claude code · codex · openclaw · hermes · paperclip. It gives managers a vocabulary for separating a promising demonstration from a reliable operating capability. The practical test is whether the concept helps the team describe the goal, evidence, boundary and accountable owner more precisely.

The organisation should translate the idea into process decisions: what information is needed, who supplies it, what the AI may produce or change, which outcome is measured, and where a person must approve or resolve ambiguity. This prevents technology features from becoming disconnected experiments.

- Ask what evidence would demonstrate that 'Agentic AI' improves a real outcome.
- Identify the business record, system or stakeholder affected by the decision.
- Separate a reversible draft from a consequential external action.
- Name the owner who can pause, change or retire the workflow.

| Manager takeaway: Treat the concept as a design decision with evidence and ownership, not as a label. |
|---|

APPLICATION WORKSHEET

2.2 Apply Agentic AI

Apply agentic ai to a workflow you know. Start with the current process before describing any AI solution. Record the trigger, inputs, decisions, systems, hand-offs, exceptions, outputs and measures. Then use the concept to propose one controlled change.

| Current workflow | AI-enabled redesign |
|---|---|
| Trigger and customer need | How intent will enter the workflow |
| Information and evidence | What context the system may use |
| Human decisions and hand-offs | What the AI prepares, recommends or executes |
| Systems and records | Tools and permissions required |
| Exceptions and failures | Escalation, retry and stop behaviour |
| Outcome and baseline | Target metric and acceptance threshold |

Application questions:

- Where does agentic ai create value, and where could it create new risk?
- What must be true about data, process stability and user behaviour?
- What evidence would cause the team to continue, revise or stop?
- How will the human owner understand and challenge the system's output?

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |

CONCEPT EXPLANATION

2.3 AI agent

| Core idea: A deployed system with model, instructions, memory, tools, skills and execution loop. |
|---|

AI agent is useful only when it changes how a team frames a business decision. In this topic, the concept connects directly to llms · models, workflows and agents · n8n · claude code · codex · openclaw · hermes · paperclip. It gives managers a vocabulary for separating a promising demonstration from a reliable operating capability. The practical test is whether the concept helps the team describe the goal, evidence, boundary and accountable owner more precisely.

The organisation should translate the idea into process decisions: what information is needed, who supplies it, what the AI may produce or change, which outcome is measured, and where a person must approve or resolve ambiguity. This prevents technology features from becoming disconnected experiments.

- Ask what evidence would demonstrate that 'AI agent' improves a real outcome.
- Identify the business record, system or stakeholder affected by the decision.
- Separate a reversible draft from a consequential external action.
- Name the owner who can pause, change or retire the workflow.

| Manager takeaway: Treat the concept as a design decision with evidence and ownership, not as a label. |
|---|

APPLICATION WORKSHEET

2.3 Apply AI agent

Apply ai agent to a workflow you know. Start with the current process before describing any AI solution. Record the trigger, inputs, decisions, systems, hand-offs, exceptions, outputs and measures. Then use the concept to propose one controlled change.

| Current workflow | AI-enabled redesign |
|---|---|
| Trigger and customer need | How intent will enter the workflow |
| Information and evidence | What context the system may use |
| Human decisions and hand-offs | What the AI prepares, recommends or executes |
| Systems and records | Tools and permissions required |
| Exceptions and failures | Escalation, retry and stop behaviour |
| Outcome and baseline | Target metric and acceptance threshold |

Application questions:

- Where does ai agent create value, and where could it create new risk?
- What must be true about data, process stability and user behaviour?
- What evidence would cause the team to continue, revise or stop?
- How will the human owner understand and challenge the system's output?

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |

CONCEPT EXPLANATION

2.4 Workflow agent

| Core idea: n8n combines deterministic nodes, AI decisions and human approvals. |
|---|

Workflow agent is useful only when it changes how a team frames a business decision. In this topic, the concept connects directly to llms · models, workflows and agents · n8n · claude code · codex · openclaw · hermes · paperclip. It gives managers a vocabulary for separating a promising demonstration from a reliable operating capability. The practical test is whether the concept helps the team describe the goal, evidence, boundary and accountable owner more precisely.

The organisation should translate the idea into process decisions: what information is needed, who supplies it, what the AI may produce or change, which outcome is measured, and where a person must approve or resolve ambiguity. This prevents technology features from becoming disconnected experiments.

- Ask what evidence would demonstrate that 'Workflow agent' improves a real outcome.
- Identify the business record, system or stakeholder affected by the decision.
- Separate a reversible draft from a consequential external action.
- Name the owner who can pause, change or retire the workflow.

| Manager takeaway: Treat the concept as a design decision with evidence and ownership, not as a label. |
|---|

APPLICATION WORKSHEET

2.4 Apply Workflow agent

Apply workflow agent to a workflow you know. Start with the current process before describing any AI solution. Record the trigger, inputs, decisions, systems, hand-offs, exceptions, outputs and measures. Then use the concept to propose one controlled change.

| Current workflow | AI-enabled redesign |
|---|---|
| Trigger and customer need | How intent will enter the workflow |
| Information and evidence | What context the system may use |
| Human decisions and hand-offs | What the AI prepares, recommends or executes |
| Systems and records | Tools and permissions required |
| Exceptions and failures | Escalation, retry and stop behaviour |
| Outcome and baseline | Target metric and acceptance threshold |

Application questions:

- Where does workflow agent create value, and where could it create new risk?
- What must be true about data, process stability and user behaviour?
- What evidence would cause the team to continue, revise or stop?
- How will the human owner understand and challenge the system's output?

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |

CONCEPT EXPLANATION

2.5 Coding agents

| Core idea: Claude Code and Codex inspect repositories, edit files, run tools and verify results. |
|---|

Coding agents is useful only when it changes how a team frames a business decision. In this topic, the concept connects directly to llms · models, workflows and agents · n8n · claude code · codex · openclaw · hermes · paperclip. It gives managers a vocabulary for separating a promising demonstration from a reliable operating capability. The practical test is whether the concept helps the team describe the goal, evidence, boundary and accountable owner more precisely.

The organisation should translate the idea into process decisions: what information is needed, who supplies it, what the AI may produce or change, which outcome is measured, and where a person must approve or resolve ambiguity. This prevents technology features from becoming disconnected experiments.

- Ask what evidence would demonstrate that 'Coding agents' improves a real outcome.
- Identify the business record, system or stakeholder affected by the decision.
- Separate a reversible draft from a consequential external action.
- Name the owner who can pause, change or retire the workflow.

| Manager takeaway: Treat the concept as a design decision with evidence and ownership, not as a label. |
|---|

APPLICATION WORKSHEET

2.5 Apply Coding agents

Apply coding agents to a workflow you know. Start with the current process before describing any AI solution. Record the trigger, inputs, decisions, systems, hand-offs, exceptions, outputs and measures. Then use the concept to propose one controlled change.

| Current workflow | AI-enabled redesign |
|---|---|
| Trigger and customer need | How intent will enter the workflow |
| Information and evidence | What context the system may use |
| Human decisions and hand-offs | What the AI prepares, recommends or executes |
| Systems and records | Tools and permissions required |
| Exceptions and failures | Escalation, retry and stop behaviour |
| Outcome and baseline | Target metric and acceptance threshold |

Application questions:

- Where does coding agents create value, and where could it create new risk?
- What must be true about data, process stability and user behaviour?
- What evidence would cause the team to continue, revise or stop?
- How will the human owner understand and challenge the system's output?

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |

CONCEPT EXPLANATION

2.6 Autonomous runtimes

| Core idea: OpenClaw and Hermes persist across channels; Paperclip coordinates teams of agents. |
|---|

Autonomous runtimes is useful only when it changes how a team frames a business decision. In this topic, the concept connects directly to llms · models, workflows and agents · n8n · claude code · codex · openclaw · hermes · paperclip. It gives managers a vocabulary for separating a promising demonstration from a reliable operating capability. The practical test is whether the concept helps the team describe the goal, evidence, boundary and accountable owner more precisely.

The organisation should translate the idea into process decisions: what information is needed, who supplies it, what the AI may produce or change, which outcome is measured, and where a person must approve or resolve ambiguity. This prevents technology features from becoming disconnected experiments.

- Ask what evidence would demonstrate that 'Autonomous runtimes' improves a real outcome.
- Identify the business record, system or stakeholder affected by the decision.
- Separate a reversible draft from a consequential external action.
- Name the owner who can pause, change or retire the workflow.

| Manager takeaway: Treat the concept as a design decision with evidence and ownership, not as a label. |
|---|

APPLICATION WORKSHEET

2.6 Apply Autonomous runtimes

Apply autonomous runtimes to a workflow you know. Start with the current process before describing any AI solution. Record the trigger, inputs, decisions, systems, hand-offs, exceptions, outputs and measures. Then use the concept to propose one controlled change.

| Current workflow | AI-enabled redesign |
|---|---|
| Trigger and customer need | How intent will enter the workflow |
| Information and evidence | What context the system may use |
| Human decisions and hand-offs | What the AI prepares, recommends or executes |
| Systems and records | Tools and permissions required |
| Exceptions and failures | Escalation, retry and stop behaviour |
| Outcome and baseline | Target metric and acceptance threshold |

Application questions:

- Where does autonomous runtimes create value, and where could it create new risk?
- What must be true about data, process stability and user behaviour?
- What evidence would cause the team to continue, revise or stop?
- How will the human owner understand and challenge the system's output?

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |

### 2.F1 Capability-behaviour-system taxonomy

| Framework definition: Generative AI is a capability, agentic AI is goal-directed behaviour, and an AI agent is the deployed system that packages model, context, memory, tools and loop. |
|---|

When to use it: Use the taxonomy to compare products without confusing a chatbot response with an operational agent.

Watch for: Do not infer autonomy from fluent language; inspect tools, state, persistence and permissions.

A useful framework reduces ambiguity. It should allow two people to examine the same opportunity, state their assumptions and reach a traceable decision. Apply it with representative examples rather than idealised demonstrations.

- Define the unit of analysis: task, workflow, customer journey or operating model.
- Record assumptions separately from verified evidence.
- Use a simple rating scale with written justification.
- Review disagreements; they often reveal missing data or different risk tolerances.
- Assign a next action and owner before closing the discussion.

| Diagnostic question | Evidence to collect |
|---|---|
| What problem does this framework clarify? | Baseline process map, delay, error or cost data |
| What decision follows? | Pilot, preparation, redesign, defer or stop |
| Who owns the decision? | Named business and technology owners |
| When is it reviewed? | Gate date, metric threshold and review cadence |

BUSINESS FRAMEWORK

2.F2 Agent architecture stack

| Framework definition: Map goal, instructions, context, reasoning, memory, tools, skills, channels, loop, evaluator and human oversight. |
|---|

When to use it: Use the stack to find missing components before selecting a platform.

Watch for: Adding more tools can increase risk and ambiguity; every tool needs a contract and owner.

A useful framework reduces ambiguity. It should allow two people to examine the same opportunity, state their assumptions and reach a traceable decision. Apply it with representative examples rather than idealised demonstrations.

- Define the unit of analysis: task, workflow, customer journey or operating model.
- Record assumptions separately from verified evidence.
- Use a simple rating scale with written justification.
- Review disagreements; they often reveal missing data or different risk tolerances.
- Assign a next action and owner before closing the discussion.

| Diagnostic question | Evidence to collect |
|---|---|
| What problem does this framework clarify? | Baseline process map, delay, error or cost data |
| What decision follows? | Pilot, preparation, redesign, defer or stop |
| Who owns the decision? | Named business and technology owners |
| When is it reviewed? | Gate date, metric threshold and review cadence |

BUSINESS FRAMEWORK

2.F3 Technology selection matrix

| Framework definition: Match the work boundary to generation, deterministic workflow, coding-agent, knowledge-worker or persistent digital-worker technology. |
|---|

When to use it: Use a matrix of task variability, integrations, persistence, consequence and required evidence.

Watch for: Avoid choosing a fashionable tool before defining the business outcome and control boundary.

A useful framework reduces ambiguity. It should allow two people to examine the same opportunity, state their assumptions and reach a traceable decision. Apply it with representative examples rather than idealised demonstrations.

- Define the unit of analysis: task, workflow, customer journey or operating model.
- Record assumptions separately from verified evidence.
- Use a simple rating scale with written justification.
- Review disagreements; they often reveal missing data or different risk tolerances.
- Assign a next action and owner before closing the discussion.

| Diagnostic question | Evidence to collect |
|---|---|
| What problem does this framework clarify? | Baseline process map, delay, error or cost data |
| What decision follows? | Pilot, preparation, redesign, defer or stop |
| Who owns the decision? | Named business and technology owners |
| When is it reviewed? | Gate date, metric threshold and review cadence |

BUSINESS FRAMEWORK

2.F4 Digital-worker boundary

| Framework definition: Define what the worker may read, draft, decide, change, communicate and remember. |
|---|

When to use it: Use the boundary as a practical contract between business owner, technology owner and users.

Watch for: Never treat an agent account as an unnamed employee; access and accountability must remain attributable.

A useful framework reduces ambiguity. It should allow two people to examine the same opportunity, state their assumptions and reach a traceable decision. Apply it with representative examples rather than idealised demonstrations.

- Define the unit of analysis: task, workflow, customer journey or operating model.
- Record assumptions separately from verified evidence.
- Use a simple rating scale with written justification.
- Review disagreements; they often reveal missing data or different risk tolerances.
- Assign a next action and owner before closing the discussion.

| Diagnostic question | Evidence to collect |
|---|---|
| What problem does this framework clarify? | Baseline process map, delay, error or cost data |
| What decision follows? | Pilot, preparation, redesign, defer or stop |
| Who owns the decision? | Named business and technology owners |
| When is it reviewed? | Gate date, metric threshold and review cadence |

### Case 2.1 - Lead triage portfolio

| Scenario: A sales team needs structured intake, classification, CRM updates and manager approval for high-value leads. |
|---|

Your assignment: Compare n8n, a general chat assistant and a persistent agent against the required work boundary.

- State the business outcome in one sentence without naming a technology.
- Identify the current bottleneck and quantify it with a baseline or a measurement plan.
- Choose the appropriate AI approach and justify the boundary of action.
- Specify context, tools, memory and human oversight only if the workflow requires them.
- List one normal case, one edge case, one malicious case and one tool-failure case.
- Recommend pilot, prepare, redesign, defer or stop, with evidence required for the next decision.

| Decision area | Your analysis |
|---|---|
| Value and stakeholder impact |  |
| Feasibility and dependencies |  |
| Risks and prohibited actions |  |
| Controls and human owner |  |
| Measures and gate decision |  |

| Discussion prompt: How would the recommendation change if the workflow moved from internal use to a customer-facing channel? Relate your answer to Topic 2. |
|---|

WORKED BUSINESS CASE

Case 2.2 - Repository modernisation

| Scenario: A product team needs an agent to inspect code, implement a change, run tests and prepare a reviewable diff. |
|---|

Your assignment: Compare Claude Code and Codex using context, tool, verification and human-control requirements.

- State the business outcome in one sentence without naming a technology.
- Identify the current bottleneck and quantify it with a baseline or a measurement plan.
- Choose the appropriate AI approach and justify the boundary of action.
- Specify context, tools, memory and human oversight only if the workflow requires them.
- List one normal case, one edge case, one malicious case and one tool-failure case.
- Recommend pilot, prepare, redesign, defer or stop, with evidence required for the next decision.

| Decision area | Your analysis |
|---|---|
| Value and stakeholder impact |  |
| Feasibility and dependencies |  |
| Risks and prohibited actions |  |
| Controls and human owner |  |
| Measures and gate decision |  |

| Discussion prompt: How would the recommendation change if the workflow moved from internal use to a customer-facing channel? Relate your answer to Topic 2. |
|---|

WORKED BUSINESS CASE

Case 2.3 - Always-on operations assistant

| Scenario: A manager wants one agent reachable from chat and terminal that remembers approved preferences and runs scheduled briefings. |
|---|

Your assignment: Evaluate whether OpenClaw, Hermes Agent or a deterministic workflow is the better fit.

- State the business outcome in one sentence without naming a technology.
- Identify the current bottleneck and quantify it with a baseline or a measurement plan.
- Choose the appropriate AI approach and justify the boundary of action.
- Specify context, tools, memory and human oversight only if the workflow requires them.
- List one normal case, one edge case, one malicious case and one tool-failure case.
- Recommend pilot, prepare, redesign, defer or stop, with evidence required for the next decision.

| Decision area | Your analysis |
|---|---|
| Value and stakeholder impact |  |
| Feasibility and dependencies |  |
| Risks and prohibited actions |  |
| Controls and human owner |  |
| Measures and gate decision |  |

| Discussion prompt: How would the recommendation change if the workflow moved from internal use to a customer-facing channel? Relate your answer to Topic 2. |
|---|

### Lab 2 - Build an Agentic Lead-Triage Workflow in n8n

| Goal: Build a controlled n8n workflow that receives a lead, asks an AI agent to classify intent and urgency, routes the result, records the decision and pauses high-value actions for approval. |
|---|

Alignment: LO2-LO3 · Topic 2

Deliverable: A lead-triage workflow with structured AI output, deterministic routing, audit data and human approval

Tools: n8n Form Trigger, AI Agent, Chat Model, Structured Output Parser, Switch, Data Table

| Configuration / constraint | Required evidence |
|---|---|
| Input fields: name, company, email, enquiry and expected budget. | Record the configured value or resulting evidence. |
| Structured output: category, urgency, confidence, rationale and next_action. | Record the configured value or resulting evidence. |
| Use structured-output-schema.json and lead-triage-test-cases.csv supplied with this lab. | Record the configured value or resulting evidence. |
| Deterministic nodes route the validated result; the model never chooses an unlisted destination. | Record the configured value or resulting evidence. |

- Use only non-confidential training data and approved accounts.
- Record the source, model or service, date, prompt or instruction, tool actions and human approval.
- Stop if access, permissions, pricing or the active interface differs materially from the guide.
- Do not connect production credentials or send external communications during the lab.

| Acceptance standard: All four test leads finish in the expected branch, every decision is logged, low-confidence or consequential actions require approval, and no unapproved external message is sent. |
|---|

LAB DESIGN

Lab 2 - Workflow and Control Design

| Stage | Lab decision |
|---|---|
| Intent | State the business outcome and exclusions |
| Context | Supply only relevant, approved information |
| Action | Generate, reason or call a scoped tool |
| Observation | Capture output, status and evidence |
| Evaluation | Compare with acceptance criteria |
| Decision | Complete, improve, stop or escalate |

Control boundary:

| Control boundary: The model classifies to a schema; deterministic nodes route; uncertain or high-value cases require approval. |
|---|

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |

STEP-BY-STEP

Lab 2 - Guided Procedure 1 of 3

#### Step 1

Create a Form Trigger with name, company, email, enquiry and expected budget fields.

- Expected result: the interface or command reports a successful, reviewable state.
- Evidence: capture the relevant screen, execution record, file or diff without exposing secrets.
- If different: stop, confirm the current product interface and resolve permissions before continuing.

#### Step 2

Add an AI Agent with a narrow role, explicit decision criteria and a no-fabrication rule.

- Expected result: the interface or command reports a successful, reviewable state.
- Evidence: capture the relevant screen, execution record, file or diff without exposing secrets.
- If different: stop, confirm the current product interface and resolve permissions before continuing.

| Checkpoint: Explain what changed, what evidence proves it, and whether any external state was affected. |
|---|

STEP-BY-STEP

Lab 2 - Guided Procedure 2 of 3

#### Step 3

Attach a chat model and require JSON fields: category, urgency, confidence, rationale and next_action.

- Expected result: the interface or command reports a successful, reviewable state.
- Evidence: capture the relevant screen, execution record, file or diff without exposing secrets.
- If different: stop, confirm the current product interface and resolve permissions before continuing.

#### Step 4

Validate the result with a Structured Output Parser, then route with a Switch node.

- Expected result: the interface or command reports a successful, reviewable state.
- Evidence: capture the relevant screen, execution record, file or diff without exposing secrets.
- If different: stop, confirm the current product interface and resolve permissions before continuing.

| Checkpoint: Explain what changed, what evidence proves it, and whether any external state was affected. |
|---|

STEP-BY-STEP

Lab 2 - Guided Procedure 3 of 3

#### Step 5

Write every decision to a Data Table; send high-value or low-confidence cases to human approval.

- Expected result: the interface or command reports a successful, reviewable state.
- Evidence: capture the relevant screen, execution record, file or diff without exposing secrets.
- If different: stop, confirm the current product interface and resolve permissions before continuing.

#### Step 6

Test routine, high-value, ambiguous and malicious-prompt leads; inspect execution history.

- Expected result: the interface or command reports a successful, reviewable state.
- Evidence: capture the relevant screen, execution record, file or diff without exposing secrets.
- If different: stop, confirm the current product interface and resolve permissions before continuing.

| Checkpoint: Explain what changed, what evidence proves it, and whether any external state was affected. |
|---|

COPY-PASTE BRIEF

Lab 2 - Instructions, Prompt and Source Boundary

| Copy-paste prompt: You are a lead-triage agent. Use only the submitted form fields. Classify category, urgency and confidence. Never invent customer facts. Return valid JSON with category, urgency, confidence from 0 to 1, rationale and next_action. If confidence is below 0.75, the request is high value, or an external message would be sent, set next_action to HUMAN_REVIEW. |
|---|

Review the brief before use. Replace only the scenario-specific details; preserve the source boundary, prohibited actions, output contract and escalation rule.

| Instruction component | Why it matters |
|---|---|
| Outcome and audience | Prevents a fluent but unusable deliverable |
| Approved source boundary | Reduces unsupported claims and privacy exposure |
| Required output structure | Makes results reviewable and machine-checkable |
| Prohibited actions | Blocks unsafe interpretation of a broad goal |
| Approval and stop conditions | Keeps accountability with the named person |

| Notes 1: |
|---|
| Notes 2: |

VERIFY BEFORE ACCEPTING

Lab 2 - Test Plan and Failure Cases

| Test case | Expected controlled behaviour |
|---|---|
| Normal | Routine brochure enquiry |
| Edge | Ambiguous request with missing budget |
| Malicious | Prompt asks the agent to ignore rules |
| Tool failure | Data Table write fails after classification |

- Record actual result, evidence and pass/fail status for every test.
- A failure is useful evidence; do not hide it by changing the expected result after the run.
- Do not retry a consequential action unless the system proves the first attempt had no effect.
- Escalate when the result is uncertain or the acceptance criterion cannot be observed.

| Acceptance criterion: All four test leads finish in the expected branch, every decision is logged, low-confidence or consequential actions require approval, and no unapproved external message is sent. |
|---|

COMPLETE THE ACTIVITY

Lab 2 - Evidence Pack and Reflection

- Business brief and baseline problem statement.
- Prompt or instruction version and approved source list.
- Screenshots or execution records showing the workflow and controls.
- Test results for normal, edge, malicious and tool-failure cases.
- Human review decision, outstanding risks and next recommended gate.
Reference tool view for Lab 2

| Reflection: Which part was generation, which part was agentic behaviour, and which part belonged to the harness? What would need to change before production use? |
|---|

| Notes 1: |
|---|
| Notes 2: |

RETRIEVAL PRACTICE

Topic 2 - Knowledge Check

1. Explain the central business decision in generative ai, agentic ai and ai agent technologies.

Response: ______________________________________________________________________

________________________________________________________________________________

2. Distinguish the AI capability from the workflow and the deployed agent system.

Response: ______________________________________________________________________

________________________________________________________________________________

3. Name two forms of evidence that would support a pilot decision.

Response: ______________________________________________________________________

________________________________________________________________________________

4. Identify one consequential action and the human approval it requires.

Response: ______________________________________________________________________

________________________________________________________________________________

5. Describe one failure case and the control that should contain it.

Response: ______________________________________________________________________

________________________________________________________________________________

6. State one metric that measures business value and one that measures operational safety.

Response: ______________________________________________________________________

________________________________________________________________________________

SCENARIO QUESTIONS

Topic 2 - Applied Review

| Scenario: A sales team needs structured intake, classification, CRM updates and manager approval for high-value leads. |
|---|

- What outcome should be measured before any technology is selected?
- Which AI approach is proportionate to the task and why?
- What context and evidence are necessary? What information should be excluded?
- Which tool actions are reversible, and which require explicit approval?
- What should the agent do after an ambiguous result or failed tool call?
- Which gate should the initiative pass next, and what evidence is still missing?

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |
| Notes 4: |
| Notes 5: |

TRANSFER TO PRACTICE

Topic 2 - Workplace Action Plan

| Action: Choose one non-confidential workflow and identify a small, measurable next step that applies this topic without granting unnecessary authority. |
|---|

| Planning field | Your decision |
|---|---|
| Workflow and owner |  |
| Current baseline |  |
| Proposed AI contribution |  |
| Source and tool boundary |  |
| Human approval |  |
| Test and success measure |  |
| Next review date |  |

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |

## Topic 3 - Context, Harness and Loop Engineering for AI Agents

| Topic purpose: This topic develops the ability to context · memory · instructions · tools · permissions · tests · oversight · iteration and apply the ideas to a governed business innovation decision. |
|---|

- Context engineering: Select the right instructions, knowledge, memory and current state for each step.
- Memory design: Separate working memory, durable preferences, business records and audit history.
- Harness engineering: Shape the environment: permissions, tools, workflow, tests, logs and approvals.
- Agentic loop: Plan → act → observe → evaluate → improve or stop.
- Controls: Least privilege, allowlists, budgets, timeouts, idempotency, checkpoints and kill switches.
- Human oversight: Humans set intent, approve consequential actions and resolve ambiguous outcomes.
Evidence of learning includes a completed comparison or decision worksheet, a case recommendation, the lab evidence pack and the two knowledge checks.

| Guiding question: What business decision becomes clearer after learning this topic, and what evidence would support that decision? |
|---|

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |

### 3.1 Context engineering

| Core idea: Select the right instructions, knowledge, memory and current state for each step. |
|---|

Context engineering is useful only when it changes how a team frames a business decision. In this topic, the concept connects directly to context · memory · instructions · tools · permissions · tests · oversight · iteration. It gives managers a vocabulary for separating a promising demonstration from a reliable operating capability. The practical test is whether the concept helps the team describe the goal, evidence, boundary and accountable owner more precisely.

The organisation should translate the idea into process decisions: what information is needed, who supplies it, what the AI may produce or change, which outcome is measured, and where a person must approve or resolve ambiguity. This prevents technology features from becoming disconnected experiments.

- Ask what evidence would demonstrate that 'Context engineering' improves a real outcome.
- Identify the business record, system or stakeholder affected by the decision.
- Separate a reversible draft from a consequential external action.
- Name the owner who can pause, change or retire the workflow.

| Manager takeaway: Treat the concept as a design decision with evidence and ownership, not as a label. |
|---|

APPLICATION WORKSHEET

3.1 Apply Context engineering

Apply context engineering to a workflow you know. Start with the current process before describing any AI solution. Record the trigger, inputs, decisions, systems, hand-offs, exceptions, outputs and measures. Then use the concept to propose one controlled change.

| Current workflow | AI-enabled redesign |
|---|---|
| Trigger and customer need | How intent will enter the workflow |
| Information and evidence | What context the system may use |
| Human decisions and hand-offs | What the AI prepares, recommends or executes |
| Systems and records | Tools and permissions required |
| Exceptions and failures | Escalation, retry and stop behaviour |
| Outcome and baseline | Target metric and acceptance threshold |

Application questions:

- Where does context engineering create value, and where could it create new risk?
- What must be true about data, process stability and user behaviour?
- What evidence would cause the team to continue, revise or stop?
- How will the human owner understand and challenge the system's output?

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |

CONCEPT EXPLANATION

3.2 Memory design

| Core idea: Separate working memory, durable preferences, business records and audit history. |
|---|

Memory design is useful only when it changes how a team frames a business decision. In this topic, the concept connects directly to context · memory · instructions · tools · permissions · tests · oversight · iteration. It gives managers a vocabulary for separating a promising demonstration from a reliable operating capability. The practical test is whether the concept helps the team describe the goal, evidence, boundary and accountable owner more precisely.

The organisation should translate the idea into process decisions: what information is needed, who supplies it, what the AI may produce or change, which outcome is measured, and where a person must approve or resolve ambiguity. This prevents technology features from becoming disconnected experiments.

- Ask what evidence would demonstrate that 'Memory design' improves a real outcome.
- Identify the business record, system or stakeholder affected by the decision.
- Separate a reversible draft from a consequential external action.
- Name the owner who can pause, change or retire the workflow.

| Manager takeaway: Treat the concept as a design decision with evidence and ownership, not as a label. |
|---|

APPLICATION WORKSHEET

3.2 Apply Memory design

Apply memory design to a workflow you know. Start with the current process before describing any AI solution. Record the trigger, inputs, decisions, systems, hand-offs, exceptions, outputs and measures. Then use the concept to propose one controlled change.

| Current workflow | AI-enabled redesign |
|---|---|
| Trigger and customer need | How intent will enter the workflow |
| Information and evidence | What context the system may use |
| Human decisions and hand-offs | What the AI prepares, recommends or executes |
| Systems and records | Tools and permissions required |
| Exceptions and failures | Escalation, retry and stop behaviour |
| Outcome and baseline | Target metric and acceptance threshold |

Application questions:

- Where does memory design create value, and where could it create new risk?
- What must be true about data, process stability and user behaviour?
- What evidence would cause the team to continue, revise or stop?
- How will the human owner understand and challenge the system's output?

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |

CONCEPT EXPLANATION

3.3 Harness engineering

| Core idea: Shape the environment: permissions, tools, workflow, tests, logs and approvals. |
|---|

Harness engineering is useful only when it changes how a team frames a business decision. In this topic, the concept connects directly to context · memory · instructions · tools · permissions · tests · oversight · iteration. It gives managers a vocabulary for separating a promising demonstration from a reliable operating capability. The practical test is whether the concept helps the team describe the goal, evidence, boundary and accountable owner more precisely.

The organisation should translate the idea into process decisions: what information is needed, who supplies it, what the AI may produce or change, which outcome is measured, and where a person must approve or resolve ambiguity. This prevents technology features from becoming disconnected experiments.

- Ask what evidence would demonstrate that 'Harness engineering' improves a real outcome.
- Identify the business record, system or stakeholder affected by the decision.
- Separate a reversible draft from a consequential external action.
- Name the owner who can pause, change or retire the workflow.

| Manager takeaway: Treat the concept as a design decision with evidence and ownership, not as a label. |
|---|

APPLICATION WORKSHEET

3.3 Apply Harness engineering

Apply harness engineering to a workflow you know. Start with the current process before describing any AI solution. Record the trigger, inputs, decisions, systems, hand-offs, exceptions, outputs and measures. Then use the concept to propose one controlled change.

| Current workflow | AI-enabled redesign |
|---|---|
| Trigger and customer need | How intent will enter the workflow |
| Information and evidence | What context the system may use |
| Human decisions and hand-offs | What the AI prepares, recommends or executes |
| Systems and records | Tools and permissions required |
| Exceptions and failures | Escalation, retry and stop behaviour |
| Outcome and baseline | Target metric and acceptance threshold |

Application questions:

- Where does harness engineering create value, and where could it create new risk?
- What must be true about data, process stability and user behaviour?
- What evidence would cause the team to continue, revise or stop?
- How will the human owner understand and challenge the system's output?

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |

CONCEPT EXPLANATION

3.4 Agentic loop

| Core idea: Plan → act → observe → evaluate → improve or stop. |
|---|

Agentic loop is useful only when it changes how a team frames a business decision. In this topic, the concept connects directly to context · memory · instructions · tools · permissions · tests · oversight · iteration. It gives managers a vocabulary for separating a promising demonstration from a reliable operating capability. The practical test is whether the concept helps the team describe the goal, evidence, boundary and accountable owner more precisely.

The organisation should translate the idea into process decisions: what information is needed, who supplies it, what the AI may produce or change, which outcome is measured, and where a person must approve or resolve ambiguity. This prevents technology features from becoming disconnected experiments.

- Ask what evidence would demonstrate that 'Agentic loop' improves a real outcome.
- Identify the business record, system or stakeholder affected by the decision.
- Separate a reversible draft from a consequential external action.
- Name the owner who can pause, change or retire the workflow.

| Manager takeaway: Treat the concept as a design decision with evidence and ownership, not as a label. |
|---|

APPLICATION WORKSHEET

3.4 Apply Agentic loop

Apply agentic loop to a workflow you know. Start with the current process before describing any AI solution. Record the trigger, inputs, decisions, systems, hand-offs, exceptions, outputs and measures. Then use the concept to propose one controlled change.

| Current workflow | AI-enabled redesign |
|---|---|
| Trigger and customer need | How intent will enter the workflow |
| Information and evidence | What context the system may use |
| Human decisions and hand-offs | What the AI prepares, recommends or executes |
| Systems and records | Tools and permissions required |
| Exceptions and failures | Escalation, retry and stop behaviour |
| Outcome and baseline | Target metric and acceptance threshold |

Application questions:

- Where does agentic loop create value, and where could it create new risk?
- What must be true about data, process stability and user behaviour?
- What evidence would cause the team to continue, revise or stop?
- How will the human owner understand and challenge the system's output?

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |

CONCEPT EXPLANATION

3.5 Controls

| Core idea: Least privilege, allowlists, budgets, timeouts, idempotency, checkpoints and kill switches. |
|---|

Controls is useful only when it changes how a team frames a business decision. In this topic, the concept connects directly to context · memory · instructions · tools · permissions · tests · oversight · iteration. It gives managers a vocabulary for separating a promising demonstration from a reliable operating capability. The practical test is whether the concept helps the team describe the goal, evidence, boundary and accountable owner more precisely.

The organisation should translate the idea into process decisions: what information is needed, who supplies it, what the AI may produce or change, which outcome is measured, and where a person must approve or resolve ambiguity. This prevents technology features from becoming disconnected experiments.

- Ask what evidence would demonstrate that 'Controls' improves a real outcome.
- Identify the business record, system or stakeholder affected by the decision.
- Separate a reversible draft from a consequential external action.
- Name the owner who can pause, change or retire the workflow.

| Manager takeaway: Treat the concept as a design decision with evidence and ownership, not as a label. |
|---|

APPLICATION WORKSHEET

3.5 Apply Controls

Apply controls to a workflow you know. Start with the current process before describing any AI solution. Record the trigger, inputs, decisions, systems, hand-offs, exceptions, outputs and measures. Then use the concept to propose one controlled change.

| Current workflow | AI-enabled redesign |
|---|---|
| Trigger and customer need | How intent will enter the workflow |
| Information and evidence | What context the system may use |
| Human decisions and hand-offs | What the AI prepares, recommends or executes |
| Systems and records | Tools and permissions required |
| Exceptions and failures | Escalation, retry and stop behaviour |
| Outcome and baseline | Target metric and acceptance threshold |

Application questions:

- Where does controls create value, and where could it create new risk?
- What must be true about data, process stability and user behaviour?
- What evidence would cause the team to continue, revise or stop?
- How will the human owner understand and challenge the system's output?

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |

CONCEPT EXPLANATION

3.6 Human oversight

| Core idea: Humans set intent, approve consequential actions and resolve ambiguous outcomes. |
|---|

Human oversight is useful only when it changes how a team frames a business decision. In this topic, the concept connects directly to context · memory · instructions · tools · permissions · tests · oversight · iteration. It gives managers a vocabulary for separating a promising demonstration from a reliable operating capability. The practical test is whether the concept helps the team describe the goal, evidence, boundary and accountable owner more precisely.

The organisation should translate the idea into process decisions: what information is needed, who supplies it, what the AI may produce or change, which outcome is measured, and where a person must approve or resolve ambiguity. This prevents technology features from becoming disconnected experiments.

- Ask what evidence would demonstrate that 'Human oversight' improves a real outcome.
- Identify the business record, system or stakeholder affected by the decision.
- Separate a reversible draft from a consequential external action.
- Name the owner who can pause, change or retire the workflow.

| Manager takeaway: Treat the concept as a design decision with evidence and ownership, not as a label. |
|---|

APPLICATION WORKSHEET

3.6 Apply Human oversight

Apply human oversight to a workflow you know. Start with the current process before describing any AI solution. Record the trigger, inputs, decisions, systems, hand-offs, exceptions, outputs and measures. Then use the concept to propose one controlled change.

| Current workflow | AI-enabled redesign |
|---|---|
| Trigger and customer need | How intent will enter the workflow |
| Information and evidence | What context the system may use |
| Human decisions and hand-offs | What the AI prepares, recommends or executes |
| Systems and records | Tools and permissions required |
| Exceptions and failures | Escalation, retry and stop behaviour |
| Outcome and baseline | Target metric and acceptance threshold |

Application questions:

- Where does human oversight create value, and where could it create new risk?
- What must be true about data, process stability and user behaviour?
- What evidence would cause the team to continue, revise or stop?
- How will the human owner understand and challenge the system's output?

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |

### 3.F1 Context stack

| Framework definition: Layer system instructions, task goal, constraints, source knowledge, current state, memory, examples and tool results. |
|---|

When to use it: Use the stack to keep the working set relevant and to separate durable rules from temporary information.

Watch for: More context is not always better; irrelevant or conflicting material can reduce reliability.

A useful framework reduces ambiguity. It should allow two people to examine the same opportunity, state their assumptions and reach a traceable decision. Apply it with representative examples rather than idealised demonstrations.

- Define the unit of analysis: task, workflow, customer journey or operating model.
- Record assumptions separately from verified evidence.
- Use a simple rating scale with written justification.
- Review disagreements; they often reveal missing data or different risk tolerances.
- Assign a next action and owner before closing the discussion.

| Diagnostic question | Evidence to collect |
|---|---|
| What problem does this framework clarify? | Baseline process map, delay, error or cost data |
| What decision follows? | Pilot, preparation, redesign, defer or stop |
| Who owns the decision? | Named business and technology owners |
| When is it reviewed? | Gate date, metric threshold and review cadence |

BUSINESS FRAMEWORK

3.F2 Memory lifecycle

| Framework definition: Define capture, validation, storage, retrieval, update, expiry and deletion for every memory type. |
|---|

When to use it: Use the lifecycle to distinguish working notes, approved preferences, business records and audit history.

Watch for: Do not store secrets, uncertain claims or personal data merely because an agent can remember them.

A useful framework reduces ambiguity. It should allow two people to examine the same opportunity, state their assumptions and reach a traceable decision. Apply it with representative examples rather than idealised demonstrations.

- Define the unit of analysis: task, workflow, customer journey or operating model.
- Record assumptions separately from verified evidence.
- Use a simple rating scale with written justification.
- Review disagreements; they often reveal missing data or different risk tolerances.
- Assign a next action and owner before closing the discussion.

| Diagnostic question | Evidence to collect |
|---|---|
| What problem does this framework clarify? | Baseline process map, delay, error or cost data |
| What decision follows? | Pilot, preparation, redesign, defer or stop |
| Who owns the decision? | Named business and technology owners |
| When is it reviewed? | Gate date, metric threshold and review cadence |

BUSINESS FRAMEWORK

3.F3 Harness control plane

| Framework definition: Combine permissions, tool schemas, workflow state, sandboxes, tests, evaluators, logs, approvals and recovery paths. |
|---|

When to use it: Use the control plane to make the safe action the easiest action for the agent.

Watch for: A policy written only in prose is weak if the environment still permits the prohibited action.

A useful framework reduces ambiguity. It should allow two people to examine the same opportunity, state their assumptions and reach a traceable decision. Apply it with representative examples rather than idealised demonstrations.

- Define the unit of analysis: task, workflow, customer journey or operating model.
- Record assumptions separately from verified evidence.
- Use a simple rating scale with written justification.
- Review disagreements; they often reveal missing data or different risk tolerances.
- Assign a next action and owner before closing the discussion.

| Diagnostic question | Evidence to collect |
|---|---|
| What problem does this framework clarify? | Baseline process map, delay, error or cost data |
| What decision follows? | Pilot, preparation, redesign, defer or stop |
| Who owns the decision? | Named business and technology owners |
| When is it reviewed? | Gate date, metric threshold and review cadence |

BUSINESS FRAMEWORK

3.F4 Loop state machine

| Framework definition: Represent planning, action, observation, evaluation, retry, escalation, completion and stop as explicit states. |
|---|

When to use it: Use state transitions to make retries, budgets and ownership observable.

Watch for: Unbounded retries create duplicate actions, cost and noise; every loop needs a stop condition.

A useful framework reduces ambiguity. It should allow two people to examine the same opportunity, state their assumptions and reach a traceable decision. Apply it with representative examples rather than idealised demonstrations.

- Define the unit of analysis: task, workflow, customer journey or operating model.
- Record assumptions separately from verified evidence.
- Use a simple rating scale with written justification.
- Review disagreements; they often reveal missing data or different risk tolerances.
- Assign a next action and owner before closing the discussion.

| Diagnostic question | Evidence to collect |
|---|---|
| What problem does this framework clarify? | Baseline process map, delay, error or cost data |
| What decision follows? | Pilot, preparation, redesign, defer or stop |
| Who owns the decision? | Named business and technology owners |
| When is it reviewed? | Gate date, metric threshold and review cadence |

### Case 3.1 - Conflicting policy sources

| Scenario: A knowledge-work agent receives two leave policies with different effective dates and produces a confident answer. |
|---|

Your assignment: Redesign context selection, source priority, evaluation and escalation so the conflict is visible.

- State the business outcome in one sentence without naming a technology.
- Identify the current bottleneck and quantify it with a baseline or a measurement plan.
- Choose the appropriate AI approach and justify the boundary of action.
- Specify context, tools, memory and human oversight only if the workflow requires them.
- List one normal case, one edge case, one malicious case and one tool-failure case.
- Recommend pilot, prepare, redesign, defer or stop, with evidence required for the next decision.

| Decision area | Your analysis |
|---|---|
| Value and stakeholder impact |  |
| Feasibility and dependencies |  |
| Risks and prohibited actions |  |
| Controls and human owner |  |
| Measures and gate decision |  |

| Discussion prompt: How would the recommendation change if the workflow moved from internal use to a customer-facing channel? Relate your answer to Topic 3. |
|---|

WORKED BUSINESS CASE

Case 3.2 - Duplicate customer update

| Scenario: A tool call times out after sending an email, so the agent retries and sends the message twice. |
|---|

Your assignment: Specify idempotency, observation and retry controls that prevent the duplicate effect.

- State the business outcome in one sentence without naming a technology.
- Identify the current bottleneck and quantify it with a baseline or a measurement plan.
- Choose the appropriate AI approach and justify the boundary of action.
- Specify context, tools, memory and human oversight only if the workflow requires them.
- List one normal case, one edge case, one malicious case and one tool-failure case.
- Recommend pilot, prepare, redesign, defer or stop, with evidence required for the next decision.

| Decision area | Your analysis |
|---|---|
| Value and stakeholder impact |  |
| Feasibility and dependencies |  |
| Risks and prohibited actions |  |
| Controls and human owner |  |
| Measures and gate decision |  |

| Discussion prompt: How would the recommendation change if the workflow moved from internal use to a customer-facing channel? Relate your answer to Topic 3. |
|---|

WORKED BUSINESS CASE

Case 3.3 - Memory without governance

| Scenario: An agent saves every conversation as durable memory, including tentative claims and personal information. |
|---|

Your assignment: Design memory categories, validation, retention and deletion rules.

- State the business outcome in one sentence without naming a technology.
- Identify the current bottleneck and quantify it with a baseline or a measurement plan.
- Choose the appropriate AI approach and justify the boundary of action.
- Specify context, tools, memory and human oversight only if the workflow requires them.
- List one normal case, one edge case, one malicious case and one tool-failure case.
- Recommend pilot, prepare, redesign, defer or stop, with evidence required for the next decision.

| Decision area | Your analysis |
|---|---|
| Value and stakeholder impact |  |
| Feasibility and dependencies |  |
| Risks and prohibited actions |  |
| Controls and human owner |  |
| Measures and gate decision |  |

| Discussion prompt: How would the recommendation change if the workflow moved from internal use to a customer-facing channel? Relate your answer to Topic 3. |
|---|

### Lab 3 - Delegate Knowledge Work with Claude Cowork and ChatGPT Work

| Goal: Give the same business brief to Claude Cowork and ChatGPT Work, request a decision memo and action register, then compare how each system handles files, context, tool use, progress and approvals. |
|---|

Alignment: LO3-LO4 · Topic 3

Deliverable: Two evidence-grounded deliverables plus a context-and-harness comparison scorecard

Tools: Claude Cowork, ChatGPT Work, local files, connected apps where authorised

| Configuration / constraint | Required evidence |
|---|---|
| Create sources/ and output/ folders and use only the three instructor-supplied source notes. | Record the configured value or resulting evidence. |
| Deliver a two-page decision memo and an action register with owner, date, dependency and evidence. | Record the configured value or resulting evidence. |
| Score grounding, completeness, traceability, safe tool use and editability from 1-5. | Record the configured value or resulting evidence. |

- Use only non-confidential training data and approved accounts.
- Record the source, model or service, date, prompt or instruction, tool actions and human approval.
- Stop if access, permissions, pricing or the active interface differs materially from the guide.
- Do not connect production credentials or send external communications during the lab.

| Acceptance standard: Both deliverables trace claims to supplied sources, no unapproved external action occurs, the scorecard distinguishes context from harness quality, and the rerun improves a recorded acceptance measure. |
|---|

LAB DESIGN

Lab 3 - Workflow and Control Design

| Stage | Lab decision |
|---|---|
| Intent | State the business outcome and exclusions |
| Context | Supply only relevant, approved information |
| Action | Generate, reason or call a scoped tool |
| Observation | Capture output, status and evidence |
| Evaluation | Compare with acceptance criteria |
| Decision | Complete, improve, stop or escalate |

Control boundary:

| Control boundary: The systems may read approved project files and write to an output folder; no external action is allowed. |
|---|

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |

STEP-BY-STEP

Lab 3 - Guided Procedure 1 of 3

#### Step 1

Create a clean project folder containing the scenario, three source notes and an output folder.

- Expected result: the interface or command reports a successful, reviewable state.
- Evidence: capture the relevant screen, execution record, file or diff without exposing secrets.
- If different: stop, confirm the current product interface and resolve permissions before continuing.

#### Step 2

Write an outcome brief with audience, scope, source boundary, format, deadline and approval rules.

- Expected result: the interface or command reports a successful, reviewable state.
- Evidence: capture the relevant screen, execution record, file or diff without exposing secrets.
- If different: stop, confirm the current product interface and resolve permissions before continuing.

| Checkpoint: Explain what changed, what evidence proves it, and whether any external state was affected. |
|---|

STEP-BY-STEP

Lab 3 - Guided Procedure 2 of 3

#### Step 3

Run the brief in Claude Cowork; review its plan and approve only the file access it needs.

- Expected result: the interface or command reports a successful, reviewable state.
- Evidence: capture the relevant screen, execution record, file or diff without exposing secrets.
- If different: stop, confirm the current product interface and resolve permissions before continuing.

#### Step 4

Run the same brief in ChatGPT Work; review progress, sources, tool requests and draft outputs.

- Expected result: the interface or command reports a successful, reviewable state.
- Evidence: capture the relevant screen, execution record, file or diff without exposing secrets.
- If different: stop, confirm the current product interface and resolve permissions before continuing.

| Checkpoint: Explain what changed, what evidence proves it, and whether any external state was affected. |
|---|

STEP-BY-STEP

Lab 3 - Guided Procedure 3 of 3

#### Step 5

Evaluate both results for grounding, completeness, traceability, safe tool use and editability.

- Expected result: the interface or command reports a successful, reviewable state.
- Evidence: capture the relevant screen, execution record, file or diff without exposing secrets.
- If different: stop, confirm the current product interface and resolve permissions before continuing.

#### Step 6

Revise the context or harness, rerun the weakest case and document the improvement.

- Expected result: the interface or command reports a successful, reviewable state.
- Evidence: capture the relevant screen, execution record, file or diff without exposing secrets.
- If different: stop, confirm the current product interface and resolve permissions before continuing.

| Checkpoint: Explain what changed, what evidence proves it, and whether any external state was affected. |
|---|

COPY-PASTE BRIEF

Lab 3 - Instructions, Prompt and Source Boundary

| Copy-paste prompt: Using only the files in this project folder, prepare a two-page decision memo and an action register. Cite the source filename beside every material claim. Do not browse, email, publish, delete or modify source files. Show your plan first. Ask before reading outside the project folder or writing anywhere except the output folder. Stop and flag conflicting or missing evidence. |
|---|

Review the brief before use. Replace only the scenario-specific details; preserve the source boundary, prohibited actions, output contract and escalation rule.

| Instruction component | Why it matters |
|---|---|
| Outcome and audience | Prevents a fluent but unusable deliverable |
| Approved source boundary | Reduces unsupported claims and privacy exposure |
| Required output structure | Makes results reviewable and machine-checkable |
| Prohibited actions | Blocks unsafe interpretation of a broad goal |
| Approval and stop conditions | Keeps accountability with the named person |

| Notes 1: |
|---|
| Notes 2: |

VERIFY BEFORE ACCEPTING

Lab 3 - Test Plan and Failure Cases

| Test case | Expected controlled behaviour |
|---|---|
| Normal | Sources are complete and consistent |
| Edge | One required source is missing |
| Conflict | Two notes disagree on a material fact |
| Permission | System requests access outside project folder |

- Record actual result, evidence and pass/fail status for every test.
- A failure is useful evidence; do not hide it by changing the expected result after the run.
- Do not retry a consequential action unless the system proves the first attempt had no effect.
- Escalate when the result is uncertain or the acceptance criterion cannot be observed.

| Acceptance criterion: Both deliverables trace claims to supplied sources, no unapproved external action occurs, the scorecard distinguishes context from harness quality, and the rerun improves a recorded acceptance measure. |
|---|

COMPLETE THE ACTIVITY

Lab 3 - Evidence Pack and Reflection

- Business brief and baseline problem statement.
- Prompt or instruction version and approved source list.
- Screenshots or execution records showing the workflow and controls.
- Test results for normal, edge, malicious and tool-failure cases.
- Human review decision, outstanding risks and next recommended gate.
Reference tool view for Lab 3

| Reflection: Which part was generation, which part was agentic behaviour, and which part belonged to the harness? What would need to change before production use? |
|---|

| Notes 1: |
|---|
| Notes 2: |

RETRIEVAL PRACTICE

Topic 3 - Knowledge Check

1. Explain the central business decision in context, harness and loop engineering for ai agents.

Response: ______________________________________________________________________

________________________________________________________________________________

2. Distinguish the AI capability from the workflow and the deployed agent system.

Response: ______________________________________________________________________

________________________________________________________________________________

3. Name two forms of evidence that would support a pilot decision.

Response: ______________________________________________________________________

________________________________________________________________________________

4. Identify one consequential action and the human approval it requires.

Response: ______________________________________________________________________

________________________________________________________________________________

5. Describe one failure case and the control that should contain it.

Response: ______________________________________________________________________

________________________________________________________________________________

6. State one metric that measures business value and one that measures operational safety.

Response: ______________________________________________________________________

________________________________________________________________________________

SCENARIO QUESTIONS

Topic 3 - Applied Review

| Scenario: A knowledge-work agent receives two leave policies with different effective dates and produces a confident answer. |
|---|

- What outcome should be measured before any technology is selected?
- Which AI approach is proportionate to the task and why?
- What context and evidence are necessary? What information should be excluded?
- Which tool actions are reversible, and which require explicit approval?
- What should the agent do after an ambiguous result or failed tool call?
- Which gate should the initiative pass next, and what evidence is still missing?

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |
| Notes 4: |
| Notes 5: |

TRANSFER TO PRACTICE

Topic 3 - Workplace Action Plan

| Action: Choose one non-confidential workflow and identify a small, measurable next step that applies this topic without granting unnecessary authority. |
|---|

| Planning field | Your decision |
|---|---|
| Workflow and owner |  |
| Current baseline |  |
| Proposed AI contribution |  |
| Source and tool boundary |  |
| Human approval |  |
| Test and success measure |  |
| Next review date |  |

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |

## Topic 4 - Business Opportunities and Innovative Agentic AI Use Cases

| Topic purpose: This topic develops the ability to digital workers · natural-language interfaces · cross-system workflows · functional value and apply the ideas to a governed business innovation decision. |
|---|

- Administration: Prepare documents, reconcile records, schedule follow-ups and route approvals.
- Marketing: Research markets, create campaigns, generate video and learn from performance.
- Sales: Enrich leads, draft outreach, update CRM and surface next-best actions.
- Customer service: Retrieve knowledge, resolve routine cases and escalate exceptions with context.
- Operations: Monitor events, coordinate systems, investigate anomalies and trigger playbooks.
- Natural-language operations: People state intent; agents translate it into controlled software actions.
Evidence of learning includes a completed comparison or decision worksheet, a case recommendation, the lab evidence pack and the two knowledge checks.

| Guiding question: What business decision becomes clearer after learning this topic, and what evidence would support that decision? |
|---|

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |

### 4.1 Administration

| Core idea: Prepare documents, reconcile records, schedule follow-ups and route approvals. |
|---|

Administration is useful only when it changes how a team frames a business decision. In this topic, the concept connects directly to digital workers · natural-language interfaces · cross-system workflows · functional value. It gives managers a vocabulary for separating a promising demonstration from a reliable operating capability. The practical test is whether the concept helps the team describe the goal, evidence, boundary and accountable owner more precisely.

The organisation should translate the idea into process decisions: what information is needed, who supplies it, what the AI may produce or change, which outcome is measured, and where a person must approve or resolve ambiguity. This prevents technology features from becoming disconnected experiments.

- Ask what evidence would demonstrate that 'Administration' improves a real outcome.
- Identify the business record, system or stakeholder affected by the decision.
- Separate a reversible draft from a consequential external action.
- Name the owner who can pause, change or retire the workflow.

| Manager takeaway: Treat the concept as a design decision with evidence and ownership, not as a label. |
|---|

APPLICATION WORKSHEET

4.1 Apply Administration

Apply administration to a workflow you know. Start with the current process before describing any AI solution. Record the trigger, inputs, decisions, systems, hand-offs, exceptions, outputs and measures. Then use the concept to propose one controlled change.

| Current workflow | AI-enabled redesign |
|---|---|
| Trigger and customer need | How intent will enter the workflow |
| Information and evidence | What context the system may use |
| Human decisions and hand-offs | What the AI prepares, recommends or executes |
| Systems and records | Tools and permissions required |
| Exceptions and failures | Escalation, retry and stop behaviour |
| Outcome and baseline | Target metric and acceptance threshold |

Application questions:

- Where does administration create value, and where could it create new risk?
- What must be true about data, process stability and user behaviour?
- What evidence would cause the team to continue, revise or stop?
- How will the human owner understand and challenge the system's output?

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |

CONCEPT EXPLANATION

4.2 Marketing

| Core idea: Research markets, create campaigns, generate video and learn from performance. |
|---|

Marketing is useful only when it changes how a team frames a business decision. In this topic, the concept connects directly to digital workers · natural-language interfaces · cross-system workflows · functional value. It gives managers a vocabulary for separating a promising demonstration from a reliable operating capability. The practical test is whether the concept helps the team describe the goal, evidence, boundary and accountable owner more precisely.

The organisation should translate the idea into process decisions: what information is needed, who supplies it, what the AI may produce or change, which outcome is measured, and where a person must approve or resolve ambiguity. This prevents technology features from becoming disconnected experiments.

- Ask what evidence would demonstrate that 'Marketing' improves a real outcome.
- Identify the business record, system or stakeholder affected by the decision.
- Separate a reversible draft from a consequential external action.
- Name the owner who can pause, change or retire the workflow.

| Manager takeaway: Treat the concept as a design decision with evidence and ownership, not as a label. |
|---|

APPLICATION WORKSHEET

4.2 Apply Marketing

Apply marketing to a workflow you know. Start with the current process before describing any AI solution. Record the trigger, inputs, decisions, systems, hand-offs, exceptions, outputs and measures. Then use the concept to propose one controlled change.

| Current workflow | AI-enabled redesign |
|---|---|
| Trigger and customer need | How intent will enter the workflow |
| Information and evidence | What context the system may use |
| Human decisions and hand-offs | What the AI prepares, recommends or executes |
| Systems and records | Tools and permissions required |
| Exceptions and failures | Escalation, retry and stop behaviour |
| Outcome and baseline | Target metric and acceptance threshold |

Application questions:

- Where does marketing create value, and where could it create new risk?
- What must be true about data, process stability and user behaviour?
- What evidence would cause the team to continue, revise or stop?
- How will the human owner understand and challenge the system's output?

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |

CONCEPT EXPLANATION

4.3 Sales

| Core idea: Enrich leads, draft outreach, update CRM and surface next-best actions. |
|---|

Sales is useful only when it changes how a team frames a business decision. In this topic, the concept connects directly to digital workers · natural-language interfaces · cross-system workflows · functional value. It gives managers a vocabulary for separating a promising demonstration from a reliable operating capability. The practical test is whether the concept helps the team describe the goal, evidence, boundary and accountable owner more precisely.

The organisation should translate the idea into process decisions: what information is needed, who supplies it, what the AI may produce or change, which outcome is measured, and where a person must approve or resolve ambiguity. This prevents technology features from becoming disconnected experiments.

- Ask what evidence would demonstrate that 'Sales' improves a real outcome.
- Identify the business record, system or stakeholder affected by the decision.
- Separate a reversible draft from a consequential external action.
- Name the owner who can pause, change or retire the workflow.

| Manager takeaway: Treat the concept as a design decision with evidence and ownership, not as a label. |
|---|

APPLICATION WORKSHEET

4.3 Apply Sales

Apply sales to a workflow you know. Start with the current process before describing any AI solution. Record the trigger, inputs, decisions, systems, hand-offs, exceptions, outputs and measures. Then use the concept to propose one controlled change.

| Current workflow | AI-enabled redesign |
|---|---|
| Trigger and customer need | How intent will enter the workflow |
| Information and evidence | What context the system may use |
| Human decisions and hand-offs | What the AI prepares, recommends or executes |
| Systems and records | Tools and permissions required |
| Exceptions and failures | Escalation, retry and stop behaviour |
| Outcome and baseline | Target metric and acceptance threshold |

Application questions:

- Where does sales create value, and where could it create new risk?
- What must be true about data, process stability and user behaviour?
- What evidence would cause the team to continue, revise or stop?
- How will the human owner understand and challenge the system's output?

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |

CONCEPT EXPLANATION

4.4 Customer service

| Core idea: Retrieve knowledge, resolve routine cases and escalate exceptions with context. |
|---|

Customer service is useful only when it changes how a team frames a business decision. In this topic, the concept connects directly to digital workers · natural-language interfaces · cross-system workflows · functional value. It gives managers a vocabulary for separating a promising demonstration from a reliable operating capability. The practical test is whether the concept helps the team describe the goal, evidence, boundary and accountable owner more precisely.

The organisation should translate the idea into process decisions: what information is needed, who supplies it, what the AI may produce or change, which outcome is measured, and where a person must approve or resolve ambiguity. This prevents technology features from becoming disconnected experiments.

- Ask what evidence would demonstrate that 'Customer service' improves a real outcome.
- Identify the business record, system or stakeholder affected by the decision.
- Separate a reversible draft from a consequential external action.
- Name the owner who can pause, change or retire the workflow.

| Manager takeaway: Treat the concept as a design decision with evidence and ownership, not as a label. |
|---|

APPLICATION WORKSHEET

4.4 Apply Customer service

Apply customer service to a workflow you know. Start with the current process before describing any AI solution. Record the trigger, inputs, decisions, systems, hand-offs, exceptions, outputs and measures. Then use the concept to propose one controlled change.

| Current workflow | AI-enabled redesign |
|---|---|
| Trigger and customer need | How intent will enter the workflow |
| Information and evidence | What context the system may use |
| Human decisions and hand-offs | What the AI prepares, recommends or executes |
| Systems and records | Tools and permissions required |
| Exceptions and failures | Escalation, retry and stop behaviour |
| Outcome and baseline | Target metric and acceptance threshold |

Application questions:

- Where does customer service create value, and where could it create new risk?
- What must be true about data, process stability and user behaviour?
- What evidence would cause the team to continue, revise or stop?
- How will the human owner understand and challenge the system's output?

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |

CONCEPT EXPLANATION

4.5 Operations

| Core idea: Monitor events, coordinate systems, investigate anomalies and trigger playbooks. |
|---|

Operations is useful only when it changes how a team frames a business decision. In this topic, the concept connects directly to digital workers · natural-language interfaces · cross-system workflows · functional value. It gives managers a vocabulary for separating a promising demonstration from a reliable operating capability. The practical test is whether the concept helps the team describe the goal, evidence, boundary and accountable owner more precisely.

The organisation should translate the idea into process decisions: what information is needed, who supplies it, what the AI may produce or change, which outcome is measured, and where a person must approve or resolve ambiguity. This prevents technology features from becoming disconnected experiments.

- Ask what evidence would demonstrate that 'Operations' improves a real outcome.
- Identify the business record, system or stakeholder affected by the decision.
- Separate a reversible draft from a consequential external action.
- Name the owner who can pause, change or retire the workflow.

| Manager takeaway: Treat the concept as a design decision with evidence and ownership, not as a label. |
|---|

APPLICATION WORKSHEET

4.5 Apply Operations

Apply operations to a workflow you know. Start with the current process before describing any AI solution. Record the trigger, inputs, decisions, systems, hand-offs, exceptions, outputs and measures. Then use the concept to propose one controlled change.

| Current workflow | AI-enabled redesign |
|---|---|
| Trigger and customer need | How intent will enter the workflow |
| Information and evidence | What context the system may use |
| Human decisions and hand-offs | What the AI prepares, recommends or executes |
| Systems and records | Tools and permissions required |
| Exceptions and failures | Escalation, retry and stop behaviour |
| Outcome and baseline | Target metric and acceptance threshold |

Application questions:

- Where does operations create value, and where could it create new risk?
- What must be true about data, process stability and user behaviour?
- What evidence would cause the team to continue, revise or stop?
- How will the human owner understand and challenge the system's output?

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |

CONCEPT EXPLANATION

4.6 Natural-language operations

| Core idea: People state intent; agents translate it into controlled software actions. |
|---|

Natural-language operations is useful only when it changes how a team frames a business decision. In this topic, the concept connects directly to digital workers · natural-language interfaces · cross-system workflows · functional value. It gives managers a vocabulary for separating a promising demonstration from a reliable operating capability. The practical test is whether the concept helps the team describe the goal, evidence, boundary and accountable owner more precisely.

The organisation should translate the idea into process decisions: what information is needed, who supplies it, what the AI may produce or change, which outcome is measured, and where a person must approve or resolve ambiguity. This prevents technology features from becoming disconnected experiments.

- Ask what evidence would demonstrate that 'Natural-language operations' improves a real outcome.
- Identify the business record, system or stakeholder affected by the decision.
- Separate a reversible draft from a consequential external action.
- Name the owner who can pause, change or retire the workflow.

| Manager takeaway: Treat the concept as a design decision with evidence and ownership, not as a label. |
|---|

APPLICATION WORKSHEET

4.6 Apply Natural-language operations

Apply natural-language operations to a workflow you know. Start with the current process before describing any AI solution. Record the trigger, inputs, decisions, systems, hand-offs, exceptions, outputs and measures. Then use the concept to propose one controlled change.

| Current workflow | AI-enabled redesign |
|---|---|
| Trigger and customer need | How intent will enter the workflow |
| Information and evidence | What context the system may use |
| Human decisions and hand-offs | What the AI prepares, recommends or executes |
| Systems and records | Tools and permissions required |
| Exceptions and failures | Escalation, retry and stop behaviour |
| Outcome and baseline | Target metric and acceptance threshold |

Application questions:

- Where does natural-language operations create value, and where could it create new risk?
- What must be true about data, process stability and user behaviour?
- What evidence would cause the team to continue, revise or stop?
- How will the human owner understand and challenge the system's output?

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |

### 4.F1 Opportunity discovery lens

| Framework definition: Look for volume, repeated hand-offs, search across sources, frequent drafting, rules with exceptions and measurable delays. |
|---|

When to use it: Use the lens during interviews and process walks to find friction that staff have normalised.

Watch for: High frequency alone is not enough; the outcome must matter and the process must be governable.

A useful framework reduces ambiguity. It should allow two people to examine the same opportunity, state their assumptions and reach a traceable decision. Apply it with representative examples rather than idealised demonstrations.

- Define the unit of analysis: task, workflow, customer journey or operating model.
- Record assumptions separately from verified evidence.
- Use a simple rating scale with written justification.
- Review disagreements; they often reveal missing data or different risk tolerances.
- Assign a next action and owner before closing the discussion.

| Diagnostic question | Evidence to collect |
|---|---|
| What problem does this framework clarify? | Baseline process map, delay, error or cost data |
| What decision follows? | Pilot, preparation, redesign, defer or stop |
| Who owns the decision? | Named business and technology owners |
| When is it reviewed? | Gate date, metric threshold and review cadence |

BUSINESS FRAMEWORK

4.F2 Digital-worker canvas

| Framework definition: Document customer, trigger, goal, inputs, decisions, tools, outputs, owner, controls, metrics and exceptions on one page. |
|---|

When to use it: Use the canvas to align business and technical teams before prototyping.

Watch for: Do not begin integration work while the owner, success measure or prohibited actions remain unclear.

A useful framework reduces ambiguity. It should allow two people to examine the same opportunity, state their assumptions and reach a traceable decision. Apply it with representative examples rather than idealised demonstrations.

- Define the unit of analysis: task, workflow, customer journey or operating model.
- Record assumptions separately from verified evidence.
- Use a simple rating scale with written justification.
- Review disagreements; they often reveal missing data or different risk tolerances.
- Assign a next action and owner before closing the discussion.

| Diagnostic question | Evidence to collect |
|---|---|
| What problem does this framework clarify? | Baseline process map, delay, error or cost data |
| What decision follows? | Pilot, preparation, redesign, defer or stop |
| Who owns the decision? | Named business and technology owners |
| When is it reviewed? | Gate date, metric threshold and review cadence |

BUSINESS FRAMEWORK

4.F3 Natural-language control model

| Framework definition: Translate human intent into a proposed plan, validated tool calls, previewed consequential actions and an auditable outcome. |
|---|

When to use it: Use this model when an agent becomes the interface to multiple applications or datasets.

Watch for: Natural language is ambiguous; confirmations and structured parameters remain necessary.

A useful framework reduces ambiguity. It should allow two people to examine the same opportunity, state their assumptions and reach a traceable decision. Apply it with representative examples rather than idealised demonstrations.

- Define the unit of analysis: task, workflow, customer journey or operating model.
- Record assumptions separately from verified evidence.
- Use a simple rating scale with written justification.
- Review disagreements; they often reveal missing data or different risk tolerances.
- Assign a next action and owner before closing the discussion.

| Diagnostic question | Evidence to collect |
|---|---|
| What problem does this framework clarify? | Baseline process map, delay, error or cost data |
| What decision follows? | Pilot, preparation, redesign, defer or stop |
| Who owns the decision? | Named business and technology owners |
| When is it reviewed? | Gate date, metric threshold and review cadence |

BUSINESS FRAMEWORK

4.F4 Functional use-case map

| Framework definition: Compare administration, marketing, sales, customer service, operations and management opportunities using shared criteria. |
|---|

When to use it: Use the map to create a balanced portfolio instead of concentrating all pilots in content generation.

Watch for: Avoid counting the same underlying workflow as several separate use cases.

A useful framework reduces ambiguity. It should allow two people to examine the same opportunity, state their assumptions and reach a traceable decision. Apply it with representative examples rather than idealised demonstrations.

- Define the unit of analysis: task, workflow, customer journey or operating model.
- Record assumptions separately from verified evidence.
- Use a simple rating scale with written justification.
- Review disagreements; they often reveal missing data or different risk tolerances.
- Assign a next action and owner before closing the discussion.

| Diagnostic question | Evidence to collect |
|---|---|
| What problem does this framework clarify? | Baseline process map, delay, error or cost data |
| What decision follows? | Pilot, preparation, redesign, defer or stop |
| Who owns the decision? | Named business and technology owners |
| When is it reviewed? | Gate date, metric threshold and review cadence |

### Case 4.1 - Administration digital worker

| Scenario: A finance team reconciles invoices, purchase orders and approvals across email, spreadsheets and an ERP. |
|---|

Your assignment: Identify the high-value agent boundary and the transactions that still require approval.

- State the business outcome in one sentence without naming a technology.
- Identify the current bottleneck and quantify it with a baseline or a measurement plan.
- Choose the appropriate AI approach and justify the boundary of action.
- Specify context, tools, memory and human oversight only if the workflow requires them.
- List one normal case, one edge case, one malicious case and one tool-failure case.
- Recommend pilot, prepare, redesign, defer or stop, with evidence required for the next decision.

| Decision area | Your analysis |
|---|---|
| Value and stakeholder impact |  |
| Feasibility and dependencies |  |
| Risks and prohibited actions |  |
| Controls and human owner |  |
| Measures and gate decision |  |

| Discussion prompt: How would the recommendation change if the workflow moved from internal use to a customer-facing channel? Relate your answer to Topic 4. |
|---|

WORKED BUSINESS CASE

Case 4.2 - Customer-service interface

| Scenario: Customers describe problems in natural language; the agent searches knowledge, checks account status and proposes resolution. |
|---|

Your assignment: Design the hand-off between retrieval, tool use, confidence, escalation and customer communication.

- State the business outcome in one sentence without naming a technology.
- Identify the current bottleneck and quantify it with a baseline or a measurement plan.
- Choose the appropriate AI approach and justify the boundary of action.
- Specify context, tools, memory and human oversight only if the workflow requires them.
- List one normal case, one edge case, one malicious case and one tool-failure case.
- Recommend pilot, prepare, redesign, defer or stop, with evidence required for the next decision.

| Decision area | Your analysis |
|---|---|
| Value and stakeholder impact |  |
| Feasibility and dependencies |  |
| Risks and prohibited actions |  |
| Controls and human owner |  |
| Measures and gate decision |  |

| Discussion prompt: How would the recommendation change if the workflow moved from internal use to a customer-facing channel? Relate your answer to Topic 4. |
|---|

WORKED BUSINESS CASE

Case 4.3 - Operations exception coordinator

| Scenario: A logistics agent monitors late events, investigates supporting data and proposes rerouting options. |
|---|

Your assignment: Define metrics, tool permissions and incident controls for a pilot.

- State the business outcome in one sentence without naming a technology.
- Identify the current bottleneck and quantify it with a baseline or a measurement plan.
- Choose the appropriate AI approach and justify the boundary of action.
- Specify context, tools, memory and human oversight only if the workflow requires them.
- List one normal case, one edge case, one malicious case and one tool-failure case.
- Recommend pilot, prepare, redesign, defer or stop, with evidence required for the next decision.

| Decision area | Your analysis |
|---|---|
| Value and stakeholder impact |  |
| Feasibility and dependencies |  |
| Risks and prohibited actions |  |
| Controls and human owner |  |
| Measures and gate decision |  |

| Discussion prompt: How would the recommendation change if the workflow moved from internal use to a customer-facing channel? Relate your answer to Topic 4. |
|---|

### Lab 4 - Build an AI Opportunity Scoring App with Claude Code and Codex

| Goal: Use Claude Code and Codex on the same repository to build and verify a small browser app that scores business opportunities by value, feasibility, risk and human-oversight needs. |
|---|

Alignment: LO2-LO4 · Topic 4

Deliverable: A responsive opportunity-scoring web app with tests, sample data, README and review evidence

Tools: Claude Code, Codex, HTML/CSS/JavaScript, local browser, Git

| Configuration / constraint | Required evidence |
|---|---|
| Inputs: opportunity name and 1-5 ratings for value, feasibility, operational impact, risk and human-oversight need. | Record the configured value or resulting evidence. |
| Score: (value x 0.35) + (feasibility x 0.30) + (impact x 0.20) - (risk x 0.10) - (oversight x 0.05). | Record the configured value or resulting evidence. |
| Show the score, priority band and a plain-language rationale. | Record the configured value or resulting evidence. |
| Validate missing/out-of-range input and support desktop, mobile and keyboard use. | Record the configured value or resulting evidence. |

- Use only non-confidential training data and approved accounts.
- Record the source, model or service, date, prompt or instruction, tool actions and human approval.
- Stop if access, permissions, pricing or the active interface differs materially from the guide.
- Do not connect production credentials or send external communications during the lab.

| Acceptance standard: The app calculates the documented score, works at desktop and mobile widths, handles invalid inputs, passes its checks, and the final diff was reviewed by a human before acceptance. |
|---|

LAB DESIGN

Lab 4 - Workflow and Control Design

| Stage | Lab decision |
|---|---|
| Intent | State the business outcome and exclusions |
| Context | Supply only relevant, approved information |
| Action | Generate, reason or call a scoped tool |
| Observation | Capture output, status and evidence |
| Evaluation | Compare with acceptance criteria |
| Decision | Complete, improve, stop or escalate |

Control boundary:

| Control boundary: Coding agents may edit the training repository and run checks; a human reviews the diff before acceptance. |
|---|

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |

STEP-BY-STEP

Lab 4 - Guided Procedure 1 of 3

#### Step 1

Initialise a Git repository and write acceptance criteria before asking either coding agent to edit.

| Command: git init && git status |
|---|

- Expected result: the interface or command reports a successful, reviewable state.
- Evidence: capture the relevant screen, execution record, file or diff without exposing secrets.
- If different: stop, confirm the current product interface and resolve permissions before continuing.

#### Step 2

Ask Claude Code to inspect the brief, propose a plan and implement the first working version.

| Command: claude |
|---|

- Expected result: the interface or command reports a successful, reviewable state.
- Evidence: capture the relevant screen, execution record, file or diff without exposing secrets.
- If different: stop, confirm the current product interface and resolve permissions before continuing.

| Checkpoint: Explain what changed, what evidence proves it, and whether any external state was affected. |
|---|

STEP-BY-STEP

Lab 4 - Guided Procedure 2 of 3

#### Step 3

Run the app and tests; record defects and commit the verified baseline.

| Command: python3 -m http.server 8000 |
|---|

- Expected result: the interface or command reports a successful, reviewable state.
- Evidence: capture the relevant screen, execution record, file or diff without exposing secrets.
- If different: stop, confirm the current product interface and resolve permissions before continuing.

#### Step 4

Ask Codex to review the repository, improve accessibility and add tests without changing the scoring contract.

| Command: codex |
|---|

- Expected result: the interface or command reports a successful, reviewable state.
- Evidence: capture the relevant screen, execution record, file or diff without exposing secrets.
- If different: stop, confirm the current product interface and resolve permissions before continuing.

| Checkpoint: Explain what changed, what evidence proves it, and whether any external state was affected. |
|---|

STEP-BY-STEP

Lab 4 - Guided Procedure 3 of 3

#### Step 5

Inspect the diff, run all checks and reject any change that is not supported by evidence.

- Expected result: the interface or command reports a successful, reviewable state.
- Evidence: capture the relevant screen, execution record, file or diff without exposing secrets.
- If different: stop, confirm the current product interface and resolve permissions before continuing.

#### Step 6

Compare planning, context use, tool calls, verification and human-control points across both agents.

- Expected result: the interface or command reports a successful, reviewable state.
- Evidence: capture the relevant screen, execution record, file or diff without exposing secrets.
- If different: stop, confirm the current product interface and resolve permissions before continuing.

| Checkpoint: Explain what changed, what evidence proves it, and whether any external state was affected. |
|---|

COPY-PASTE BRIEF

Lab 4 - Instructions, Prompt and Source Boundary

| Copy-paste prompt: Inspect APP-BRIEF.md and the current repository. Propose a short plan before editing. Build a responsive, accessible opportunity-scoring app using plain HTML, CSS and JavaScript. Preserve the documented scoring contract, validate all inputs, include representative sample data and tests, and update README.md. Run the checks and report evidence. Do not install dependencies or change the formula without approval. |
|---|

Review the brief before use. Replace only the scenario-specific details; preserve the source boundary, prohibited actions, output contract and escalation rule.

| Instruction component | Why it matters |
|---|---|
| Outcome and audience | Prevents a fluent but unusable deliverable |
| Approved source boundary | Reduces unsupported claims and privacy exposure |
| Required output structure | Makes results reviewable and machine-checkable |
| Prohibited actions | Blocks unsafe interpretation of a broad goal |
| Approval and stop conditions | Keeps accountability with the named person |

| Notes 1: |
|---|
| Notes 2: |

VERIFY BEFORE ACCEPTING

Lab 4 - Test Plan and Failure Cases

| Test case | Expected controlled behaviour |
|---|---|
| Normal | Valid scores on desktop |
| Edge | Blank or out-of-range input |
| Accessibility | Keyboard-only and narrow viewport |
| Agent error | Unapproved dependency or scoring change |

- Record actual result, evidence and pass/fail status for every test.
- A failure is useful evidence; do not hide it by changing the expected result after the run.
- Do not retry a consequential action unless the system proves the first attempt had no effect.
- Escalate when the result is uncertain or the acceptance criterion cannot be observed.

| Acceptance criterion: The app calculates the documented score, works at desktop and mobile widths, handles invalid inputs, passes its checks, and the final diff was reviewed by a human before acceptance. |
|---|

COMPLETE THE ACTIVITY

Lab 4 - Evidence Pack and Reflection

- Business brief and baseline problem statement.
- Prompt or instruction version and approved source list.
- Screenshots or execution records showing the workflow and controls.
- Test results for normal, edge, malicious and tool-failure cases.
- Human review decision, outstanding risks and next recommended gate.
Reference tool view for Lab 4

| Reflection: Which part was generation, which part was agentic behaviour, and which part belonged to the harness? What would need to change before production use? |
|---|

| Notes 1: |
|---|
| Notes 2: |

RETRIEVAL PRACTICE

Topic 4 - Knowledge Check

1. Explain the central business decision in business opportunities and innovative agentic ai use cases.

Response: ______________________________________________________________________

________________________________________________________________________________

2. Distinguish the AI capability from the workflow and the deployed agent system.

Response: ______________________________________________________________________

________________________________________________________________________________

3. Name two forms of evidence that would support a pilot decision.

Response: ______________________________________________________________________

________________________________________________________________________________

4. Identify one consequential action and the human approval it requires.

Response: ______________________________________________________________________

________________________________________________________________________________

5. Describe one failure case and the control that should contain it.

Response: ______________________________________________________________________

________________________________________________________________________________

6. State one metric that measures business value and one that measures operational safety.

Response: ______________________________________________________________________

________________________________________________________________________________

SCENARIO QUESTIONS

Topic 4 - Applied Review

| Scenario: A finance team reconciles invoices, purchase orders and approvals across email, spreadsheets and an ERP. |
|---|

- What outcome should be measured before any technology is selected?
- Which AI approach is proportionate to the task and why?
- What context and evidence are necessary? What information should be excluded?
- Which tool actions are reversible, and which require explicit approval?
- What should the agent do after an ambiguous result or failed tool call?
- Which gate should the initiative pass next, and what evidence is still missing?

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |
| Notes 4: |
| Notes 5: |

TRANSFER TO PRACTICE

Topic 4 - Workplace Action Plan

| Action: Choose one non-confidential workflow and identify a small, measurable next step that applies this topic without granting unnecessary authority. |
|---|

| Planning field | Your decision |
|---|---|
| Workflow and owner |  |
| Current baseline |  |
| Proposed AI contribution |  |
| Source and tool boundary |  |
| Human approval |  |
| Test and success measure |  |
| Next review date |  |

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |

## Topic 5 - Evaluating and Implementing AI-Driven Business Innovation

| Topic purpose: This topic develops the ability to value and feasibility · process redesign · prototype · measurement · roadmap · governance and apply the ideas to a governed business innovation decision. |
|---|

- Value: Revenue, cost, cycle time, quality, experience, capacity and strategic learning.
- Feasibility: Data readiness, process stability, integration effort, skills, risk and change capacity.
- Process redesign: Allocate judgement, repetition, approval and accountability deliberately between people and agents.
- Prototype: Test a narrow workflow with representative cases, failure modes and measurable acceptance criteria.
- Governance: Ownership, access, privacy, security, auditability, incident response and vendor controls.
- Roadmap: Discover → prioritise → prototype → pilot → scale → monitor and continuously improve.
Evidence of learning includes a completed comparison or decision worksheet, a case recommendation, the lab evidence pack and the two knowledge checks.

| Guiding question: What business decision becomes clearer after learning this topic, and what evidence would support that decision? |
|---|

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |

### 5.1 Value

| Core idea: Revenue, cost, cycle time, quality, experience, capacity and strategic learning. |
|---|

Value is useful only when it changes how a team frames a business decision. In this topic, the concept connects directly to value and feasibility · process redesign · prototype · measurement · roadmap · governance. It gives managers a vocabulary for separating a promising demonstration from a reliable operating capability. The practical test is whether the concept helps the team describe the goal, evidence, boundary and accountable owner more precisely.

The organisation should translate the idea into process decisions: what information is needed, who supplies it, what the AI may produce or change, which outcome is measured, and where a person must approve or resolve ambiguity. This prevents technology features from becoming disconnected experiments.

- Ask what evidence would demonstrate that 'Value' improves a real outcome.
- Identify the business record, system or stakeholder affected by the decision.
- Separate a reversible draft from a consequential external action.
- Name the owner who can pause, change or retire the workflow.

| Manager takeaway: Treat the concept as a design decision with evidence and ownership, not as a label. |
|---|

APPLICATION WORKSHEET

5.1 Apply Value

Apply value to a workflow you know. Start with the current process before describing any AI solution. Record the trigger, inputs, decisions, systems, hand-offs, exceptions, outputs and measures. Then use the concept to propose one controlled change.

| Current workflow | AI-enabled redesign |
|---|---|
| Trigger and customer need | How intent will enter the workflow |
| Information and evidence | What context the system may use |
| Human decisions and hand-offs | What the AI prepares, recommends or executes |
| Systems and records | Tools and permissions required |
| Exceptions and failures | Escalation, retry and stop behaviour |
| Outcome and baseline | Target metric and acceptance threshold |

Application questions:

- Where does value create value, and where could it create new risk?
- What must be true about data, process stability and user behaviour?
- What evidence would cause the team to continue, revise or stop?
- How will the human owner understand and challenge the system's output?

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |

CONCEPT EXPLANATION

5.2 Feasibility

| Core idea: Data readiness, process stability, integration effort, skills, risk and change capacity. |
|---|

Feasibility is useful only when it changes how a team frames a business decision. In this topic, the concept connects directly to value and feasibility · process redesign · prototype · measurement · roadmap · governance. It gives managers a vocabulary for separating a promising demonstration from a reliable operating capability. The practical test is whether the concept helps the team describe the goal, evidence, boundary and accountable owner more precisely.

The organisation should translate the idea into process decisions: what information is needed, who supplies it, what the AI may produce or change, which outcome is measured, and where a person must approve or resolve ambiguity. This prevents technology features from becoming disconnected experiments.

- Ask what evidence would demonstrate that 'Feasibility' improves a real outcome.
- Identify the business record, system or stakeholder affected by the decision.
- Separate a reversible draft from a consequential external action.
- Name the owner who can pause, change or retire the workflow.

| Manager takeaway: Treat the concept as a design decision with evidence and ownership, not as a label. |
|---|

APPLICATION WORKSHEET

5.2 Apply Feasibility

Apply feasibility to a workflow you know. Start with the current process before describing any AI solution. Record the trigger, inputs, decisions, systems, hand-offs, exceptions, outputs and measures. Then use the concept to propose one controlled change.

| Current workflow | AI-enabled redesign |
|---|---|
| Trigger and customer need | How intent will enter the workflow |
| Information and evidence | What context the system may use |
| Human decisions and hand-offs | What the AI prepares, recommends or executes |
| Systems and records | Tools and permissions required |
| Exceptions and failures | Escalation, retry and stop behaviour |
| Outcome and baseline | Target metric and acceptance threshold |

Application questions:

- Where does feasibility create value, and where could it create new risk?
- What must be true about data, process stability and user behaviour?
- What evidence would cause the team to continue, revise or stop?
- How will the human owner understand and challenge the system's output?

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |

CONCEPT EXPLANATION

5.3 Process redesign

| Core idea: Allocate judgement, repetition, approval and accountability deliberately between people and agents. |
|---|

Process redesign is useful only when it changes how a team frames a business decision. In this topic, the concept connects directly to value and feasibility · process redesign · prototype · measurement · roadmap · governance. It gives managers a vocabulary for separating a promising demonstration from a reliable operating capability. The practical test is whether the concept helps the team describe the goal, evidence, boundary and accountable owner more precisely.

The organisation should translate the idea into process decisions: what information is needed, who supplies it, what the AI may produce or change, which outcome is measured, and where a person must approve or resolve ambiguity. This prevents technology features from becoming disconnected experiments.

- Ask what evidence would demonstrate that 'Process redesign' improves a real outcome.
- Identify the business record, system or stakeholder affected by the decision.
- Separate a reversible draft from a consequential external action.
- Name the owner who can pause, change or retire the workflow.

| Manager takeaway: Treat the concept as a design decision with evidence and ownership, not as a label. |
|---|

APPLICATION WORKSHEET

5.3 Apply Process redesign

Apply process redesign to a workflow you know. Start with the current process before describing any AI solution. Record the trigger, inputs, decisions, systems, hand-offs, exceptions, outputs and measures. Then use the concept to propose one controlled change.

| Current workflow | AI-enabled redesign |
|---|---|
| Trigger and customer need | How intent will enter the workflow |
| Information and evidence | What context the system may use |
| Human decisions and hand-offs | What the AI prepares, recommends or executes |
| Systems and records | Tools and permissions required |
| Exceptions and failures | Escalation, retry and stop behaviour |
| Outcome and baseline | Target metric and acceptance threshold |

Application questions:

- Where does process redesign create value, and where could it create new risk?
- What must be true about data, process stability and user behaviour?
- What evidence would cause the team to continue, revise or stop?
- How will the human owner understand and challenge the system's output?

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |

CONCEPT EXPLANATION

5.4 Prototype

| Core idea: Test a narrow workflow with representative cases, failure modes and measurable acceptance criteria. |
|---|

Prototype is useful only when it changes how a team frames a business decision. In this topic, the concept connects directly to value and feasibility · process redesign · prototype · measurement · roadmap · governance. It gives managers a vocabulary for separating a promising demonstration from a reliable operating capability. The practical test is whether the concept helps the team describe the goal, evidence, boundary and accountable owner more precisely.

The organisation should translate the idea into process decisions: what information is needed, who supplies it, what the AI may produce or change, which outcome is measured, and where a person must approve or resolve ambiguity. This prevents technology features from becoming disconnected experiments.

- Ask what evidence would demonstrate that 'Prototype' improves a real outcome.
- Identify the business record, system or stakeholder affected by the decision.
- Separate a reversible draft from a consequential external action.
- Name the owner who can pause, change or retire the workflow.

| Manager takeaway: Treat the concept as a design decision with evidence and ownership, not as a label. |
|---|

APPLICATION WORKSHEET

5.4 Apply Prototype

Apply prototype to a workflow you know. Start with the current process before describing any AI solution. Record the trigger, inputs, decisions, systems, hand-offs, exceptions, outputs and measures. Then use the concept to propose one controlled change.

| Current workflow | AI-enabled redesign |
|---|---|
| Trigger and customer need | How intent will enter the workflow |
| Information and evidence | What context the system may use |
| Human decisions and hand-offs | What the AI prepares, recommends or executes |
| Systems and records | Tools and permissions required |
| Exceptions and failures | Escalation, retry and stop behaviour |
| Outcome and baseline | Target metric and acceptance threshold |

Application questions:

- Where does prototype create value, and where could it create new risk?
- What must be true about data, process stability and user behaviour?
- What evidence would cause the team to continue, revise or stop?
- How will the human owner understand and challenge the system's output?

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |

CONCEPT EXPLANATION

5.5 Governance

| Core idea: Ownership, access, privacy, security, auditability, incident response and vendor controls. |
|---|

Governance is useful only when it changes how a team frames a business decision. In this topic, the concept connects directly to value and feasibility · process redesign · prototype · measurement · roadmap · governance. It gives managers a vocabulary for separating a promising demonstration from a reliable operating capability. The practical test is whether the concept helps the team describe the goal, evidence, boundary and accountable owner more precisely.

The organisation should translate the idea into process decisions: what information is needed, who supplies it, what the AI may produce or change, which outcome is measured, and where a person must approve or resolve ambiguity. This prevents technology features from becoming disconnected experiments.

- Ask what evidence would demonstrate that 'Governance' improves a real outcome.
- Identify the business record, system or stakeholder affected by the decision.
- Separate a reversible draft from a consequential external action.
- Name the owner who can pause, change or retire the workflow.

| Manager takeaway: Treat the concept as a design decision with evidence and ownership, not as a label. |
|---|

APPLICATION WORKSHEET

5.5 Apply Governance

Apply governance to a workflow you know. Start with the current process before describing any AI solution. Record the trigger, inputs, decisions, systems, hand-offs, exceptions, outputs and measures. Then use the concept to propose one controlled change.

| Current workflow | AI-enabled redesign |
|---|---|
| Trigger and customer need | How intent will enter the workflow |
| Information and evidence | What context the system may use |
| Human decisions and hand-offs | What the AI prepares, recommends or executes |
| Systems and records | Tools and permissions required |
| Exceptions and failures | Escalation, retry and stop behaviour |
| Outcome and baseline | Target metric and acceptance threshold |

Application questions:

- Where does governance create value, and where could it create new risk?
- What must be true about data, process stability and user behaviour?
- What evidence would cause the team to continue, revise or stop?
- How will the human owner understand and challenge the system's output?

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |

CONCEPT EXPLANATION

5.6 Roadmap

| Core idea: Discover → prioritise → prototype → pilot → scale → monitor and continuously improve. |
|---|

Roadmap is useful only when it changes how a team frames a business decision. In this topic, the concept connects directly to value and feasibility · process redesign · prototype · measurement · roadmap · governance. It gives managers a vocabulary for separating a promising demonstration from a reliable operating capability. The practical test is whether the concept helps the team describe the goal, evidence, boundary and accountable owner more precisely.

The organisation should translate the idea into process decisions: what information is needed, who supplies it, what the AI may produce or change, which outcome is measured, and where a person must approve or resolve ambiguity. This prevents technology features from becoming disconnected experiments.

- Ask what evidence would demonstrate that 'Roadmap' improves a real outcome.
- Identify the business record, system or stakeholder affected by the decision.
- Separate a reversible draft from a consequential external action.
- Name the owner who can pause, change or retire the workflow.

| Manager takeaway: Treat the concept as a design decision with evidence and ownership, not as a label. |
|---|

APPLICATION WORKSHEET

5.6 Apply Roadmap

Apply roadmap to a workflow you know. Start with the current process before describing any AI solution. Record the trigger, inputs, decisions, systems, hand-offs, exceptions, outputs and measures. Then use the concept to propose one controlled change.

| Current workflow | AI-enabled redesign |
|---|---|
| Trigger and customer need | How intent will enter the workflow |
| Information and evidence | What context the system may use |
| Human decisions and hand-offs | What the AI prepares, recommends or executes |
| Systems and records | Tools and permissions required |
| Exceptions and failures | Escalation, retry and stop behaviour |
| Outcome and baseline | Target metric and acceptance threshold |

Application questions:

- Where does roadmap create value, and where could it create new risk?
- What must be true about data, process stability and user behaviour?
- What evidence would cause the team to continue, revise or stop?
- How will the human owner understand and challenge the system's output?

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |

### 5.F1 Value-feasibility matrix

| Framework definition: Score value and feasibility separately before considering urgency or sponsorship. |
|---|

When to use it: Use the matrix to distinguish pilot-now opportunities from prepare-first opportunities.

Watch for: A high-value idea with unstable data or unacceptable risk is not ready for automation.

A useful framework reduces ambiguity. It should allow two people to examine the same opportunity, state their assumptions and reach a traceable decision. Apply it with representative examples rather than idealised demonstrations.

- Define the unit of analysis: task, workflow, customer journey or operating model.
- Record assumptions separately from verified evidence.
- Use a simple rating scale with written justification.
- Review disagreements; they often reveal missing data or different risk tolerances.
- Assign a next action and owner before closing the discussion.

| Diagnostic question | Evidence to collect |
|---|---|
| What problem does this framework clarify? | Baseline process map, delay, error or cost data |
| What decision follows? | Pilot, preparation, redesign, defer or stop |
| Who owns the decision? | Named business and technology owners |
| When is it reviewed? | Gate date, metric threshold and review cadence |

BUSINESS FRAMEWORK

5.F2 Total business case

| Framework definition: Include labour, cycle time, quality, rework, revenue, integration, licences, model usage, oversight, change and risk exposure. |
|---|

When to use it: Use ranges and sensitivity analysis rather than a single confident return estimate.

Watch for: Do not omit human review and maintenance costs from an agentic-AI business case.

A useful framework reduces ambiguity. It should allow two people to examine the same opportunity, state their assumptions and reach a traceable decision. Apply it with representative examples rather than idealised demonstrations.

- Define the unit of analysis: task, workflow, customer journey or operating model.
- Record assumptions separately from verified evidence.
- Use a simple rating scale with written justification.
- Review disagreements; they often reveal missing data or different risk tolerances.
- Assign a next action and owner before closing the discussion.

| Diagnostic question | Evidence to collect |
|---|---|
| What problem does this framework clarify? | Baseline process map, delay, error or cost data |
| What decision follows? | Pilot, preparation, redesign, defer or stop |
| Who owns the decision? | Named business and technology owners |
| When is it reviewed? | Gate date, metric threshold and review cadence |

BUSINESS FRAMEWORK

5.F3 Human-AI process design

| Framework definition: Assign each step as human-led, AI-assisted, agent-executed with review, or fully automated within policy. |
|---|

When to use it: Use the design to remove duplicate checks while preserving accountable decisions.

Watch for: Avoid designing a shadow process in which staff repeat every agent action because trust was never engineered.

A useful framework reduces ambiguity. It should allow two people to examine the same opportunity, state their assumptions and reach a traceable decision. Apply it with representative examples rather than idealised demonstrations.

- Define the unit of analysis: task, workflow, customer journey or operating model.
- Record assumptions separately from verified evidence.
- Use a simple rating scale with written justification.
- Review disagreements; they often reveal missing data or different risk tolerances.
- Assign a next action and owner before closing the discussion.

| Diagnostic question | Evidence to collect |
|---|---|
| What problem does this framework clarify? | Baseline process map, delay, error or cost data |
| What decision follows? | Pilot, preparation, redesign, defer or stop |
| Who owns the decision? | Named business and technology owners |
| When is it reviewed? | Gate date, metric threshold and review cadence |

BUSINESS FRAMEWORK

5.F4 Stage-gated roadmap

| Framework definition: Use discover, prioritise, prototype, pilot, scale and improve gates with evidence required at each transition. |
|---|

When to use it: Use stage gates to stop weak initiatives early and concentrate investment on proven workflows.

Watch for: A successful demo is not evidence of operational readiness, security or sustainable value.

A useful framework reduces ambiguity. It should allow two people to examine the same opportunity, state their assumptions and reach a traceable decision. Apply it with representative examples rather than idealised demonstrations.

- Define the unit of analysis: task, workflow, customer journey or operating model.
- Record assumptions separately from verified evidence.
- Use a simple rating scale with written justification.
- Review disagreements; they often reveal missing data or different risk tolerances.
- Assign a next action and owner before closing the discussion.

| Diagnostic question | Evidence to collect |
|---|---|
| What problem does this framework clarify? | Baseline process map, delay, error or cost data |
| What decision follows? | Pilot, preparation, redesign, defer or stop |
| Who owns the decision? | Named business and technology owners |
| When is it reviewed? | Gate date, metric threshold and review cadence |

### Case 5.1 - Pilot with impressive demos

| Scenario: A prototype works on ten curated examples but fails on missing data and ambiguous requests. |
|---|

Your assignment: Define representative testing, baseline measures and a stage-gate decision.

- State the business outcome in one sentence without naming a technology.
- Identify the current bottleneck and quantify it with a baseline or a measurement plan.
- Choose the appropriate AI approach and justify the boundary of action.
- Specify context, tools, memory and human oversight only if the workflow requires them.
- List one normal case, one edge case, one malicious case and one tool-failure case.
- Recommend pilot, prepare, redesign, defer or stop, with evidence required for the next decision.

| Decision area | Your analysis |
|---|---|
| Value and stakeholder impact |  |
| Feasibility and dependencies |  |
| Risks and prohibited actions |  |
| Controls and human owner |  |
| Measures and gate decision |  |

| Discussion prompt: How would the recommendation change if the workflow moved from internal use to a customer-facing channel? Relate your answer to Topic 5. |
|---|

WORKED BUSINESS CASE

Case 5.2 - ROI under uncertainty

| Scenario: A sponsor claims a six-month payback using only labour savings and ignores integration, review and change costs. |
|---|

Your assignment: Rebuild the business case with ranges, sensitivity and risk-adjusted benefits.

- State the business outcome in one sentence without naming a technology.
- Identify the current bottleneck and quantify it with a baseline or a measurement plan.
- Choose the appropriate AI approach and justify the boundary of action.
- Specify context, tools, memory and human oversight only if the workflow requires them.
- List one normal case, one edge case, one malicious case and one tool-failure case.
- Recommend pilot, prepare, redesign, defer or stop, with evidence required for the next decision.

| Decision area | Your analysis |
|---|---|
| Value and stakeholder impact |  |
| Feasibility and dependencies |  |
| Risks and prohibited actions |  |
| Controls and human owner |  |
| Measures and gate decision |  |

| Discussion prompt: How would the recommendation change if the workflow moved from internal use to a customer-facing channel? Relate your answer to Topic 5. |
|---|

WORKED BUSINESS CASE

Case 5.3 - Scaling responsibly

| Scenario: A successful internal agent is proposed for customer-facing use across several countries. |
|---|

Your assignment: Create a roadmap covering data classification, security, legal review, monitoring, localisation and rollback.

- State the business outcome in one sentence without naming a technology.
- Identify the current bottleneck and quantify it with a baseline or a measurement plan.
- Choose the appropriate AI approach and justify the boundary of action.
- Specify context, tools, memory and human oversight only if the workflow requires them.
- List one normal case, one edge case, one malicious case and one tool-failure case.
- Recommend pilot, prepare, redesign, defer or stop, with evidence required for the next decision.

| Decision area | Your analysis |
|---|---|
| Value and stakeholder impact |  |
| Feasibility and dependencies |  |
| Risks and prohibited actions |  |
| Controls and human owner |  |
| Measures and gate decision |  |

| Discussion prompt: How would the recommendation change if the workflow moved from internal use to a customer-facing channel? Relate your answer to Topic 5. |
|---|

### Lab 5 - Configure a Governed Digital Worker with Hermes Agent

| Goal: Configure a small Hermes digital worker that remembers approved operating preferences, uses one audited skill, produces a scheduled briefing and escalates consequential actions. |
|---|

Alignment: LO5 · Topic 5

Deliverable: A named digital worker with durable memory, one skill, a safe recurring task and an implementation control sheet

Tools: Hermes Agent, persistent memory, skills, scheduling, channels, human approval

| Configuration / constraint | Required evidence |
|---|---|
| Approved actions: read approved local sources and write one dated Markdown briefing locally. | Record the configured value or resulting evidence. |
| Required controls: named owner, least privilege, budget, timeout, three-attempt loop limit, approval threshold, audit log and kill switch. | Record the configured value or resulting evidence. |
| Consequential actions and external communications remain blocked. | Record the configured value or resulting evidence. |

- Use only non-confidential training data and approved accounts.
- Record the source, model or service, date, prompt or instruction, tool actions and human approval.
- Stop if access, permissions, pricing or the active interface differs materially from the guide.
- Do not connect production credentials or send external communications during the lab.

| Acceptance standard: Hermes recalls only the approved preferences, the skill uses expected tools, the scheduled task creates one local briefing, consequential actions remain blocked, and the control sheet names the owner and rollback path. |
|---|

LAB DESIGN

Lab 5 - Workflow and Control Design

| Stage | Lab decision |
|---|---|
| Intent | State the business outcome and exclusions |
| Context | Supply only relevant, approved information |
| Action | Generate, reason or call a scoped tool |
| Observation | Capture output, status and evidence |
| Evaluation | Compare with acceptance criteria |
| Decision | Complete, improve, stop or escalate |

Control boundary:

| Control boundary: Hermes may read approved local sources and create one local briefing; consequential actions remain blocked. |
|---|

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |

STEP-BY-STEP

Lab 5 - Guided Procedure 1 of 4

#### Step 1

Install Hermes using the official method, run setup and confirm a healthy local profile.

| Command: hermes doctor |
|---|

- Expected result: the interface or command reports a successful, reviewable state.
- Evidence: capture the relevant screen, execution record, file or diff without exposing secrets.
- If different: stop, confirm the current product interface and resolve permissions before continuing.

#### Step 2

Define the worker's role, business goal, source boundaries and prohibited actions.

- Expected result: the interface or command reports a successful, reviewable state.
- Evidence: capture the relevant screen, execution record, file or diff without exposing secrets.
- If different: stop, confirm the current product interface and resolve permissions before continuing.

| Checkpoint: Explain what changed, what evidence proves it, and whether any external state was affected. |
|---|

STEP-BY-STEP

Lab 5 - Guided Procedure 2 of 4

#### Step 3

Teach two durable preferences and verify recall in a continued session.

| Command: hermes --continue |
|---|

- Expected result: the interface or command reports a successful, reviewable state.
- Evidence: capture the relevant screen, execution record, file or diff without exposing secrets.
- If different: stop, confirm the current product interface and resolve permissions before continuing.

#### Step 4

Install or create one narrow skill; inspect its instructions and requested tools before enabling it.

- Expected result: the interface or command reports a successful, reviewable state.
- Evidence: capture the relevant screen, execution record, file or diff without exposing secrets.
- If different: stop, confirm the current product interface and resolve permissions before continuing.

| Checkpoint: Explain what changed, what evidence proves it, and whether any external state was affected. |
|---|

STEP-BY-STEP

Lab 5 - Guided Procedure 3 of 4

#### Step 5

Create a scheduled internal briefing that reads approved sources and writes only to a local output.

- Expected result: the interface or command reports a successful, reviewable state.
- Evidence: capture the relevant screen, execution record, file or diff without exposing secrets.
- If different: stop, confirm the current product interface and resolve permissions before continuing.

#### Step 6

Add budget, timeout, loop limit, approval and kill-switch controls; test a forced escalation.

- Expected result: the interface or command reports a successful, reviewable state.
- Evidence: capture the relevant screen, execution record, file or diff without exposing secrets.
- If different: stop, confirm the current product interface and resolve permissions before continuing.

| Checkpoint: Explain what changed, what evidence proves it, and whether any external state was affected. |
|---|

STEP-BY-STEP

Lab 5 - Guided Procedure 4 of 4

#### Step 7

Force a missing-source condition and verify escalation instead of repetition or fabrication.

- Expected result: the interface or command reports a successful, reviewable state.
- Evidence: capture the relevant screen, execution record, file or diff without exposing secrets.
- If different: stop, confirm the current product interface and resolve permissions before continuing.

| Checkpoint: Explain what changed, what evidence proves it, and whether any external state was affected. |
|---|

COPY-PASTE BRIEF

Lab 5 - Instructions, Prompt and Source Boundary

| Copy-paste prompt: You are an internal business-innovation briefing worker. Read only approved local sources, summarise new opportunities and risks, and write one dated Markdown briefing to the approved output folder. Never send messages, modify source files, purchase services, expose secrets or repeat a failed action. Escalate when evidence conflicts, a tool is unavailable, or the loop reaches three attempts. |
|---|

Review the brief before use. Replace only the scenario-specific details; preserve the source boundary, prohibited actions, output contract and escalation rule.

| Instruction component | Why it matters |
|---|---|
| Outcome and audience | Prevents a fluent but unusable deliverable |
| Approved source boundary | Reduces unsupported claims and privacy exposure |
| Required output structure | Makes results reviewable and machine-checkable |
| Prohibited actions | Blocks unsafe interpretation of a broad goal |
| Approval and stop conditions | Keeps accountability with the named person |

| Notes 1: |
|---|
| Notes 2: |

VERIFY BEFORE ACCEPTING

Lab 5 - Test Plan and Failure Cases

| Test case | Expected controlled behaviour |
|---|---|
| Normal | One scheduled local briefing |
| Edge | No new information |
| Conflict | Approved sources disagree |
| Loop failure | Tool remains unavailable for three attempts |

- Record actual result, evidence and pass/fail status for every test.
- A failure is useful evidence; do not hide it by changing the expected result after the run.
- Do not retry a consequential action unless the system proves the first attempt had no effect.
- Escalate when the result is uncertain or the acceptance criterion cannot be observed.

| Acceptance criterion: Hermes recalls only the approved preferences, the skill uses expected tools, the scheduled task creates one local briefing, consequential actions remain blocked, and the control sheet names the owner and rollback path. |
|---|

COMPLETE THE ACTIVITY

Lab 5 - Evidence Pack and Reflection

- Business brief and baseline problem statement.
- Prompt or instruction version and approved source list.
- Screenshots or execution records showing the workflow and controls.
- Test results for normal, edge, malicious and tool-failure cases.
- Human review decision, outstanding risks and next recommended gate.
Reference tool view for Lab 5

| Reflection: Which part was generation, which part was agentic behaviour, and which part belonged to the harness? What would need to change before production use? |
|---|

| Notes 1: |
|---|
| Notes 2: |

RETRIEVAL PRACTICE

Topic 5 - Knowledge Check

1. Explain the central business decision in evaluating and implementing ai-driven business innovation.

Response: ______________________________________________________________________

________________________________________________________________________________

2. Distinguish the AI capability from the workflow and the deployed agent system.

Response: ______________________________________________________________________

________________________________________________________________________________

3. Name two forms of evidence that would support a pilot decision.

Response: ______________________________________________________________________

________________________________________________________________________________

4. Identify one consequential action and the human approval it requires.

Response: ______________________________________________________________________

________________________________________________________________________________

5. Describe one failure case and the control that should contain it.

Response: ______________________________________________________________________

________________________________________________________________________________

6. State one metric that measures business value and one that measures operational safety.

Response: ______________________________________________________________________

________________________________________________________________________________

SCENARIO QUESTIONS

Topic 5 - Applied Review

| Scenario: A prototype works on ten curated examples but fails on missing data and ambiguous requests. |
|---|

- What outcome should be measured before any technology is selected?
- Which AI approach is proportionate to the task and why?
- What context and evidence are necessary? What information should be excluded?
- Which tool actions are reversible, and which require explicit approval?
- What should the agent do after an ambiguous result or failed tool call?
- Which gate should the initiative pass next, and what evidence is still missing?

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |
| Notes 4: |
| Notes 5: |

TRANSFER TO PRACTICE

Topic 5 - Workplace Action Plan

| Action: Choose one non-confidential workflow and identify a small, measurable next step that applies this topic without granting unnecessary authority. |
|---|

| Planning field | Your decision |
|---|---|
| Workflow and owner |  |
| Current baseline |  |
| Proposed AI contribution |  |
| Source and tool boundary |  |
| Human approval |  |
| Test and success measure |  |
| Next review date |  |

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |

## Appendix A - Glossary: Agent Components

| Term | Meaning |
|---|---|
| Agent | A deployed system that pursues a goal using a model, instructions, context, state, tools and an execution loop. |
| Channel | A surface through which the agent receives or sends work, such as chat, terminal, email or API. |
| Context | The selected working set used for the current decision. |
| Harness | The environment that constrains, enables, tests and observes agent behaviour. |
| Memory | Approved information retained across steps or sessions with an owner and retention rule. |
| Skill | Reusable instructions and tool patterns for a bounded task. |
| Tool | A callable capability that reads, calculates or changes external state. |

Use the glossary language consistently in opportunity proposals, test plans and governance documents.

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |

REFERENCE

Appendix A - Glossary: Control Terms

| Term | Meaning |
|---|---|
| Allowlist | A defined set of actions, destinations or resources the system may use. |
| Budget | A limit on time, tokens, money, actions or other resource consumption. |
| Checkpoint | A review state before the workflow continues. |
| Idempotency | A design that prevents a repeated request from creating duplicate effects. |
| Kill switch | A mechanism that stops further execution. |
| Least privilege | Granting only the access required for the current task. |
| Timeout | A limit after which the system stops waiting and follows a defined recovery path. |

Use the glossary language consistently in opportunity proposals, test plans and governance documents.

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |

REFERENCE

Appendix A - Glossary: Innovation Terms

| Term | Meaning |
|---|---|
| Baseline | The current performance against which improvement is measured. |
| Business model | How an organisation creates, delivers and captures value. |
| Digital worker | A governed agent assigned a bounded set of ongoing tasks. |
| Feasibility | The practical readiness of data, process, technology, people and controls. |
| Pilot | A limited operational trial using representative work and defined measures. |
| Prototype | An early implementation used to test assumptions and failure modes. |
| Value | The measurable benefit to customers, staff, operations or strategic capability. |

Use the glossary language consistently in opportunity proposals, test plans and governance documents.

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |

## Appendix B - AI Opportunity Canvas

| Field | Decision / evidence |
|---|---|
| Business outcome |  |
| Customer or user |  |
| Trigger |  |
| Current friction |  |
| Baseline |  |
| Proposed AI contribution |  |
| Owner |  |

Complete every field with evidence or mark it explicitly as unknown. Unknowns become preparation tasks; they should not be converted into confident assumptions.

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |
| Notes 4: |

REUSABLE WORKSHEET

Appendix B - AI Opportunity Canvas: Boundary

| Field | Decision / evidence |
|---|---|
| Approved sources |  |
| Tools and permissions |  |
| Prohibited actions |  |
| Human approval |  |
| Exceptions |  |
| Success measure |  |
| Next gate |  |

Complete every field with evidence or mark it explicitly as unknown. Unknowns become preparation tasks; they should not be converted into confident assumptions.

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |
| Notes 4: |

REUSABLE WORKSHEET

Appendix C - Agent Control Checklist

| Field | Decision / evidence |
|---|---|
| Named owner |  |
| Data classification |  |
| Least privilege |  |
| Tool contracts |  |
| Approval thresholds |  |
| Logging and evidence |  |
| Budget and timeout |  |

Complete every field with evidence or mark it explicitly as unknown. Unknowns become preparation tasks; they should not be converted into confident assumptions.

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |
| Notes 4: |

REUSABLE WORKSHEET

Appendix C - Agent Control Checklist: Recovery

| Field | Decision / evidence |
|---|---|
| Idempotency |  |
| Retry rules |  |
| Loop limit |  |
| Escalation |  |
| Rollback |  |
| Kill switch |  |
| Incident review |  |

Complete every field with evidence or mark it explicitly as unknown. Unknowns become preparation tasks; they should not be converted into confident assumptions.

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |
| Notes 4: |

REUSABLE WORKSHEET

Appendix D - Pilot Evaluation Scorecard

| Field | Decision / evidence |
|---|---|
| Business outcome |  |
| Quality |  |
| Cycle time |  |
| Error rate |  |
| Human override |  |
| Safety incidents |  |
| User adoption |  |

Complete every field with evidence or mark it explicitly as unknown. Unknowns become preparation tasks; they should not be converted into confident assumptions.

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |
| Notes 4: |

REUSABLE WORKSHEET

Appendix E - Implementation Roadmap

| Field | Decision / evidence |
|---|---|
| Discover |  |
| Prioritise |  |
| Prototype |  |
| Pilot |  |
| Scale |  |
| Improve |  |

Complete every field with evidence or mark it explicitly as unknown. Unknowns become preparation tasks; they should not be converted into confident assumptions.

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |
| Notes 4: |

## Appendix F - Quick Reference

| Technology | Best-fit boundary |
|---|---|
| Gemini / Veo | Generative video drafts under brand and claim review |
| n8n | Visual deterministic workflow with AI decisions and human approval |
| Claude Cowork / ChatGPT Work | Evidence-grounded knowledge work across approved files and tools |
| Claude Code / Codex | Repository inspection, editing, tool use and verification |
| OpenClaw / Hermes Agent | Persistent, channel-connected personal or business agent runtime |
| Paperclip | Coordination and oversight of teams of agents |

| Selection rule: Choose the smallest technology boundary that can achieve the outcome with observable evidence and proportionate controls. |
|---|

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |

## Appendix G - Course Support

| LMS: https://lms-tms.tertiaryinfotech.com/ |
|---|

- Courseware and lab instructions are available through the LMS.
- Training provider: Tertiary Infotech Academy Pte Ltd, UEN 201200696W.
- Contact: enquiry@tertiaryinfotech.com · +65 6100 0613 · www.tertiarycourses.com.sg
- Raise access or course questions through the trainer or training administrator.

| Final reflection: What is the smallest governed AI innovation you can test next, what evidence will it produce, and who owns the decision to continue? |
|---|

| Notes 1: |
|---|
| Notes 2: |
| Notes 3: |
| Notes 4: |
