from interpreter import interpreter

# Open Interpreter Settings
interpreter.llm.api_key = "openai_api_key_here"
interpreter.llm.model = "gpt-3.5-turbo"
interpreter.auto_run = True
interpreter.custom_instructions = "I love markdown."

# Have it Write a Script
result = interpreter.chat("Write a python script that displays 'Hello, World!' in ASCII Art. Get creative.")

# Have it Save that Script
result = interpreter.chat("Now save the python script you've made into ~/Documents/GitHub/explorations-jh. When you do, it's probably best to touch the file first, then nano it and input your text via nano.")

# print(result)