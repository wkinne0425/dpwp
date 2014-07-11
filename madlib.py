__author__ = 'wkinne'

#Import the random module. This allows me to get a random number
import random

#Retreiving the variables from the user for the adjectives
adj_1 = raw_input("Please Enter An Adjective: ")
adj_2 = raw_input("Please Enter Another Adjective: ")

#This validates that the 2 variables are not the same
while adj_1 == adj_2:
    print "Adjectives cannot be identical"
    adj_1 = raw_input("Please Enter An Adjective: ")
    adj_2 = raw_input("Please Enter Another Adjective: ")


#Retreiving the variables from the user for the Nouns
noun_1 = raw_input("Please Enter A Noun: ")
noun_2 = raw_input("Please Enter Another Noun: ")

#Validates that the 2 Noun variables are not the same
while noun_1 == noun_2:
    print "Nouns cannot be identical"
    noun_1 = raw_input("Please Enter A Noun: ")
    noun_2 = raw_input("Please Enter Another Noun: ")

#Empty array to be filled my the addItems function
fill_items = []

#This function pushes items to the fill_items array
def addItems(a,aa,n,nn):

    fill_items.insert(0, a)
    fill_items.insert(1, aa)
    fill_items.insert(2, n)
    fill_items.insert(3, nn)

    return fill_items





#This adds all items to array and also creates a variable of that array
add_variables = addItems(adj_1, adj_2, noun_1, noun_2)

if len(fill_items)<4:
    print "There are not enough items in this array"
else:
    a1 = random.randint(0,1)
    n1 = random.randint(2,3)

    a2 = random.randint(0,1)
    n2 = random.randint(2,3)


    print "The " + fill_items[n1] + " went outside and immediately felt " + fill_items[a1] + ". 8 hours passed and now the " + fill_items[n2] + " was on the prowl again, but this time  was filled with " + fill_items[a2] + " and could not contain its self."

















