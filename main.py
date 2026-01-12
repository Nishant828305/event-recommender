from data import past_events
from agent import event_agent

new_event = {
    "event_type": "wedding",
    "location": "Dhanbad",
    "guests": 120
}

best_event = event_agent(new_event, past_events)

print("\n🎯 BEST EVENT RECOMMENDATION\n")
for k, v in best_event.items():
    print(f"{k}: {v}")
