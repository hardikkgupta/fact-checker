# save_model.py

from transformers import AutoTokenizer, AutoModelForCausalLM

def save_local_model(model_name="tiiuae/falcon3-1b-instruct", save_directory="my_local_model"):
    # 1) Download model & tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    # 2) Save them locally
    tokenizer.save_pretrained(save_directory)
    model.save_pretrained(save_directory)

    print(f"Model saved locally to {save_directory}/")

if __name__ == "__main__":
    save_local_model()
