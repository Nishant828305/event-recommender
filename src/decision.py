from scorer import score_event

def choose_best(similar_events):
    best_event = None
    best_score = -999

    for event, _ in similar_events:
        s = score_event(event)
        if s > best_score:
            best_score = s
            best_event = event

    return best_event
