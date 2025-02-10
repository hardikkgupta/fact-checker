import time
import statistics
from retrieval import Retriever
from fact_checker import load_local_llm, fact_check

# Initialize retriever and model pipeline once
retriever = Retriever()
pipeline = load_local_llm("my_local_model")

# Define a list of test queries (use real or synthetic queries)
queries = [
    "Did Tim Walz sign a new education bill?",
    "What did Tim Walz say about healthcare?",
    "Did Tim Walz mention taxes?",
    "When was Tim Walz born?",
    "What initiatives did Tim Walz announce recently?"
]

# List to store individual query latencies
latencies = []

print("Running latency and throughput measurements...\n")
for query in queries:
    start = time.perf_counter()
    
    # Execute the entire RAG workflow: embedding, retrieval, prompt building, LLM generation
    answer, _ = fact_check(query, retriever, pipeline)
    
    end = time.perf_counter()
    latency = end - start
    latencies.append(latency)
    
    print(f"Query: {query}")
    print(f"Answer: {answer}")
    print(f"Latency: {latency:.3f} seconds\n")

# Calculate overall statistics
avg_latency = statistics.mean(latencies)
# For p95 latency, sort and take the value at the 95th percentile
sorted_latencies = sorted(latencies)
p95_index = int(0.95 * len(sorted_latencies)) - 1
p95_latency = sorted_latencies[p95_index] if sorted_latencies else 0
total_time = sum(latencies)
qps = len(queries) / total_time

print("Overall Metrics:")
print(f"Average latency: {avg_latency:.3f} seconds")
print(f"95th percentile latency: {p95_latency:.3f} seconds")
print(f"Throughput: {qps:.2f} queries per second")
