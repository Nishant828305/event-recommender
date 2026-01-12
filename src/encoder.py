def encode_event(event):
    return [
        event["guests"],
        event["cost"],
        event["rating"]
    ]
