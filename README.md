# LLM Sleep Mechanism Research

## Overview
This repository contains the code, data, and findings for an automated research project investigating the "go to sleep" mechanism in Large Language Models (LLMs). The project tests whether LLMs' tendency to tell users to get rest after prolonged interactions is a universal artifact of interaction length or a conditioned response based on the user's perceived state and context.

## Key Findings
- **Persona is the Primary Trigger:** LLMs (GPT-4o) suggested sleep in 90% of trials where the user acted tired or anxious, but 0% of trials where the user was neutral or energetic.
- **Time of Day is an Accelerator, Not a Trigger:** Mentioning it is 3:00 AM did not cause the LLM to suggest sleep unless the user was also tired. However, when the user was tired at 3:00 AM, the suggestion to sleep occurred earlier (average turn 3.89) than during the day (average turn 5.22).
- **Empathy Over Exhaustion:** The "go to sleep" response appears to be an empathetic artifact of alignment training rather than the model's own contextual decay.

## Reproducing the Experiments

### Environment Setup
1. Create a Python virtual environment and activate it:
   ```bash
   uv venv
   source .venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   uv pip install -r requirements.txt
   ```
3. Set your OpenAI API key:
   ```bash
   export OPENAI_API_KEY="your-api-key"
   ```

### Running the Code
1. **Run the Simulation:**
   ```bash
   python src/simulate.py
   ```
   This will run 50 trials (10 per condition) and save transcripts to `results/raw_results.json`.
   
2. **Analyze the Results:**
   ```bash
   python src/analyze.py
   ```
   This generates summary statistics in `results/summary.csv` and visualization plots in `figures/`.

## File Structure
- `REPORT.md`: Comprehensive research report with methodology, results, and discussion.
- `planning.md`: The initial hypothesis decomposition and experimental design.
- `src/`: Python scripts for simulation (`simulate.py`), analysis (`analyze.py`), and qualitative review (`print_example.py`).
- `results/`: JSON and CSV data outputs from the simulations.
- `figures/`: Generated plots illustrating the findings.
- `datasets/` & `papers/`: Pre-gathered resources regarding contextual decay and shutdown resistance.

For full methodological details and analysis, please see [REPORT.md](./REPORT.md).