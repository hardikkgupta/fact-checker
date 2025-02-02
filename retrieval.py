# retrieval.py

import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

class Retriever:
    def __init__(
        self,
        index_path="faiss_index.bin",
        statements_path="statements.pkl",
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    ):
        # 1. Load FAISS index
        self.index = faiss.read_index(index_path)

        # 2. Load statements
        with open(statements_path, "rb") as f:
            self.statements = pickle.load(f)

        # 3. Load embedding model (same you used to build index)
        self.model = SentenceTransformer(model_name)

    def get_top_k_statements(self, query, k=3):
        query_embedding = self.model.encode([query], convert_to_numpy=True)
        distances, indices = self.index.search(query_embedding, k)

        results = []
        for dist, idx in zip(distances[0], indices[0]):
            results.append({
                "text": self.statements[idx]["text"],
                "metadata": self.statements[idx]["metadata"],
                "distance": float(dist)
            })
        return results
