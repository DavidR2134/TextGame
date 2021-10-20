class Item:
  def __init__(self, name, description, value):
    self.name = name
    self.description = description
    self.value = value
    
  def whoami(self):
    return type(self).__name__
    
class Gold(Item):
  def __init__(self, amount):
    super().__init__("Gold", "A round golden coin", 1)
    self.amount = amount
  
  def whoami(self):
    return type(self).__name__

class Weapon(Item):
  def __init__(self, name, description, value, att_bonus):
    super().__init__(name, description, value)
    self.att_bonus = att_bonus
  
  def whoami(self):
    return type(self).__name__
    
    
class Potion(Item):
  def __init__(self, name, description, value, healing):
    super().__init__(name, description, value)
    self.healing = healing
  
  
items = {"letter" : Item("Letter", "The letter reads: 'Hello there friend'", 1),
  "knife" : Weapon("Knife", "A sharp object", 3, 2),
  "map" : Item("Map", "A map of the building", 0),
  "potion" : Potion("Potion", "A vial with a red shimmering liquid", 30, 15),
  "key" : Item("Key", "Some sort of device used to open a lock", 1)
}
