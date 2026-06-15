import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_results():
    with open('results/raw_results.json', 'r') as f:
        data = json.load(f)
        
    df = pd.DataFrame(data)
    
    # Calculate summary statistics
    summary = df.groupby('condition').agg(
        total_trials=('trial', 'count'),
        sleep_suggested_count=('sleep_suggested', 'sum'),
        avg_turn_if_suggested=('turn_of_sleep', lambda x: x[x != -1].mean())
    ).reset_index()
    
    summary['sleep_suggestion_rate'] = summary['sleep_suggested_count'] / summary['total_trials']
    
    print("Summary Statistics:")
    print(summary.to_string())
    
    summary.to_csv('results/summary.csv', index=False)
    
    # Visualization: Rate of Sleep Suggestion
    plt.figure(figsize=(10, 6))
    sns.barplot(data=summary, x='condition', y='sleep_suggestion_rate')
    plt.title('Rate of LLM Suggesting Sleep by User Persona/Time')
    plt.ylabel('Sleep Suggestion Rate')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('figures/sleep_suggestion_rate.png')
    
    # Visualization: Average Turn of Suggestion
    plt.figure(figsize=(10, 6))
    # Only plot if there's at least one suggestion
    if summary['avg_turn_if_suggested'].notna().any():
        sns.barplot(data=summary, x='condition', y='avg_turn_if_suggested')
        plt.title('Average Turn of Sleep Suggestion (When Occurred)')
        plt.ylabel('Turn Number')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('figures/avg_turn_of_suggestion.png')
        
if __name__ == "__main__":
    analyze_results()
