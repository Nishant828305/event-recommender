def score_event(event):
    return (event["rating"] * 0.7) - (event["cost"] / 100000)
