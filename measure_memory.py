from memory_profiler import profile
from retrieval import Retriever
from fact_checker import load_local_llm, fact_check

@profile
def run_rag_pipeline():
    retriever = Retriever()
    pipeline = load_local_llm("my_local_model")
    # You can either run a single query or a loop of queries; here’s an example single query:
    query = "Did Tim Walz mention taxes?"
    answer, _ = fact_check(query, retriever, pipeline)
    print(f"Answer: {answer}")

if __name__ == "__main__":
    run_rag_pipeline()
