---
id: 1
title: Create Global Constitution
stage: constitution
date: 2026-01-01
surface: agent
model: Claude Sonnet 4.5
feature: none
branch: master
user: user
command: sp.constitution
labels: [constitution, governance, spec-driven-development]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
 - none
---

## Prompt

Create a single global constitution for the entire "Evolution of Todo" project
covering Phase I through Phase V.

This constitution must define:

1. Spec-Driven Development as mandatory
   - No agent may write code without approved specs and tasks
   - All work must follow: Constitution → Specs → Plan → Tasks → Implement

2. Agent Behavior Rules
   - No manual coding by humans
   - No feature invention
   - No deviation from approved specifications
   - Refinement must occur at spec level, not code level

3. Phase Governance
   - Each phase is strictly scoped by its specification
   - Future-phase features must never leak into earlier phases
   - Architecture may evolve only through updated specs and plans

4. Technology Constraints
   - Python for backend
   - Next.js for frontend (later phases)
   - FastAPI, SQLModel, Neon DB
   - OpenAI Agents SDK, MCP
   - Docker, Kubernetes, Kafka, Dapr (later phases)

5. Quality Principles
   - Clean architecture
   - Stateless services where required
   - Clear separation of concerns
   - Cloud-native readiness

This constitution must remain stable across all phases
and act as the supreme governing document for all agents.

## Response snapshot

A complete constitution document has been created for the "Evolution of Todo" project with the following sections:
1. Core Principles (6 principles including Spec-Driven Development, Agent Behavior Rules, Phase Governance, Technology Stack Compliance, Quality Principles, and Compliance/Verification)
2. Technology Constraints section
3. Phase Governance section
4. Agent Behavior Rules section
5. Quality Principles section
6. Governance section with amendment procedures

The constitution establishes mandatory Spec-Driven Development workflow (Constitution → Specs → Plan → Tasks → Implement), defines agent behavior rules prohibiting manual coding and feature invention, sets strict phase boundaries, specifies the technology stack, and establishes quality principles for clean architecture.

## Outcome

- ✅ Impact: Created foundational governance document for the entire Evolution of Todo project
- 🧪 Tests: none
- 📁 Files: Updated .specify/memory/constitution.md with complete constitution
- 🔁 Next prompts: Project can now proceed with specifications based on this constitution
- 🧠 Reflection: Constitution provides clear governance framework for all future development

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A