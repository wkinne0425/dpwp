__author__ = 'wkinne'


#Retreiving the variables from the user for the adjectives
adj_1 = raw_input("Please Enter An Adjective: ")
adj_2 = raw_input("Please Enter Another Adjective: ")

#This validates that the 2 variables are not the same
while adj_1 == adj_2:
    print "Adjectives cannot be identical"
    adj_1 = raw_input("Please Enter An Adjective: ")
    adj_2 = raw_input("Please Enter Another Adjective: ")


#Retreiving the variables from the user for the Nouns
noun_1 = raw_input("Please Enter A Animal: ")
noun_2 = raw_input("Please Enter Another Animal: ")

while noun_1 == noun_2:
    print "Nouns cannot be identical"
    animal_1 = raw_input("Please Enter An Animal: ")
    animal_2 = raw_input("Please Enter Another Animal: ")


#Retreiving numbers
number_1 = raw_input("Please Enter a Number: ")
number_2 = raw_input("Please Enter a Number: ")
number_3 = raw_input("Please Enter a Number: ")


#Validating that each number is different
while number_1 == number_2 or number_2 == number_3 or number_3 == 1:
    print "All numbers must be different"
    number_1 = raw_input("Please Enter a Number: ")
    number_2 = raw_input("Please Enter a Number: ")
    number_3 = raw_input("Please Enter a Number: ")

#Empty array to be filled my the addItems function
madlib_items = []

def addItems(a1,a2,animal_1, animal_2, n1, n2, n3):

    madlib_items.append(a1)
    madlib_items.append(a2)
    madlib_items.append(animal_1)
    madlib_items.append(animal_2)
    madlib_items.append(n1)
    madlib_items.append(n2)
    madlib_items.append(n3)


    print "This week the pound took in " + madlib_items[4] + " " + madlib_items[2] + "'s and " + madlib_items[5] + " " + madlib_items[3] + "'s. Out of all of those animals " + madlib_items[6] + " of them found owners already. All of the " + madlib_items[2] + "'s were " + madlib_items[0] + " and all of the " + madlib_items[3] + "'s were " + madlib_items[1]








addItems(adj_1, adj_2, noun_1, noun_2, number_1, number_2, number_3)
