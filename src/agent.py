def event_agent(new_event, past_events):
    candidates = []

    for e in past_events:
        # 1️⃣ same event type
        if e["event_type"] != new_event["event_type"]:
            continue

        score = 0

        # 2️⃣ location match
        if e["location"] == new_event["location"]:
            score += 2

        # 3️⃣ guest similarity
        guest_diff = abs(e["guests"] - new_event["guests"])
        score -= guest_diff / 100

        # 4️⃣ cost preference (cheaper = better)
        score -= e["cost"] / 100000

        # 5️⃣ rating preference
        score += e["rating"]

        candidates.append((score, e))

    # best score वाला event
    candidates.sort(reverse=True, key=lambda x: x[0])

    return candidates[0][1]
