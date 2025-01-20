from fastapi import FastAPI
import faiss
import numpy as np

# Load FAISS index and metadata
faiss_index = faiss.read_index("faiss_index.bin")
user_product_matrix = np.load("user_product_matrix.npy")

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FAISS Recommendation System is live!"}

@app.get("/recommend/")
def recommend(user_index: int, top_n: int = 5):
    # Ensure user_index is within range
    if user_index < 0 or user_index >= user_product_matrix.shape[0]:
        return {"error": "Invalid user index."}

    # Query FAISS for recommendations
    user_vector = user_product_matrix[user_index:user_index+1]
    faiss.normalize_L2(user_vector)  # Normalize the query vector
    distances, indices = faiss_index.search(user_vector, top_n)

    # Format recommendations
    recommendations = [
        {"product_id": int(idx), "score": float(dist)}
        for idx, dist in zip(indices[0], distances[0])
    ]
    return {"user_index": user_index, "recommendations": recommendations}
