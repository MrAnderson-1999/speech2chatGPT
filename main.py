import functions


question = "Please explain elaborately " + functions.get_voice_input()
answer = functions.openai_request(question)

print("The question is: \n", question)
print("The answer is: \n", answer)