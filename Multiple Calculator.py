def calculator (num1, symbol ,num2 ) : # Calculator Opretion 
    
    if symbol == "+" :
        total = num1 + num2
        return total
    elif symbol == "-"  :
        total = num1 - num2
        return total
        # (Multiply And Divide Opretion 
    elif symbol  == "*" or symbol == "×" or symbol == "x" or symbol == "X": 
        total = num1 * num2  
        return total
    elif symbol == "**" or symbol == "*2" or symbol == "×2" or symbol == "×²" or symbol == "x2" or symbol =="X2" :
        total = num1 ** num2
        return total
    elif symbol  == "/" or symbol  == "÷" :
        if num2 == 0 :
            return "0 Error division Invalid "
        else :
            total = num1 / num2
            return total 
    elif symbol  == "//" or symbol  == "÷2" or symbol == "÷²" :
        if num2 == 0 :
            return "0 Error division Invalid "
        else :
            total = num1 // num2
            return total 
            
    #----- Calculator Opretion Finish -----#
           
            
            
def feet_to_meter(size, convert) : # Feet 🔄 Meter 
    
    try:
        size = float(size)
    except ValueError  :
        return "invalid Input Enter Size Value (int or Float)"
        
    if convert == 1:
        total_size = size * 3.28084 
        return total_size
    elif convert == 2 :
        total_size = size / 3.28083
        return total_size
    else :
        return "Just Select (1,2)"     
     
    #--- Feet To Meter Finish Opretion ---# 
    
def inch_to_cm( size, convert) : # Inch To Centimeter 
    
    try:
        size = float(size)
    except ValueError :
        return "Invalid input Enter Size Value (int or float)"
        
    if convert == 1 :
        total_size = size * 2.54
        return total_size
    elif convert == 2 :
        total_size = size / 2.54
        return total_size
    else :
        return "Just Select (1,2)"      
           
    #--- Inch To CM Opretion Finish ---#        
    
def kg_to_pound(weight , convert ): # weight_mass KG To Pound
    
    try :
        weight = float(weight) 
    except ValueError :
        return "invalid Input Enter Size Value (int or Float)"
        
    if convert == 1 :
        total_weight = weight * 2.20462
        return total_weight
    elif convert == 2 :
        total_weight = weight / 2.20462 
        return total_weight 
            
    #--- KG To Pound Opretion Finish ---#
     
def km_to_mile (length , convert) : # Kilometers To Miles
    
    try :
        length = float(length)
    except ValueError :
        return   "invalid Input Enter Size Value (int or Float)"
        
    if convert == 1 :
        total_length = length / 0.621371
        return total_length
    elif convert == 2 :
        total_length = length * 0.621371  
        return total_length 
        
    #--- KM To Mile Opretion Finish ---#   
            
def age_birth(age, current_year) : # Age 
    
    your_age = current_year - age
    return your_age
    
    #--- Age Opretion Finish ---#   
        
    
    
# -----Main-----#       
def main() :
    print ("Welcome To Multi Calculator")
    while True :
        
        # Choose What Do You Want
        print ("1 Calculator")
        print ("2 Feet To Meter Calculator ")
        print ("3 Centimeter To Inch")
        print ("4 KG To Pound")
        print ("5 Kilometer To Mile")
        print ("6 Age Calculator")
        print ("7 Exit program")
        
        
        try:
            choice = int(input("Enter Choice "))
            
            
            if choice == 1 : # Calculator Inputs / Output 
                try:
                    number1 = int(input("Enter Number "))
                    select_symbol = input("Select Symbol (-+÷§) : ")
                    number2 = int(input("Enter Second Number "))
                    result = calculator(number1 , select_symbol , number2)
                    print (f"{number1} {select_symbol } = {result}")
                    
                except ValueError :
                    print ("Make Sure Numbers in digits Or Valid Opretion Symbol") 
                    #---Calculator Finished ---#
                    
                
            elif choice == 2 : # Feet Meter Input / Output 
                try:
                    any_size = input("Enter Size ")
                    converter = int(input("1 Meter To Feet : 2 Feet To Meter : "))
                    result = feet_to_meter(any_size , converter)
                    
                    if converter == 1 :
                        print (f"{any_size} Meter = {result} Feet")
                    else:
                        print (f"{any_size} Feet = {result} Meter")
                        
                except ValueError :
                    print ("Make Sure Size In Digits Or Meter To feet In Just Select (1 or 2)")
                    #---Feet To Meter Fisnished ---#
                
                
            elif choice == 3 : # Centimeters To Inch Input/Output 
                try:
                    mini_size = input("Enter Size You Want Convert inch cm ")
                    converter  = int(input("1 inch to centimeter : 2 Centimeter to Inch : "))
                    result = inch_to_cm(mini_size, converter)
                    
                    if converter == 1 :
                        print (f"{mini_size} Inch = {result} Centimeter")
                    else :
                        print (f"{mini_size} Centimeter = {result} Inch")
                             
                except ValueError :
                    print ("Make Sure Enter Size in Digits Or just Select (1, 2)")
                     #---Inch To CM Finished ---#
                           
            elif choice == 4 : # KG To Pound Input/Output 
                try :
                    weight_value = input("Enter Weight/Mass ")
                    weight_converter = int(input("(1 KG To Pound) (2 Pound To KG) "))
                    result = kg_to_pound(weight_value , weight_converter)
                    
                    if weight_converter == 1 :
                        print (f"{weight_value} Kg = {result} Pound")
                    elif weight_converter == 2 :
                        print (f"{weight_value} Pound = {result} KG")
                    
                except ValueError  :
                    print ("Make Sure Enter Weight In Digits") 
                    #--- KG To Pound Finished ---#    
                    
            elif choice == 5 : # KM To Mile Input/Output 
                try :
                    area_length = input("Enter Length ") 
                    converter  = int(input("(1 KM To Mile) (2 Mile To KM) "))
                    result = km_to_mile(area_length , converter)
                    
                    if converter == 1 :
                        print (f"{area_length} KM = {result} Mile ")
                    elif converter == 2 :
                        print (f"{area_length} Mile = {result} KM")
                        
                except ValueError :
                    print ("Make Sure Enter Length In Digits") 
                    #--- KM To Mile Finished ---#
            
            elif choice == 6 : # Agr Birth Input/Output 
                try:
                    birth_or_age = int(input("Enter Your Or Birth Year "))
                    now_year = 2025
                    result = age_birth(birth_or_age , now_year)
                    print (f"You Old Are {result}")
                
                except ValueError :
                    print ("Make Sure Enter Age In Digits")
                    #--- Age Finished ---#
                    
                                 
                        
                    
           elif choice == 7 :
                print ("Thank You")
                break  
                
                
                    
                
        except ValueError  :
            print ("Invalid Choice ")
            

main()

    
        
        
        
        
        
    
