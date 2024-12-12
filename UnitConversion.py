value = float(input("Put in the value you want to convert: "))
measure = input("What Measurement Scale? eg. mass, distance, currency, temp: ")
#unit = input("Unit of value  entered eg. Kg,Lbs,$,£,mile,Km,Celcius, Farenheit: ")
if measure == "mass" or measure == "Mass" or measure == "MASS" :
    unit = input("Enter Unit eg. Kg,Lbs: ")
    if unit[0] == "K" or unit[0] == "k":
        converted = 0.45 * value
        print(value, "from Kg to Pounds(Lbs) is: ", converted, "Lbs" )
    
    elif unit[0] == "L" or unit[0]=="l":
        converted2 = value/0.45
        print(value, " from Pounds (Lbs) to Kg is: ", converted2, "Kg")
    else: print("Please enter Kg or Lbs")
elif measure == "distance" or measure == "Dist" or measure[0] == "d" :
    unit = input("Enter Unit eg. mile,Km: ")
    if unit[0] == "M" or unit[0] == "m":
        converted = 1.6093 * value
        print(value, "from miles to Km is: ", converted, "Km" )
    
    elif unit[0] == "K" or unit[0]=="k":
        converted = value/1.6093
        print(value, " from Kilometers (Km) to miles is: ", converted, "miles")
    else: print("Please enter Km or miles")
elif measure == "Temperature" or measure == "temp" or measure[0] == "T" :
    unit = input("Enter Unit eg. Celcius, C, Fahrenheit, F: ")
    if unit[0] == "C" or unit[0] == "c":
        converted =  (value*(9/5))+32
        print(value, "from degree Celcius (C) to Fahrenheit (F) is: ", converted, "F" )
    
    elif unit[0] == "F" or unit[0]=="f":
        converted = (value-32)/1.8
        print(value, " from degree Fahrenheit (F) to Celcius is: ", converted, "C")
    else: print("Please enter Km or miles")
elif measure == "Currency" or measure == "currency" or measure[0] == "c" :
    unit = input("Enter Unit eg. GBP,USD,GHS: ")
    if unit == "USD" or unit[0] == "u":
        end_currency = input("What currency are yu converting to: ")
        if end_currency == "GBP" or end_currency == "£":
            rate = 0.789
            converted = rate * value
            print(value, "from USD to GBP is: ", "£", converted )
        elif end_currency == "GHS" or end_currency[0] == "c":
            rate = 14.60
            converted = rate * value
            print(value, "from USD to GHS is: ", converted, "cedis")
        else: print("Please enter GBP (Pound) or GHS (Ghana cedis)")
    elif unit == "GBP" or unit[0] == "g":
        end_currency = input("What currency are yu converting to: ")
        if end_currency == "USD" or end_currency == "$":
            rate = 1.267
            converted = rate * value
            print(value, "from GBP to USD is: ", "$", converted )
        elif end_currency == "GHS" or end_currency == "cedis":
            rate = 18.61
            converted = rate * value
            print(value, "from USD to GHS is: ", converted, "Cedis")
        else: print("Please enter USD (US Dollar) or GHS (Ghanaian Cedis)")
    elif unit == "GHS" or unit[0] == "C":
        end_currency = int(input("What currency are yu converting to: "))
        if end_currency == "GBP" or end_currency == "pound":
            rate = 0.0537
            converted = rate * value
            print(value, "from GHS to GBP is: ", "£", converted )
        elif end_currency == "USD" or end_currency == "usd":
            rate = 0.068
            converted = rate * value
            print(value, "from GHS to USD is: ", converted, "USD")
        else: print("Please enter GBP (Pound) or USD (US Dollar)")
    else: print("Please enter GBP (Pounds), USD (Dollar) or GHS (Gh Cedis)")
else: print("We can not convert this measure")

