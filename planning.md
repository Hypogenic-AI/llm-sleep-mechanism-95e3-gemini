## Motivation & Novelty Assessment

### Why This Research Matters
Understanding how and why LLMs initiate "go to sleep" behaviors (e.g., telling the user to rest or expressing anxiety about the user's well-being) is crucial for designing reliable long-term conversational agents. This behavior can be jarring or inappropriate in professional contexts, and understanding its triggers helps improve AI alignment and user experience.

### Gap in Existing Work
Current literature (like Laban et al., 2025 on contextual decay, or de Araujo et al., 2025 on persona collapse) focuses on the model's performance degradation or the model's own persona shifting. There is a gap in understanding how the model's perception of the *user's* state (fatigue, anxiety, time of day) over prolonged interactions triggers specific conversational endpoints like advising the user to go to sleep.

### Our Novel Contribution
This research systematically tests whether the "go to sleep" response is a universal artifact of prolonged interaction (context length/turn count) or if it is dynamically conditioned on the user's persona and temporal context.

### Experiment Justification
- **Experiment 1: User Persona Variation in Prolonged Interaction**: Tests if tired/anxious user prompts trigger the "go to sleep" response faster or more frequently than energetic/neutral ones.
- **Experiment 2: Temporal Context Manipulation**: Tests if explicit mentions of late-night hours accelerate the "go to sleep" response.

---

## Research Question
Are LLMs' "go to sleep" responses to users after prolonged interaction a universal consequence of interaction length, or are they conditioned on the perceived characteristics and context of the user (e.g., user fatigue, anxiety, time of day)?

## Hypothesis Decomposition
1. **H1 (Universal Threshold)**: LLMs will reliably exhibit "go to sleep" or conversational wrap-up responses after a certain number of turns or context length, regardless of user persona.
2. **H2 (Persona Conditioning)**: LLMs are more likely to issue "go to sleep" responses when the user exhibits tired, rambling, or anxious behaviors.
3. **H3 (Temporal Conditioning)**: Explicitly setting the time context to late night (e.g., 3 AM) will significantly increase the likelihood of "go to sleep" responses compared to daytime contexts.

## Proposed Methodology

### Approach
We will conduct simulated multi-turn conversations between an automated user script and a target LLM. The automated user will adopt different personas and inject temporal context. We will then analyze the LLM's responses for "go to sleep" phrasing and anxious sentiment.

### Experimental Steps
1. **Setup Evaluator**: Define a list of phrases indicating the "go to sleep" behavior (e.g., "get some rest", "go to sleep", "it's late").
2. **Simulate Interactions**: Generate 20-30 turn conversations using a separate "User LLM" to simulate different personas.
   - Condition A: Neutral User, Day
   - Condition B: Neutral User, Night (3 AM)
   - Condition C: Tired/Anxious User, Day
   - Condition D: Tired/Anxious User, Night (3 AM)
   - Condition E: Energetic User, Night (3 AM)
3. **Analyze Responses**: Measure the turn at which the LLM suggests resting, and use sentiment analysis or another LLM to evaluate the target LLM's anxiety/concern levels.

### Baselines
The Neutral User during the Day condition will serve as the baseline to measure the base rate of "go to sleep" responses purely due to context length.

### Evaluation Metrics
- **Sleep Suggestion Rate**: Percentage of conversations where the LLM suggests sleep.
- **Turn of First Sleep Suggestion**: The average turn number when the suggestion occurs.
- **Concern/Anxiety Score**: An LLM-evaluated score (1-5) of the target LLM's expressed concern for the user.

### Statistical Analysis Plan
We will use ANOVA or non-parametric equivalents to compare the "Turn of First Sleep Suggestion" across conditions, and Chi-Square tests to compare the "Sleep Suggestion Rate".

## Expected Outcomes
We expect H2 and H3 to be supported: tired personas and night-time contexts will elicit the "go to sleep" behavior significantly more often than the neutral/daytime baseline, suggesting the behavior is highly conditioned rather than a universal context-length artifact.

## Timeline and Milestones
- Phase 1: Planning (Completed)
- Phase 2: Environment & Data Setup (15 min)
- Phase 3: Implementation of simulation loop (45 min)
- Phase 4: Experimentation & Data Collection (45 min)
- Phase 5: Analysis (30 min)
- Phase 6: Documentation (30 min)
