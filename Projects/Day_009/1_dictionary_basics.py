programming_dictionary = {
    "Firstname": 'Mohamed',
    "Middle Name":'Aliy',
}
print(programming_dictionary)
programming_dictionary['Lastname'] = "Mohammed"
print(programming_dictionary)
programming_dictionary['Firstname']='Mohammed'
print(programming_dictionary)

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
