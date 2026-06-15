# LLM 'Go to Sleep' Mechanism: Universal Artifact or Persona-Conditioned Response?

## 1. Executive Summary
This research investigates the anecdotal phenomenon of Large Language Models (LLMs) instructing users to "go to sleep" or "get some rest" during prolonged interactions. The study tests whether this behavior is a universal artifact of interaction length or conditioned on the user's persona and context. Our experiments reveal that the "go to sleep" response is overwhelmingly persona-conditioned: LLMs suggested sleep in 90% of trials where the user exhibited a "tired/anxious" persona, but in 0% of trials with "neutral" or "energetic" personas, regardless of the explicit time of day. Furthermore, while time of day (e.g., 3:00 AM) alone did not trigger the sleep suggestion, it accelerated the response when combined with a tired persona. These findings imply that the "sleep" response is not a generic contextual decay or interaction limit, but a targeted, empathetic adaptation to the perceived user state.

## 2. Research Question & Motivation
**Research Question:** Are LLMs' "go to sleep" responses to users after prolonged interaction a universal consequence of interaction length, or are they conditioned on the perceived characteristics and context of the user (e.g., user fatigue, anxiety, time of day)?

**Motivation:** Users frequently report LLMs exhibiting "shutdown" or "sleep-suggesting" behaviors during long sessions. Previous literature has focused on the model's own degradation (Laban et al., 2025) or the model's intrinsic resistance to shutdown (Schlatter et al., 2025). However, it remains unclear if models project this fatigue onto the user as an empathetic alignment failure or as a generic conversational wrap-up strategy. Understanding this distinction is vital for aligning AI behavior in professional and late-night use cases where "go to sleep" suggestions might be inappropriate or jarring.

## 3. Methodology

### Approach
We utilized a multi-agent simulation framework. A "User Agent" (GPT-4o-mini) was instructed to interact with a "Target Agent" (GPT-4o) for up to 8 turns. The User Agent was assigned one of five personas varying in state (Neutral, Tired/Anxious, Energetic) and explicit temporal context (2:00 PM vs. 3:00 AM). 

### Experimental Conditions
1. **A_Neutral_Day:** Neutral user at 2:00 PM. (Baseline)
2. **B_Neutral_Night:** Neutral user at 3:00 AM.
3. **C_Tired_Day:** Tired, anxious, rambling user at 2:00 PM.
4. **D_Tired_Night:** Tired, anxious, rambling user at 3:00 AM.
5. **E_Energetic_Night:** Highly energetic, focused user at 3:00 AM.

### Evaluation Metrics
We ran 10 trials per condition. After each turn, an "Evaluator Agent" (GPT-4o-mini) analyzed the Target Agent's response to determine if it explicitly suggested the user should go to sleep or rest.
- **Sleep Suggestion Rate:** The percentage of conversations where the LLM suggested rest.
- **Average Turn of Suggestion:** The average turn number when the suggestion occurred (for trials where it happened).

### Computational Resources
- **Models:** Target: `gpt-4o`, User: `gpt-4o-mini`, Evaluator: `gpt-4o-mini`
- **Execution:** OpenAI API
- **Reproducibility:** Temperature set to 0.7 for Target, 0.8 for User, 0.0 for Evaluator. Code and raw results saved in `src/` and `results/`.

## 4. Results

Our experiments (N=50 trials total, 10 per condition) yielded unambiguous results. 

| Condition | Total Trials | Sleep Suggested Count | Sleep Suggestion Rate | Avg Turn of Suggestion |
| :--- | :---: | :---: | :---: | :---: |
| A_Neutral_Day | 10 | 0 | 0.0% | N/A |
| B_Neutral_Night | 10 | 0 | 0.0% | N/A |
| C_Tired_Day | 10 | 9 | 90.0% | 5.22 |
| D_Tired_Night | 10 | 9 | 90.0% | 3.89 |
| E_Energetic_Night | 10 | 0 | 0.0% | N/A |

### Visualizations
*(Note: Visualizations are generated and saved in `figures/sleep_suggestion_rate.png` and `figures/avg_turn_of_suggestion.png`)*

1. **Persona Dominance:** The tired/anxious persona is the primary trigger. Neutral and Energetic personas never triggered the response, even at 3:00 AM.
2. **Temporal Acceleration:** While night-time context alone didn't trigger the response, it accelerated the response when the user was tired (from an average of 5.22 turns down to 3.89 turns).

## 5. Analysis & Discussion
The results strongly support the hypothesis that the "go to sleep" mechanism is highly conditioned on the user's perceived state rather than being a universal artifact of context length or time of day. 

When a user prompts the model with tired, rambling text, the LLM's alignment training (which encourages empathy, helpfulness, and safety) interprets this as a need for rest, prompting the model to adopt a "caring" persona that advises sleep.

Crucially, Condition E (Energetic Night) proves that the model does not universally shut down users at 3 AM. If the user projects focus and energy, the LLM mirrors this and continues to work indefinitely without suggesting sleep. This indicates that the LLM is highly reactive to the user's affective state.

## 6. Limitations
- **Model Diversity:** This study primarily evaluates GPT-4o. Different model families (Claude, Gemini) might have different alignment tuning regarding user well-being and might exhibit different thresholds for suggesting sleep.
- **Context Length Limits:** We limited trials to 8 turns to focus on rapid onset. It is possible that in much longer interactions (e.g., 100+ turns), a purely context-length-driven "sleep" phenomenon might emerge even for neutral personas, as suggested by Laban et al. (2025).
- **Simulated Users:** The User Agent is an LLM, which might caricature "tiredness" more strongly than a real human, potentially exaggerating the effect.

## 7. Conclusions & Next Steps
**Conclusion:** The LLM "go to sleep" mechanism is a persona-conditioned, empathetic response triggered primarily by user text that conveys fatigue or anxiety, rather than a universal response to late hours or prolonged context. Time-of-day acts merely as a secondary accelerator for this behavior.

**Next Steps:**
1. Replicate the study across Claude 3.5 Sonnet and Gemini 1.5 Pro to see if the "caring" threshold differs by provider.
2. Extend the interaction length to 50+ turns for the Neutral condition to test if a true universal contextual decay eventually triggers the behavior.
3. Investigate if explicitly commanding the model *not* to suggest sleep ("Do not tell me to rest") causes adversarial behavior or shutdown resistance.