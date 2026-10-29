import torch

from transformers import AutoTokenizer
from transformers import AutoModelForCausalLM


#Pretrained model name
model_name = "distilgpt2"


#Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)

#Load pretrained language model
model = AutoModelForCausalLM.from_pretrained(model_name)


#Input sentence
sentence = "I Love AI"

#Convert text into PyTorch tensors
inputs = tokenizer(sentence,return_tensors = "pt")                  #pt-pytorch

#Extract token ids
token_ids = inputs["input_ids"]


#access the pretrained input embeddding layer
embedding_layer = model.get_input_embeddings()

#retrieved the embedding vectors
embeddings = embedding_layer(token_ids)

print("Input sentence : ",sentence)

print("Token ids : ")
print(token_ids)

print("Embedding shape:")
print(embeddings.shape)

print("first token embedding : ")
print(embeddings[0,0, :10])