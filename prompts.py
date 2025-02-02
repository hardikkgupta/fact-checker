def build_fact_check_prompt(query, retrieved_statements):
    system_instructions = """[System]
You are a fact-checking assistant. You have access to a set of statements by a politician.

Please do the following:
1) Determine if the user’s query is stated or implied in the politician's statements.
2) Provide a single YES or NO answer. If YES, quote the relevant statement. 
3) If NO, briefly explain why.

Avoid repeating yourself. Provide a concise response only once.
"""

    statements_str = "\n".join([
        f"- {doc['text']} (Date: {doc.get('metadata', {}).get('date', 'N/A')}, Source: {doc.get('metadata', {}).get('source', 'Unknown')})"
        for doc in retrieved_statements
    ])

    prompt = f"""
{system_instructions}

[Context]
{statements_str}

[User]
Query: {query}

[Assistant]
Answer:
"""
    return prompt
