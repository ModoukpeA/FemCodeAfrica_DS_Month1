#Three ways to concatenate strings

"""
1. + sign
2. the .format() method
3. f ...{} method

"""

adjective = input("Adjective : \n")

print ("My love for Computer Science is very " + adjective)
print ("My love for Computer Science is very {} ".format(adjective))
print (f"My love for Computer Science is very {adjective}")
print ("\n\n\n")

#Madlibs

print(
    " ********** Hey!! We are going to play some grammatical elements to create some funny madlibs. ********** \n\n")

#Three adjectives
adj1 = input("Give a first adjective : ")
adj2 = input("Give a second adjective : ")
adj3 = input("Give a third adjective  : ")

#Two verbs
verb1 = input("\nGive a verb : ")
verb2 = input("Give another verb : ")

#Two nouns
noun1 = input("\nA noun : ")
noun2 = input("Another noun : ")

print("\n\t\t\t Your Madlib sounds like this : \n")

print("As I started my studies in IT field, I feel very " + adj1 + " and " + adj2 + ". \n")
print(f"I was always willing to {verb1} from my friends and the internet." "\n")      
print("My main goal was to {} \n".format(verb2))       
print(f"Finally, I end up as a {noun1} and also a {noun2}. Personally, all this make me " + adj3 + "\n")