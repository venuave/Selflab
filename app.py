print("Welcome! This is your shopping list!")

items=[]

def add_item():
  print("What item would you like to add?")

  item = input("> ")
  items.append(item)
  
  print(items)

  print("Do you want to add anything else? y/n?")
  response = input("> ")

  if response == "y":
    add_item()
  else:
    print("Ok bye")
    save_list()


def save_list():
  file = open("list.txt", "w")

  for item in items:
    file.write(item + "\n")
  file.close()

print ("Your list was saved!")

add_item()
  

