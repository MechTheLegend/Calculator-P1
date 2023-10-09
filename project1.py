symbol = input("what symbol? ")
decimal = input("use decimals? ")
first = input("first number: ")
second = input("second number: ")
if decimal == "no":
    sum = int(first) + int(second)
if decimal == "no":
    difference = int(first) - int(second)
if decimal == "no":
    product = int(first) * int(second)
if decimal == "no":
    dividend = int(first) / int(second)
if decimal == "no":
    exponent = int(first) ** int(second)
if decimal == "yes":
    decimal_sum = float(first) + float(second)
if decimal == "yes":
    decimal_difference = float(first) - float(second)
if decimal == "yes":
    decimal_product = float(first) * float(second)
if decimal == "yes":
    decimal_dividend = float(first) / float(second)
if decimal == "yes":
    decimal_exponent = float(first) ** float(second)
if symbol == "+" and decimal == "no":
    print ("answer: " + str(sum))
if symbol == "-" and decimal == "no":
    print ("answer: " + str(difference)) 
if symbol == "*" and decimal == "no":
    print ("answer: " + str(product))
if symbol == "/" and decimal == "no":
    print ("answer: " + str(dividend))
if symbol == "^" and decimal == "no":
    print ("answer: " + str(exponent))
if symbol == "+" and decimal == "yes":
    print ("answer: " + str(decimal_sum))
if symbol == "-" and decimal == "yes":
    print ("answer: " + str(decimal_difference))
if symbol == "*" and decimal == "yes":
    print ("answer: " + str(decimal_product))
if symbol == "/" and decimal == "yes":
    print ("answer: " + str(decimal_dividend))
if symbol == "^" and decimal == "yes":
    print ("answer: " + str(decimal_exponent))