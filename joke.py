from JokePy import prompt
import random

questions = [ 
  {"type": "input", "message": "What's your name?", "name": "name"},
  {"type": "list", "message": "What kind of joke do you want?", "choices": ["Bad", "Dark", "Random", "All"]}
]

result = prompt(questions)
name = result ["name"]
joke = result [1]

funnyArray = ["This is a bad joke!", "This is a dark joke", "This is a random joke!", "These are all jokes!" ]

if joke == "Bad":
  print (funnyArray[0])
elif joke == "Dark":
  print (funnyArray[1])
elif joke == "Random":
  import random
  randJoke =random.randint(0,1)
  print(funnyArray[randJoke])
elif joke == "All":
  print(funnyArray)


  

