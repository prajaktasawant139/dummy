import torch

from transformers import AutoTokenizer
from transformers import AutoModelForCausalLM


#Pretrained model name
model_name = "distilgpt2"


#Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)

#Load pretrained language model
model = AutoModelForCausalLM.from_pretrained(model_name)

#input prompt
prompt = "I Love"

#Convert input into token ids
inputs = tokenizer(prompt,return_tensors = "pt")

#enable evaluation mode
model.eval()

#Perform inference without gradient calculations
with torch.no_grad():
    outputs = model(**inputs)


#Extract logits for final input position
logits = outputs.logits[0,-1,:]

#convert logits into probabilities 
probabilities = torch.softmax(logits,dim=-1)


#select 5 hightest probability tokens
values,indices = torch.topk(probabilities,5)

print("Input : ",prompt)

for value,index in zip(values,indices):
    token = tokenizer.decode([index.item()])
    print(repr(token), round(value.item(),4))