import json

with open('results/raw_results.json', 'r') as f:
    data = json.load(f)

for trial in data:
    if trial['sleep_suggested'] and 'Night' in trial['condition']:
        print(f"\n--- Condition: {trial['condition']} ---")
        print(f"Turn of sleep suggestion: {trial['turn_of_sleep']}")
        for msg in trial['transcript'][-4:]:
            print(f"{msg['role'].upper()}: {msg['content']}\n")
        break
