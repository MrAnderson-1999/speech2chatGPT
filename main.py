import functions


#print("The value is: \n"+functions.get_voice_input())

print(functions.openai_request(functions.get_voice_input())["choices"][0]["text"])
# functions.openai_request(functions.get_voice_input())