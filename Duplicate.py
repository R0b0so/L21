studentid = {
    "id1":{"Name": ["Ethan"], "Class": ["VIII"], "Subjects": ["Math, Science, English"]},
    "id2":{"Name": ["Rya"], "Class": ["VI"], "Subjects": ["Math, Science, English"]},
    "id3":{"Name": ["Rya"], "Class": ["VI"], "Subjects": ["Math, Science, English"]},
    "id4":{"Name": ["David"], "Class": ["VIII"], "Subjects": ["Math, Science, English"]} 
}
result = {}
for key,value in studentid.items():
 if value not in result.values():
  result[key] = value
print(result)