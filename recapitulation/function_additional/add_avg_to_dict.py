def addAvg(dict_name):    
    dict_name.update({"avg" : sum(dict_name.values()) / 3})


notes = {
  "sem_1": 9.0,
  "sem_2": 8.0,
  "exam" : 9.0, 
  }

addAvg(notes)
print(notes)