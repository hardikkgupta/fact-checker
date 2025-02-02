# build_index.py

import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
from data import politician_statements

def build_and_save_index(
    statements,
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    index_path="faiss_index.bin",
    statements_path="statements.pkl"
):
    # 1. Initialize embedding model
    model = SentenceTransformer(model_name)

    # 2. Embed each statement
    corpus_texts = [s["text"] for s in statements]
    embeddings = model.encode(corpus_texts, convert_to_numpy=True)

    # 3. Create a FAISS index
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    # 4. Save index to file
    faiss.write_index(index, index_path)

    # 5. Save statements metadata (optional but often useful)
    with open(statements_path, "wb") as f:
        pickle.dump(statements, f)

    print(f"Index built and saved to {index_path}.")
    print(f"Statements saved to {statements_path}.")

if __name__ == "__main__":
    build_and_save_index(politician_statements)
