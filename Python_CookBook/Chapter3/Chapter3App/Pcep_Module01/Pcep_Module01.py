
def hello_world():
    print ('Hello, world!')
    friends = ['john', 'pat', 'gary', 'michael']
    for i, name in enumerate(friends):
       print ("iteration {iteration} is {name}".format(iteration=i, name=name))


print('The first sentence', end='\r\n')
print('The second sentence', end='\r\n')
print('The last sentence.')

print('Mercury', 'Venus', 'Earth', sep=', ', end=', ')
print('Mars', 'Jupiter', 'Saturn', sep=', ', end=', ')
print('Uranus', 'Neptune', 'Pluto', sep=', ')
