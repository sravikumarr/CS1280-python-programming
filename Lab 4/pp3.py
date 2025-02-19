BCA ={
  "USN":"1RUA24BCA0086",
  "Name":"Sumukh R"
}
#CALLING THE KEY VALUE
print("Here are the keys")
for key in BCA:
    print (key)
#CALLING THE VALUES
print("Here are the values")
for key in BCA:
    print(BCA[key])
#HERE ARE THE KEYS IN VALUES
for key,values in BCA.items():
    print(key,values)
print()
