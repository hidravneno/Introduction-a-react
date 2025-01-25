print ("hello world!")

#variables
name = "adrian"
last_name = "Aguinaga"
age = 10000000
found = False

print (name)

#if / statement
if age < 100:
    print ("no worry  your not that old")
    print ("im using the indentation")
    print ("im in of the if statement")
elif age == 100: #else if 
    print ("wow your a century")
else: 
    print ("seems that youre really old")

# functions
def sayHello():
    print ("hello world!")
    
def sayGoodbye(name):
    print ("bye " + str(name))
    
# call functions
sayHello()
sayGoodbye(2)

# arrays are called list
color = ["red", "green", "blue", "yellow"]
print (color)
# add an element
color.append("pink")
print (color)
print (color[0])
color.remove("yellow")
print (color)

# for loop 
for col in color:
    print(col)
    
# for(let i=0; color.lenght>0;i++)
# let temp = color[i]
# print temp

# dictionaries
me = {
    "name": "adrian",
    "last_name": "aguinaga",
    "age":38
}
print(me["last_name"])
me["last_name"] ="Doe"
print(me)
me["color"] ="blue"
print(me)