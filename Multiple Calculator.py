


print ("Multiple Calculator")



while True:
    print("1 simple Calculator ")
    print("2 feet To Meter ")
    print ("3 CM to Inch ")
    print("4 GM/ KG/ Ton/ ")
    print("5 KM To Mile ")
    print ("6 Current Age ")
    print ("7 Exit")
    try:
         choice=int(input("What Do You Calculate? "))
         
         if choice==1 : # Simple Calculator Opretion
             try:
                  num1=int(input("enter Number"))
                  symbol=input(" Select Opren  +  -  *  ÷  ")
                  num2=int(input("enter Second number"))
                  
                  if symbol=="+":
                      print (f"{num1+num2}")
                  elif symbol =="-"  :
                      print (f"{num1-num2}")
                  elif symbol =="*" :
                      print (f"{num1*num2}")
                  elif symbol =="÷"   :
                      if num1 != 0:
                          print (f"{num1/num2}")
                      else:
                          print ("0÷anything is 0" )
                  else: 
                      print ("only below Symbol Opretion possible \n(- + ÷ *)") 
             except ValueError :
                 print ("Select Symbol Or Make Sure You Entered A digits")   
                          
         elif choice ==2: # Feet To Meter Opretion 
             try:
                 size=int(input("Enter Feet Or Meter You Want To Convert "))
                 convert=int(input("1 Feet  2 Meter"))
                 if convert==1:
                     print (f" {size}Feet = {size/3.28084}Meter")
                 elif convert ==2:
                     print (f"{size}Meter = {size*3.28084}Feet")
             except ValueError :
                 print ("Enter Just Feet or meter Length Or Select Convert Option 1 or 2" )   
                 
         elif choice==3: # Centimeter to Inch Opretion 
             try:
                 mini_size=int(input("Enter Inch Or Centimeter"))
                 inch_cm=int(input(f"{mini_size} Is 1 Inch 2 Centimeter ?"))
                 if inch_cm ==1:
                     print (f" {mini_size}Inch = {mini_size*2.54} Centimeters")
                 elif inch_cm==2:
                     print (f" {mini_size}Centimeter = {mini_size/2.54} Inch")
             except ValueError :
                 print ("uncomplete" )
                 
         elif choice ==4: # Grams To Tons  Opretion 
             try:
                 weight=int(input("Enter weight "))
                 transform=int(input(f"Your Weight Is 1 GM 2 KG 3 TON \npick What is This"))
                 if transform==1:
                     print (f" {weight}GM = {weight/1000}KG \n {weight}GM = {weight/1000000}TON")
                 elif transform ==2:
                     print (f" {weight}KG = {weight/1000}TON \n {weight}KG = {weight*1000}GM") 
                 elif transform ==3:
                     print (f" {weight}TON = {weight*1000}KG \n {weight}TON = {weight*1000000}GM") 
                 else:
                     print ("Select Your Wait Is What? GM KG Or TON")   
             except ValueError :
                 print ("enter Just Weight Size Or Pick What Is This KG GM TON")
                 
         elif choice ==5: # Kilometers To Miles Opretion 
             try:
                 length=int(input("Enter Length You Want To Convert"))
                 distance_convert=int(input("Your Distance Is 1 Meter 2 Kilometer 3 Mile "))
                 if distance_convert==1:
                     print (f" {length}Meter = {length/1000}KM \n {length}Meter = {length*0.000621371}Mile")
                 elif distance_convert==2:
                     print (f" {length}Kilometer = {length*1000}Meter \n {length}Kilometer = {length*0.621371}Mile")
                 elif distance_convert==3:
                     print (f" {length}Mile = {length/0.621371} Kilometer \n {length}Mile = {length/0.000621372}Meter")
                 else:
                     print ("Select Your Length Is What Meter Kilometer Or Mile")  
             except ValueError :
                 print ("Enter Only Length Don't Use KM Or Mile Or Make Sure You Choose Your Length what Is")     
                 
         elif choice==6: # age Opretion 
             try:
                 age=int(input("Enter Your Age Or Birth Year"))
                 current_year=2025
                 your_age=current_year-age
                 print (f" your Old are{your_age}")
             except ValueError :
                 print ("Just Upload Age Or Birth Year") 
         
         elif choice==7:
             print ("Thank You")
             break        
                           
    except ValueError :
        print ("just Choose A Number Do You Want")
        
        
        
        
        
    