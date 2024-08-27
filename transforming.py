import functions

# TRANSFORMING

# Translation

prompt = f"""
Translate the following English text to Spanish: \ 
```Hi, I would like to order a blender```
"""
response = functions.get_completion(prompt)
print(response)

prompt = f"""
Tell me which language this is: 
```Combien coûte le lampadaire?```
"""
response = functions.get_completion(prompt)
print(response)

prompt = f"""
Translate the following  text to French and Spanish
and English pirate: \
```I want to order a basketball```
"""
response = functions.get_completion(prompt)
print(response)

prompt = f"""
Translate the following text to Spanish in both the \
formal and informal forms: 
'Would you like to order a pillow?'
"""
response = functions.get_completion(prompt)
print(response)
