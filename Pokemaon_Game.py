import requests
from practice_1 import get_pokemon_data

class Pokemon:
  '''Represents a simple Pokemon object, instead of just a dictionary'''
  def __init__(self, name, id, hp, attack, sprite_url, type):
    self.name = name
    self.id = id,
    self.hp = hp
    self.attack = attack
    self.sprite_url = sprite_url
    self.type = type
  
  def info(self):
    print(f"=============== {self.name}'s Info ===============")
    print(f"ID: {self.id}")
    print(f"Stats: HP - {self.hp} Attack - {self.attack}")
    print(f"Type: {self.type}")
    print(f"Sprite: {self.sprite_url}")



class Player:
  def __init__(self, name):
    self.name = name
    self.team = [] #List of pokemon objects No more than 6 at a time
  
  def add_pokemon(self, pokemon):
    '''Takes in a pokemon object and adds it to the team if there is room'''

    if len(self.team) < 6:
      self.team.append(pokemon)
      print(f"{pokemon.name} has been added ot the team!")
      return
    else:
      print("The team is full, remove a pokemon to make space.")
      return
  


charmander = get_pokemon_data("charmander")
print(charmander)
# {'name': 'charmander', 'id': 4, 'hp': 39, 'attack': 52, 'sprite_url': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/4.png', 'type': 'fire'}

# object_charmander = Pokemon(name = charmander["name"], pokemon_id=charmander['id'], hp=charmander['hp'], attack=charmander['attack'], sprite_url=charmander['sprite_url'], pokemon_type=charmander['type'])

object_charmander = Pokemon(**charmander)

# object_charmander.info()

new_player = Player("Ash")
new_player.add_pokemon(object_charmander)



