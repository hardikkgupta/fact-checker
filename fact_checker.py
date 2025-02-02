# fact_checker.py

from retrieval import Retriever
from prompts import build_fact_check_prompt
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

def load_local_llm(local_path="my_local_model"):
    """
    Loads the tokenizer and model from a local directory (my_local_model).
    Returns a text-generation pipeline.
    """
    tokenizer = AutoTokenizer.from_pretrained(local_path)
    model = AutoModelForCausalLM.from_pretrained(local_path)
    generation_pipeline = pipeline("text-generation", model=model, tokenizer=tokenizer)
    return generation_pipeline

def fact_check(query, retriever, generation_pipeline):
    """
    1. Retrieve top statements from the FAISS index.
    2. Build a prompt.
    3. Generate a response using the local LLM.
    """
    # Get relevant statements for the query
    top_k_statements = retriever.get_top_k_statements(query)
    
    # Build the prompt
    prompt = build_fact_check_prompt(query, top_k_statements)

    # Generate text with specific hyperparameters to reduce repetition
    output = generation_pipeline(
        prompt,
        max_new_tokens=80,
        temperature=0.3,
        top_p=0.9,
        repetition_penalty=1.4
    )
    
    # Extract the generated text
    generated_text = output[0]["generated_text"]
    return generated_text, top_k_statements

if __name__ == "__main__":
    # 1) Load the FAISS index and statements (once)
    retriever = Retriever()  # ensure faiss_index.bin and statements.pkl exist

    # 2) Load the local model from disk (once)
    text_pipeline = load_local_llm("my_local_model")

    # 3) Keep accepting user queries in a loop
    print("Welcome to the Fact Checker! Type 'exit' or 'quit' to stop.\n")
    while True:
        user_query = input("Enter your question: ")
        if user_query.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        answer, evidence = fact_check(user_query, retriever, text_pipeline)
        print("\n==== ANSWER ====")
        print(answer)
        print("\n")
