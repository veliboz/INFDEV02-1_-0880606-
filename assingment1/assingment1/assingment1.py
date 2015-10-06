# Opdracht 1.1
fahrenheit=int(raw_input("Enter a tempurature in fahrenheit: "))

celsuis = (float(fahrenheit - 32) * 5/9)
celsuis = round (celsuis, 2)
print celsuis, "celsuis "


# Opdracht 1.2
celsuis=float(raw_input("Enter a tempurature in celsuis:"))
zero = 0
kelvin = celsuis + 273.15

if kelvin >= zero:
    print kelvin, "kelvin" 
else:
    print "Lower then absolute"


# Opdracht 1.3
cijfer = int(raw_input("Enter your number in: "))
abscijfer = abs(cijfer)
print abscijfer

nummer = int(raw_input("Enter your number in: "))
absnummer = abs(nummer)
print absnummer