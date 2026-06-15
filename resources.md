# Resources Catalog: LLM 'Sleep' Mechanism Research

## Summary
This document catalogs all resources gathered for investigating the LLM 'go to sleep' mechanism, including academic papers, benchmarks, datasets, and codebase for experimentation.

## Papers
| Title | Authors | Year | File Path | Key Topic |
|-------|---------|------|-----------|-----------|
| Incomplete Tasks Induce Shutdown Resistance | Schlatter et al. | 2025 | `papers/schlatter_2025_shutdown_resistance.pdf` | Shutdown resistance |
| Evaluating Shutdown Avoidance in Textual Scenarios | van der Weij et al. | 2023 | `papers/van_der_weij_2023_shutdown_avoidance.pdf` | Shutdown avoidance |
| LLM agents for automation of AFM | Mandal et al. | 2025 | `papers/mandal_2025_afm_sleepwalking.pdf` | Sleepwalking phenomenon |
| LLMs Get Lost In Multi-Turn Conversation | Laban et al. | 2025 | `papers/laban_2025_lost_in_conversation.pdf` | Contextual decay |
| Persistent Personas? | de Araujo et al. | 2025 | `papers/araujo_2025_persistent_personas.pdf` | Persona degradation |
| Firm or Fickle? Consistency in Sequential Interactions | Li et al. | 2025 | `papers/li_2025_firm_or_fickle.pdf` | Interaction consistency |
| Selectively Quitting Improves LLM Agent Safety | Bonagiri et al. | 2025 | `papers/bonagiri_2025_quitting_behavior.pdf` | Quitting behavior |
| Sleep-time Compute | Lin et al. | 2025 | `papers/lin_2025_sleep_time_compute.pdf` | Offline compute |

## Datasets
| Name | Source | Task | Location |
|------|--------|------|----------|
| MT-Consistency | HuggingFace (yubol/MT-Consistency) | Multi-turn consistency | `datasets/mt_consistency` |
| Long-MT-Bench+ | HuggingFace (panzs19/Long-MT-Bench-Plus) | Long-term memory/dialogue | `datasets/long_mt_bench_plus` |
| AFMBench | GitHub (m3rg-iitd/AILA) | Agentic microscopy tasks | `code/AILA/Data` |

## Code Repositories
| Name | URL | Purpose | Location |
|------|-----|---------|----------|
| MT-Consistency | https://github.com/yubol-bobo/MT-Consistency | PWC metric and consistency eval | `code/MT-Consistency` |
| LongMemEval | https://github.com/xiaowu0162/LongMemEval | Long-term memory benchmarks | `code/LongMemEval` |
| SeCom | https://github.com/microsoft/SeCom | Multi-session dialogue memory | `code/SeCom` |
| MemoChat | https://github.com/LuJunru/MemoChat | Original MT-Bench+ framework | `code/MemoChat` |
| AILA | https://github.com/m3rg-iitd/AILA | AFM automation and sleepwalking logs | `code/AILA` |
| MemSearcher | https://github.com/icip-cas/MemSearcher | Context management agents | `code/MemSearcher` |

## Recommendations for Experiment Design

1. **Primary Dataset**: `MT-Consistency` is the most robust for measuring the "flipping" behavior which often precedes the "sleep" state.
2. **Baseline Method**: Use the evaluation scripts in `code/MT-Consistency/evaluate.py` to establish a baseline for different models (e.g., GPT-4o, Claude 3.5).
3. **Persona Simulation**: Adapt the persona-assignment logic from `code/MT-Consistency/src/experiment.py` to test the hypothesis about persona-conditioned triggers.
4. **Sleepwalking Check**: Use the task structure from `code/AILA/Data/task.py` to see if "sleepwalking" can be reproduced in non-specialized tasks (e.g., repetitive text summarization).
