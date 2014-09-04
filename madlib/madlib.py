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
noun_1 = raw_input("Please Enter A Noun: ")
noun_2 = raw_input("Please Enter Another Noun: ")

while noun_1 == noun_2:
    print "Nouns cannot be identical"
    noun_1 = raw_input("Please Enter A Noun: ")
    noun_2 = raw_input("Please Enter Another Noun: ")


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

