__author__ = 'wkinne'

adj_1 = raw_input("Please Enter An Adjective")
'''
adj_2 = raw_input("Please Enter Another Adjective")

noun_1 = raw_input("Please Enter A Noun")
noun_2 = raw_input("Please Enter Another Noun")
'''
fill_items = []

def addItems(a):

    fill_items.insert(0, a)
    return fill_items

test = addItems(adj_1)

print test





