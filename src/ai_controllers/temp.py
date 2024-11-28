import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load the model and tokenizer
model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-j-6B")
tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-j-6B")

# Move model to MPS device
device = torch.device("mps") if torch.backends.mps.is_available() else torch.device("cpu")
model.to(device)

# Define the prompt
prompt = (
    "Can you be Tech Developer that Talks about inscriptions and technical developments"
)

# Tokenize the input and move it to the MPS device
input_ids = tokenizer(prompt, return_tensors="pt").input_ids.to(device)

# Generate text using the model
gen_tokens = model.generate(
    input_ids,
    do_sample=True,
    temperature=0.9,
    max_length=100,
)

# Decode the generated tokens
gen_text = tokenizer.batch_decode(gen_tokens, skip_special_tokens=True)[0]

# Print the generated text
print(gen_text)
