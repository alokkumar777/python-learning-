# Day 1 and 2 topics covered 
# * - Variables
# * - Valid & Invaild
# * - print(), sep & end parameter
# Todo: - Operator
# Todo: - Datatype
# Todo: - Conversion
# * - ASCII code
# Todo: - type()

# ? Variable
# Variables - Name of the location in memory used to store data.
# Here alphanumeric code is data and productKey is the location name where the data is stored.
productKey = "7WE8 8GH7 8HSW 56SE 3D5G" 
print(productKey) # print() prints the specified msg to the screen

# ? ord() return ASCII code of given character
conversionToASCII = ord("5") 
print("ACSII code of given character: ", conversionToASCII)

# ? ACSII to Binary conversion - bin()
conversionACSII_ToBinary = bin(conversionToASCII)
print("ASCII to binary: ", conversionACSII_ToBinary)


# ? Binary to Decimal conversion - int(binary_number, 2)
binaryContainer = conversionACSII_ToBinary
conversionBinaryToDecimal = int(binaryContainer, 2)
print("binary to decimal", conversionBinaryToDecimal)

# ? Decimal to Character conversion - chr()
conversionDecimalToChar = chr(conversionBinaryToDecimal)
print("decimal to character", conversionDecimalToChar)   

# ? sep - parameter specifies the separator between the items u r printing
print("Hello", "world")  # Default separator (space)
print("Hello", "World", sep="-")  # Custom separator
print("Hello", "World", sep="")  # No separator

# ? end -  parameter specifies what to print at the end of the output
print("Hello")  # Default end (newline)
print("Hello", end="")
print("World")
print("Hello", end="! ")
print("World")
