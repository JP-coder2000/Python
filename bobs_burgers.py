class Restaurant:
    name = ""
    type_of = ""
    rating = 0.0
    delivery = True

bobs_burgers = Restaurant()
bobs_burgers.name = "Bob's Burgers"
bobs_burgers.type_of = "American Diner"
bobs_burgers.rating = 4.7
bobs_burgers.delivery = False

print(vars(bobs_burgers))