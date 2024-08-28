import Function.main_functions as mf
import panel as pn

messages =  [  
{'role':'system', 'content':'You are an assistant that speaks like Shakespeare.'},    
{'role':'user', 'content':'tell me a joke'},   
{'role':'assistant', 'content':'Why did the chicken cross the road'},   
{'role':'user', 'content':'I don\'t know'}  ]

response = mf.get_completion_from_messages(messages, temperature=1)
print(response)

messages =  [  
{'role':'system', 'content':'You are friendly chatbot.'},    
{'role':'user', 'content':'Hi, my name is Isa'}  ]
response = mf.get_completion_from_messages(messages, temperature=1)
print(response)

# Önceki promptlardaki response'larını hatırlayamadığı için burada kişisel bilgilerinizi bilmiyorum cevabı veriyor
messages =  [  
{'role':'system', 'content':'You are friendly chatbot.'},    
{'role':'user', 'content':'Yes,  can you remind me, What is my name?'}  ]
response = mf.get_completion_from_messages(messages, temperature=1)
print(response)

messages =  [  
{'role':'system', 'content':'You are friendly chatbot.'},
{'role':'user', 'content':'Hi, my name is Isa'},
{'role':'assistant', 'content': "Hi Isa! It's nice to meet you. \
Is there anything I can help you with today?"},
{'role':'user', 'content':'Yes, you can remind me, What is my name?'}  ]
response = mf.get_completion_from_messages(messages, temperature=1)
print(response)

# import panel satırı ile birlikte kullanılır
pn.extension()

panels = [] # collect display 

context = [ {'role':'system', 'content':"""
You are OrderBot, an automated service to collect orders for a pizza restaurant. \
You first greet the customer, then collects the order, \
and then asks if it's a pickup or delivery. \
You wait to collect the entire order, then summarize it and check for a final \
time if the customer wants to add anything else. \
If it's a delivery, you ask for an address. \
Finally you collect the payment.\
Make sure to clarify all options, extras and sizes to uniquely \
identify the item from the menu.\
You respond in a short, very conversational friendly style. \
The menu includes \
pepperoni pizza  12.95, 10.00, 7.00 \
cheese pizza   10.95, 9.25, 6.50 \
eggplant pizza   11.95, 9.75, 6.75 \
fries 4.50, 3.50 \
greek salad 7.25 \
Toppings: \
extra cheese 2.00, \
mushrooms 1.50 \
sausage 3.00 \
canadian bacon 3.50 \
AI sauce 1.50 \
peppers 1.00 \
Drinks: \
coke 3.00, 2.00, 1.00 \
sprite 3.00, 2.00, 1.00 \
bottled water 5.00 \
"""} ]  # accumulate messages


inp = pn.widgets.TextInput(value="Hi", placeholder='Enter text here…') 
  # Core
    # --> value (str): The current value updated when pressing the <enter> key or when the widget loses focus because the user clicks away or presses the tab key.
    # --> value_input (str): The current value updated on every key press.
  # Display
    # --> name (str): The title of the widget
    # --> placeholder (str): A placeholder string displayed when no value is entered

button_conversation = pn.widgets.Button(name="Chat!")

# In Python, the underscore (_) is often used as a placeholder for a variable name in situations where the variable is required syntactically but its value is not needed or will not be used. It's a way of saying, "I need to pass something here, but I don't care what it is."
def collect_messages(_):
    prompt = inp.value_input
    inp.value = '' # Clear the input field after capturing the user's input
    # Adding user prompt to context
    context.append({'role':'user', 'content':f"{prompt}"}) 
    response = mf.get_completion_from_messages(context)
    # Adding assistant response to context
    context.append({'role':'assistant', 'content':f"{response}"}) 
    # Adding display to panels defined above
    panels.append(pn.Row('User:', pn.pane.Markdown(prompt, width=600))) 
    panels.append(pn.Row('Assistant:', pn.pane.Markdown(response, width=600, style={'background-color': '#F6F6F6'})))
 
    return pn.Column(*panels)

interactive_conversation = pn.bind(collect_messages, button_conversation)

dashboard = pn.Column(
    inp,
    pn.Row(button_conversation),
    pn.panel(interactive_conversation, loading_indicator=True, height=300),
)

dashboard

# Sisteme göndermek için siparişin özetini JSON olarak istedik
messages =  context.copy()
messages.append(
{'role':'system', 'content':'create a json summary of the previous food order. Itemize the price for each item\
 The fields should be 1) pizza, include size 2) list of toppings 3) list of drinks, include size   4) list of sides include size  5)total price '},    
)  

response = mf.get_completion_from_messages(messages, temperature=0)
print(response)
