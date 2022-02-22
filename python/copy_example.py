import copy

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "person": {
      "name": "Priyank",
      "location": "US",
      "state": "LA",
  }
}

# Way1, Way2 and Way3 do the shallow copy.
# Way4 is deep copy

# Way1
mydict = thisdict.copy()

# Way2
#mydict = dict(thisdict)

mydict["brand"] = "Hyundai"
mydict["person"]["name"] = "Richa"

# Way3
mydict = copy.copy(thisdict)
mydict["person"]["location"] = "India"

# Way4
mydict = copy.deepcopy(thisdict)
mydict["person"]["state"] = "Guj"

print(thisdict)
print(mydict)