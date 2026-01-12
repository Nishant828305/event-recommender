from sklearn.metrics.pairwise import cosine_similarity
from encoder import encode_event

def find_similar_events(new_event, past_events):
    new_vec = [encode_event(new_event)]
    past_vecs = [encode_event(e) for e in past_events]

    scores = cosine_similarity(new_vec, past_vecs)[0]
    return list(zip(past_events, scores))
  