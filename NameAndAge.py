from datetime import datetime


name = input("What is your name? " +'\n')
current = datetime.now()

if len(name) < 1 :
    print("Invalid name.")

else :
    print("Hello " +name.title() +"!")    # .title() makes the first letter big, looks better 

age = input("When is your birthday? " +'\n')
birthday = datetime.strptime(age, "%d.%m.%Y")  # new datetime parsed from a given string. Order or marker (1.1.2011, 1-1-2011...) can be changed

difference = current - birthday
ageYears = difference.days // 365

print("You are " +str(ageYears) +" old.")
