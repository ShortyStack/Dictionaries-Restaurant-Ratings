
restaurant_rating = {}
sorted_rating = []

restaurant_info = open("scores.txt")

for line in restaurant_info:
    line = line.strip()
    line = line.split(":")
    restaurant_rating[line[0]] = line[1]
    #The "=" is assigning the value "Line [1]" to the
    # "key" "Line[0]" within the dictionary restaurant_rating

sorted_rating = sorted(restaurant_rating.items())

print sorted_rating

for tup in sorted_rating:
    print "{} is rated at {}.".format(tup[0], tup[1])

restaurant_info.close()
