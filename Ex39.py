# create a mapping of county to abbreviation
counties = {
    'Mombasa': 'MSA',
    'Nairobi': 'NBO',
    'Naivasha': 'NVA',
    'Eldoret': 'ELD',
    'Kisumu': 'KSM'
}

# create a basic set of counties and some cities in them
cities = {
    'MSA': 'Nyali',
    'KSM': 'Tom Mboya',
    'NBO': 'Kileleshwa'
}

# add some more sub-counties
cities['ELD'] = 'Mursik'
cities['NVA'] = 'Mungiki'

# print out some cities
print('-' * 10)
print("ELD county has: ", cities['ELD'])
print("NVA County has: ", cities['NVA'])

# print some counties
print('-' * 10)
print("Kisumu abbreviation is: ", counties['Kisumu'])
print("Nairobi abbreviation is: ", counties['Nairobi'])

# do it by using the state then cities dict
print('-' * 10)
print("Kisumu has: ", cities[counties['Kisumu']])
print("Nairobi has: ", cities[counties['Nairobi']])

# print every county abbreviation
print('-' * 10)
for counties, abbrev in counties.items():
    print("%s has the city %s" % (cities, abbrev))

# print every city in county
print('-' * 10)
for abbrev, city in cities.items():
    print("%s has the city %s" % (abbrev, cities))

# now do both at the same time
print('-' * 10)
for county, abbrev in counties.items():
    print("%s county is abbreviated %s and has city %s" % (
        counties, abbrev, cities[abbrev]))

print('-' * 10)
# safely get an abbreviation by state that might not be there
counties = counties.get('Texas', None)

if not counties:
    print("Sorry no Texas.")

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print("The city for the state 'TX' is: %s" % city)

