"""Time to play with Python dictionaries!
You're going to work on a dictionary that
stores cities by country and continent.
One is done for you - the city of Mountain 
View is in the USA, which is in North America.

You need to add the cities listed below by
modifying the structure.
Then, you should print out the values specified
by looking them up in the structure.

Cities to add:
Bangalore (India, Asia)
Atlanta (USA, North America)
Cairo (Egypt, Africa)
Shanghai (China, Asia)"""

locations = {'North America': {'USA': ['Mountain View']}}

"""Print the following (using "print").
1. A list of all cities in the USA in
alphabetic order.
2. All cities in Asia, in alphabetic
order, next to the name of the country.
In your output, label each answer with a number
so it looks like this:
1
American City
American City
2
Asian City - Country
Asian City - Country"""
def addCity(myDict, city, country, continent):
    if continent not in myDict:
        myDict[continent] = {}
    if country not in myDict[continent]:
        myDict[continent][country] = []
    myDict[continent][country].append(city)

def sortCity(continent, country):
    return sorted(locations[continent][country])

def myKey(element):
    return element[0]
    
addCity(locations, "Bangalore", "India", "Asia")
addCity(locations, "Atlanta", "USA", "North America")
addCity(locations, "Cairo", "Egypt", "Africa")
addCity(locations, "Shanghai", "China", "Asia")

print 1
list = sortCity("North America", "USA")
for city in list:
    print city
    
print 2
myCities = []
for continent, value in locations.items():
    if continent == "Asia":
        for country, cities in value.items():
            for city in cities:
                myCities.append([(city,country)])
listT = sorted(myCities, key=myKey)
for cityInfo in listT:
    print cityInfo[0][0] + " - " + cityInfo[0][1]
