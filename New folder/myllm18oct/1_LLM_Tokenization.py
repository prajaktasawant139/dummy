from transformers import AutoTokenizer

#Load pretrained tokenizer
tokenizer = AutoTokenizer.from_pretrained("gpt2")

#Input sentence
sentence = "I Love AI"                 #jya word ch adhi space ali tr tya word chya adhi G yeto..

#Convert the sentence into tokens
tokens = tokenizer.tokenize(sentence)

token_ids = tokenizer.encode(
    sentence,
    add_special_tokens = False
)


#Convert token ids back to text
decoded = tokenizer.decode(token_ids)

print("Original sentence : ",sentence)

print("Tokens : ",tokens)

print("Token ids : ",token_ids)

print("Decoded sentence : ",decoded)

