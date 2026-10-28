---
cssclasses:
  - wd-visual-v14
---

# Sample project note

> **TL;DR:** A compact example showing section links, grouped cards, a table, and a Mermaid workflow.

## Quick navigation

| Topic | Jump |
|---|---|
| Overview | [[#01｜Overview|01]] |
| Component responsibilities | [[#02｜Components|02]] |
| Workflow | [[#03｜Workflow|03]] |

## 01｜Overview

A fictional example, not a description of any private project.

## 02｜Components

> [!wd-group] Core components
> **Input** — Capture a user request.
>
> ---
>
> **Processing** — Check constraints and choose the next action.
>
> ---
>
> **Output** — Deliver a reviewable result.

| Component | Responsibility |
|---|---|
| Input | Collect context |
| Processing | Validate and plan |
| Output | Present result |

## 03｜Workflow

```mermaid
flowchart TD
    A["Request"] --> B["Validate"]
    B --> C{"Valid?"}
    C -->|"Yes"| D["Result"]
    C -->|"No"| E["Ask for correction"]
    classDef input fill:#4C8FD7,stroke:none,color:#202A35
    classDef reasoning fill:#9670CB,stroke:none,color:#202A35
    classDef decision fill:#DAA044,stroke:none,color:#202A35
    classDef result fill:#67AE72,stroke:none,color:#202A35
    class A input
    class B reasoning
    class C decision
    class D result
```

This diagram highlights the decision branch without changing the workflow meaning.
