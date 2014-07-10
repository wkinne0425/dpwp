__author__ = 'wkinne'

adj_1 = raw_input("Please Enter An Adjective: ")

adj_2 = raw_input("Please Enter Another Adjective: ")

while adj_1 == adj_2:
    print "Adjectives cannot be identical"
    adj_1 = raw_input("Please Enter An Adjective: ")
    adj_2 = raw_input("Please Enter Another Adjective: ")



noun_1 = raw_input("Please Enter A Noun: ")
noun_2 = raw_input("Please Enter Another Noun: ")

while noun_1 == noun_2:
    print "Nouns cannot be identical"
    noun_1 = raw_input("Please Enter A Noun: ")
    noun_2 = raw_input("Please Enter Another Noun: ")

fill_items = []

def addItems(a,aa,n,nn):

    fill_items.insert(0, a)
    fill_items.insert(1, aa)
    fill_items.insert(2, n)
    fill_items.insert(3, nn)

    return fill_items






test = addItems(adj_1, adj_2, noun_1, noun_2)

if len(fill_items)<4:
    print "There are not enough items in this array"
else:
    print "The " + fill_items[2] + " was very " + fill_items[0]











