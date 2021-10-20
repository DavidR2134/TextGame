from locations import *
from os import system, name
import sys

current_location = locations["kitchen"]


def clear():
  if name == 'nt':
    _ = system('cls')
  else:
    _ = system('clear')

def winner():
  if "key" in player.inventory.keys() and current_location.name == "Garden":
    print("You win!")
    sys.exit(0)

def player_menu(monster):
  print("What would you like to do?")
  print("HP: ", player.hp)
  user = input("> ")
  
  if user.lower() == "run":
    if player.run():
      print("You manage to escape!")
      return "run"
  
  elif user.lower() == "attack":
    plahit = player.attack()
    if plahit > 0:
      print("You attack the {} and do {} damage!".format(monster.name, plahit))
      monster.get_hit(plahit)
      if monster.hp <= 0:
        clear()
        print("The {} falls, slain!".format(monster.name))
        wait = input("\nPress enter to continue...")
        clear()
        return "death"
    else:
      print("You swing but miss!")
  else:
    print("You can only attack or run!")
  

def encounter():
  mon = current_location.monsters[0]
  
  while mon.hp > 0 or player.hp > 0:
    clear()
    monhit = mon.attack()
    if monhit > 0:
      print("The {} attacks and does {} damage!".format(mon.name, monhit))
      player.get_hit(monhit)
      if player.hp <= 0:
        print("Game Over.")
        sys.exit(0)
    else:
      print("The {} attempts to hit you but misses!".format(mon.name))
  
    action = player_menu(mon)
    
    if action == "run":
      break
    elif action == "death":
      current_location.monsters.pop()
      break


while(True):
  winner()
  clear()
  print(current_location)
  print("Inventory:\n====================")
  for key, item in player.inventory.items():
    print("\t", item.name)
  print()
    
  
  if current_location.monsters:
    action = encounter()
    print(current_location)
    
  for locations in connected_rooms[current_location.name]:
    print(locations , ": ", connected_rooms[current_location.name][locations].name)
    
  user = input("> ")
  
  if user[:2] == "go":
    if user[3:] in connected_rooms[current_location.name]:
      current_location = connected_rooms[current_location.name][user[3:]]
    else:
      print("You can't go that way!")
      wait = input("\nPress enter to continue....")
      
  elif user[:2] == "ge":
    if user[4:] == current_location.items[0].name.lower():
      player.add_item(current_location.items[0])
      print("You take the {}".format(current_location.items[0].name))
      current_location.items.pop()
    wait = input("\nPress enter to continue....")

  elif user[:2] == "us":
    if user[4:] in player.inventory:
      typ = player.inventory[user[4:]].whoami()
      if typ == "Weapon":
        player.att += player.inventory[user[4:]].att_bonus
        del player.inventory[user[4:]]
      elif typ == "Item":
        print("You can't do anything with that")
        wait = input("\nPress enter to continue...")
      elif typ == "Potion":
        print("You drink the potion and regain {} health!".format(player.inventory[user[4:]].healing))
        player.heal(player.inventory[user[4:]].healing)
        wait = input("\nPress enter to continue...")
        del player.inventory[user[4:]]
      else:
        print("You don't have that item...")    
        wait = input("\nPress enter to continue...")
  
  elif user[:4] == "look":
      try:
        print(player.inventory[user[5:]].description)
        wait = input("\nPress enter to continue...")
      except KeyError:
        try:
          if current_location.items[0].name.lower() == user[5:].lower():
            print(current_location.items[0].description)
            wait = input("\nPress enter to continue...")
          else:
            raise IndexError
        except IndexError:
          print("That isn't here...")
          wait = input("\nPress enter to continue...")
  
  else:
    print("I don't understand, please enter:\n1) go [direction]\n2) get [item]\n3) use [item]\n4) look [item]")
    wait = input("\nPress enter to continue...")
