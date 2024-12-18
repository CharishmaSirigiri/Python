#to check whether a number is divisible by 5 and 11
a=int(input("enter a number"))
if a%5==0 and a%11==0:
    print("it is divisible by 5")
else:
    print("not divisible")    


#to check whether the given number is even or not
a=int(input("enter a number"))
if a%2==0:
    print("the number is even")    
else:
    print("the number is odd")



#to check whether the letter is vowel or consonant
A=input("enter any alphabet")
if A in "a" "e" "i" "o" "u":
    print("it is a vowel")
else:
    print("it is a consonant")   



#to check whether the given input is alphabet or not
char=input("enter any alphabet")
if char.isalpha():
    print("it is an alphabet")
else:
    print("its not an alphabet")    
    
        

#to check whether the letter is uppercase or lowercase
alphabet=input("enter any letter")
if alphabet.isupper():
    print("its an uppercase letter")
else:
    print("its a lowercase letter")    


    #area of circle
pi=3.14
r=float(input("enter r value :"))
print(int(pi*r*r))

#area of traingle
b=float(input("enter base value:"))
h=float(input("enter height value:"))
print(f"area of traingle is {(1/2)*b*h}")

#celcius to fahrenheit 
fahrenheit=int(input("enter fahrenheit value"))
celcius=int((fahrenheit - 32) * 5 / 9 )
print(f"celcius value is {celcius}")
