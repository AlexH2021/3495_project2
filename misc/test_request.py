import requests
import random 

url = 'http://34.102.113.153:3001/input_data?username=testing'


height = random.randint(1, 100)
weight = random.randint(1, 100)
people = ['steven', 'james', 'joe', 'jim', 'jane', 'jill', 'jennifer', 'jessica', 'josh', 'joshua']


def main():
    while True:
      data = {
          "name": random.choice(people),
          "height": f'{height}',
          "weight": f'{weight}',
          "gender": "F",
          "age" : "123"
          }
      r = requests.post(url, json=data)
      print(r)
      
if __name__ == "__main__":
  main()