from items import *
from monsters import *

class Location:
  
  def __init__(self, name, description, items, monsters):
    self.name = name
    self.description = description
    self.items = items
    self.monsters = monsters
    
  def __str__(self):
    return self.name + "\n====================\n" + self.description + "\n\n====================\n"
  
  
locations = {
  'hall' : Location("Hall", "A dimly lit hall", [], [creatures["spider"]]),
  'kitchen': Location("Kitchen", "A place to eat", [], []),
  'living room' : Location("Living Room", "A place to sit, relax, and watch some tv", [items['knife']], []),
  'garden' : Location("Garden", "A tranquil setting, fit enough for a victory", [items['key']], [])
}

connected_rooms = {
  "Hall" : { "north" : locations['kitchen'], "west" : locations['living room']},
  "Kitchen" : {"south" : locations['hall']},
  "Living Room" : {"east" : locations['hall'], "south" : locations['garden']},
  "Garden" : {"north" : locations["living room"]}
}
