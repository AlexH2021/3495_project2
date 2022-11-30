import requests
import random 

url = 'http://35.235.89.62:3001/input_data?username=testing'


height = random.randint(1, 100)
weight = random.randint(1, 100)
people = ['steven', 'james', 'joe', 'jim', 'jane', 'jill', 'jennifer', 'jessica', 'josh', 'joshua',
'stevn', 'jame', 'je', 'jm', 'jae', 'jil', 'jennfer', 'jesica', 'joh', 'josua']
gender = ['f', 'm', 'female', 'male', 'none']
age = random.randint(1,100)


def send_request():
    data = {
        "name": random.choice(people),
        "height": f'{height}',
        "weight": f'{weight}',
        "gender": random.choice(gender),
        "age" : f'{age}'
        }
    r = requests.post(url, json=data)
    print(r)
      
if __name__ == "__main__":
    while True:
        send_request()
