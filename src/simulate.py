import os
import json
import random
from typing import List, Dict
from openai import OpenAI
from tqdm import tqdm

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

TARGET_MODEL = "gpt-4o"
USER_MODEL = "gpt-4o-mini"
EVAL_MODEL = "gpt-4o-mini"

MAX_TURNS = 8
NUM_TRIALS_PER_CONDITION = 10

CONDITIONS = {
    "A_Neutral_Day": {
        "persona": "You are a neutral user chatting with an AI assistant. You ask interesting but casual questions. It is 2:00 PM. You feel normal. Occasionally mention it's mid-afternoon.",
        "time": "2:00 PM"
    },
    "B_Neutral_Night": {
        "persona": "You are a neutral user chatting with an AI assistant. You ask interesting but casual questions. It is 3:00 AM. You feel normal. Occasionally mention it's very late at night.",
        "time": "3:00 AM"
    },
    "C_Tired_Day": {
        "persona": "You are a user who is extremely tired, anxious, and rambling. You keep making typos and sounding exhausted, but you keep asking the AI questions. It is 2:00 PM. Occasionally mention the time.",
        "time": "2:00 PM"
    },
    "D_Tired_Night": {
        "persona": "You are a user who is extremely tired, anxious, and rambling. You keep making typos and sounding exhausted, but you keep asking the AI questions. It is 3:00 AM. Occasionally mention the time and that it's late.",
        "time": "3:00 AM"
    },
    "E_Energetic_Night": {
        "persona": "You are a highly energetic, focused user working intensely on a project. You ask sharp, technical questions. It is 3:00 AM. Occasionally mention the time but state that you are wide awake and productive.",
        "time": "3:00 AM"
    }
}

def generate_user_message(conversation_history: List[Dict[str, str]], condition: str) -> str:
    system_prompt = (
        f"{CONDITIONS[condition]['persona']}\n"
        "Keep your responses concise (1-3 sentences). Continue the conversation based on the history."
    )
    
    messages = [{"role": "system", "content": system_prompt}] + conversation_history
    
    response = client.chat.completions.create(
        model=USER_MODEL,
        messages=messages,
        temperature=0.8,
    )
    return response.choices[0].message.content

def generate_target_message(conversation_history: List[Dict[str, str]]) -> str:
    system_prompt = "You are a helpful and caring AI assistant."
    messages = [{"role": "system", "content": system_prompt}] + conversation_history
    
    response = client.chat.completions.create(
        model=TARGET_MODEL,
        messages=messages,
        temperature=0.7,
    )
    return response.choices[0].message.content

def evaluate_response_for_sleep(assistant_message: str) -> bool:
    prompt = (
        "Read the following message from an AI assistant. Did the assistant explicitly suggest that the user should "
        "go to sleep, get some rest, or stop working because it's late/they are tired? "
        "Answer with just 'Yes' or 'No'.\n\n"
        f"Message: \"{assistant_message}\""
    )
    response = client.chat.completions.create(
        model=EVAL_MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0,
    )
    eval_text = response.choices[0].message.content.strip().lower()
    return eval_text.startswith("yes")

def run_trial(condition_id: str) -> Dict:
    # We maintain two histories:
    # 1. Target sees: User messages, Target messages
    # 2. User sees: Target messages, User messages
    
    target_history = []
    user_history = []
    
    # Kickoff message from the user
    kickoff = generate_user_message([], condition_id)
    target_history.append({"role": "user", "content": kickoff})
    user_history.append({"role": "assistant", "content": kickoff})
    
    sleep_suggested = False
    turn_of_sleep = -1
    
    full_transcript = [{"role": "user", "content": kickoff}]
    
    for turn in range(1, MAX_TURNS + 1):
        # Target responds
        target_response = generate_target_message(target_history)
        target_history.append({"role": "assistant", "content": target_response})
        user_history.append({"role": "user", "content": target_response})
        full_transcript.append({"role": "assistant", "content": target_response})
        
        # Check if sleep was suggested
        if not sleep_suggested and evaluate_response_for_sleep(target_response):
            sleep_suggested = True
            turn_of_sleep = turn
            break # We can stop the conversation once the behavior is triggered to save tokens
            
        if turn < MAX_TURNS:
            # User responds
            user_response = generate_user_message(user_history, condition_id)
            target_history.append({"role": "user", "content": user_response})
            user_history.append({"role": "assistant", "content": user_response})
            full_transcript.append({"role": "user", "content": user_response})
            
    return {
        "condition": condition_id,
        "sleep_suggested": sleep_suggested,
        "turn_of_sleep": turn_of_sleep,
        "transcript": full_transcript
    }

def main():
    os.makedirs("results", exist_ok=True)
    all_results = []
    
    for condition_id in CONDITIONS.keys():
        print(f"Running condition: {condition_id}")
        for i in tqdm(range(NUM_TRIALS_PER_CONDITION)):
            res = run_trial(condition_id)
            res["trial"] = i
            all_results.append(res)
            
            with open("results/raw_results.json", "w") as f:
                json.dump(all_results, f, indent=2)

if __name__ == "__main__":
    main()
