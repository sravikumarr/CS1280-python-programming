person = {
   "p1": {"name": "Rhee", "profession": "engineer"},
   "p2": {"name": "Chandhana", "profession": "doctor"},
   "p3": {"name": "Meeera", "profession": "teacher"}
}
# Access a value
print(person)
p1_name = person["p1"]["name"]
# Update a value
person["p1"]["profession"] = "farmer"
# Delete an entry
del person["p2"]
# Iterate through dictionary
for p, details in person.items():
    print(f"{p}:")
for key, value in details.items():
    print(f" {key}: {value}")
