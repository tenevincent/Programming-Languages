result = type(x*x for x in [2, 4, 6])    
print(result)


class Flight:
    
    def number(self):
        return "SN0060"


print(result)
flight = Flight()
print(flight.number())

result = Flight.number(flight)
print(result)
