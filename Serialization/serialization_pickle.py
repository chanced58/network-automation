#Data Serializaiton in Python

import pickle

# Declaring a dictionary
friends1 = {"Dan: ": [20, "London", 3234342], "Maria":[25, "Madrid", 43525222]}
friends2 = {"Bob: ": [30, "Sydney", 3454323], "Steve":[40, "Amarillo", 8066816]}
friends = (friends1, friends2)

# Serializing the dictionary to binary file called friends.dat
with open('friends.dat', 'wb') as f:
    pickle.dump(friends, f)

# Deserializing into a Python object
with open('friends.dat', 'rb') as f:
    obj = pickle.load(f)
    print(type(obj))
    print(obj)