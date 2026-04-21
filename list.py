#list - index


marvel = ["Tony Stark", "Steve Rogers", "Thor", "Natasha Romonof", "Hulk", "Clint"]
marvel[4] = "Bruce Banners"
marvel.append("Peter Parker")
marvel.insert(1, "Black Panther") # insert element at the mentioned position
marvel.append("Batman") #adds element at last
print(marvel)
marvel.remove("Batman") #removes element
marvel.pop() #remove last element
print(marvel)
print(marvel.index("Steve Rogers")) #display index 1 based list not 0 based
marvel.sort()
print(marvel)
marvel.reverse()
print(marvel)

# for i in range(len(marvel)):
#     print(marvel[i])

#[print(x) for x in marvel]
avengers = marvel.copy()
print(avengers)
