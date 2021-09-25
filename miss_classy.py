a = """
Hello There!
My Name Is {name}.
I Am From {destiny}.
I Am {age} Year Old.
My 1st Cry On {dob}.
My Birth Place is {place}.
Thank You!
"""

b = input("What Is Your Name?: ")

c = input("Where Are You From?: ")

d = str(input("How Many Years Old You Are?:" ))

e = str(input("What Is Your Birth Date?: "))

f = input("What Is Your Birth Place?: ")

a = a.replace("{name}", b)

a = a.replace("{destiny}", c)

a = a.replace("{age}", d)

a = a.replace("{dob}", e)

a = a.replace("{place}", f)

print(a)
