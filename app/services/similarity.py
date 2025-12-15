from sentence_transformers import SentenceTransformer, util

# Load model once at startup
model = SentenceTransformer("all-MiniLM-L6-v2")

def compute_similarity(text1: str, text2: str, threshold: float = 0.7) -> dict:
    if not text1.strip() or not text2.strip():
        return {"error": "Both texts must be non-empty"}

    emb1 = model.encode(text1, convert_to_tensor=True)
    emb2 = model.encode(text2, convert_to_tensor=True)
    score = util.pytorch_cos_sim(emb1, emb2).item()
    
    result = {
        "similarity": score,
        "is_similar": score >= threshold
    }
    return result

