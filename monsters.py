import random
from items import *

class Monster:
  def __init__(self, name, hp, att, ac):
    self.name = name
    self.hp = hp
    self.att = att
    self.ac = ac
  
  def attack(self):
    r = random.randint(0, self.att)
    return r
  
  def get_hit(self, dam):
    self.hp -= dam
    return self.hp
  
  def heal(self, heal):
    self.hp += heal
    return self.hp
    
  def run(self):
    r = random.randint(0, self.ac)
    if r > self.ac/2:
      return True
    else:
      return False
      

class Player(Monster):
  def __init__(self, name, hp, att, ac, inventory):
    super().__init__(name, hp, att, ac)
    self.inventory = inventory
  
  def add_item(self, item):
    self.inventory[item.name.lower()] = item
    
  def use_item(self, item):
    if item in self.inventory:
      self.inventory.remove(item)
    
creatures = {
  "spider" : Monster("Spider", 30, 6, 11)
}

player = Player("Player", 50, 10, 12, {items['letter'].name.lower():items['letter'], items['potion'].name.lower() : items['potion']})
