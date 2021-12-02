things = ['a', 'b','c', 'd']
print(things[1])
things[1] = 'z'
print(things[1])

#dictionary 
stuff = {'name': 'sandeep', 'age': 39 , 'height': 6 * 12 + 2}
print(stuff['name'])

#create a mapping of state to abbreviation  
states = {
    'oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

#create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

#add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print outsome cities
print('_' * 10)
print("NY state has:", cities['NY'])
print("OR State has:", cities['OR'])

#print some states
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")
    
#print every city in state
print('_' * 10 )
for abbrev, city in list(cities.items):
    print(f"{abbrev} has the city (city)")
    
# now do both at the same time
print('_'* 10)
for state, abbrev, in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")
    
print('_' * 10)
#safety get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")
    
if not state:
    print("sorry, no Texas.")
    
# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is : (city)") 