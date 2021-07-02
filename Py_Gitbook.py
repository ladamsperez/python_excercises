# # Integer refers to an integer number.For example:
# # my_inte= 3
# # Float refers to a decimal number, such as:
# # my_flo= 3.2
# # You can use the commands float()and int() to change from onte type to another:
# float(8)
# int(9.5)

# fifth_letter = "MONTY" [4]
# print (fifth_letter)

# #This code breaks because Python thinks the apostrophe in 'There's' ends the string. We can use the backslash to fix the problem(for escaping characters), like this:
# yee_yee =  'There\'s a snake in my boot!'
# print(yee_yee)

#len() The output when using this method will be the number of letters in the string.
# parrot="Norwegian Blue"
# len(parrot)
# print (len(parrot))

# parrot="Norwegian Blue"
# print(parrot.lower())

# parrot="Norwegian Blue"
# print(parrot.upper())

# Now let's look at str(), which is a little less straightforward. 
# The str() method turns non-strings into strings.
# pi=3.14
# pi=(str(pi))
# print(type(pi))
# #<class 'str'>

# You can work with integer, string and float variables. 
# But don't mix string variables with float and integer ones when making concatenations:
# width + "Hello"

# # Sometimes you need to combine a string with something that isn't a string. 
# # In order to do that, you have to convert the non-string into a string using `str()``.
# print("The value of pi is around " + str(3.14))
# The value of pi is around 3.14

# When you want to print a variable with a string, 
# there is a better method than concatenating strings together.
# The %operator after a string is used to combine a string with variables. 
# The %operator will replace a %s in the string with the string variable that comes after it.

# string_1= "Erle"
# string_2= "drone"
# print (" %s is an awesome %s" %(string_1, string_2))
#  Erle is an awesome drone

name = raw_input("What is your name?")
color = raw_input("What is your favorite color?")

print ("Ah, so your name is %s and your favorite color is %s." % (name,  color))

name = raw_input("What is your name?")
color = raw_input("What is your favorite color?")

print "Ah, so your name is %s and your favorite color is %s." % (name,  color)

