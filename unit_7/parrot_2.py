prompt = "\n Tell me something, and i will repeat it back to you:"
prompt +="\n Enter 'quit to end the progtam."

active = True
while active:
  message = input(prompt)

  if message == 'quit':
      active = False
  else:
    print (message)