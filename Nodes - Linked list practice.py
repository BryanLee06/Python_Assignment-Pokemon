"""
Introduction to linked lists 
"""

class Meals:
    def __init__(self, dataval = None):
        self.dataval = dataval
        self.nextval = None


m1 = Meals('Breakfast')
m2 = Meals('Lunch')
m3 = Meals('Dinner')

m1.nextval = m2
m2.nextval = m3

# this just created a linked list where Lunch is assigned as the next value
# after Breakfast, and dinner is after lunch


thisvalue = m1

while thisvalue:
    print(thisvalue.dataval)
    thisvalue = thisvalue.nextval
