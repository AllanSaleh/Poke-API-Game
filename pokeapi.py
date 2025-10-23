import requests

def get_pikachu():
  '''Function to grab pikachu data from pokeapi
  specifically name, health stat'''

  url ="https://pokeapi.co/api/v2/pokemon/pikachu"

  response = requests.get(url)

  if response.status_code == 200:
    data = response.json() #Converting JSON to Python
    pikachu = {
      "name": data['name'],
      "hp": data['stats'][0]["base_stat"]
    }
    return pikachu
  else:
    print("Failed to catch Pikachu")
    

print(get_pikachu()) 