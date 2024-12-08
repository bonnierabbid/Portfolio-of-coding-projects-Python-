
#Exercise 3: Temperature Converter

def main():
    print("This is a Temperature Converter! ")
    CorF = input("Celsius or Fahrenheit? Type C or F to choose: ").strip().upper()
    i = 1
    while i == 1:
        temperature = int(input("Type your tempreture(number): "))
        if CorF == "C" and -90 < temperature < 60:
            break
        elif CorF == "F" and -129 < temperature < 135:
            break
        else:
            print("Thats not a valid tempreture on earth, please type again?") 
        

    if CorF == "C":
        temperature = (temperature * (9/5)) + 32
        print("Celsius to Fahrenheit = " + str(temperature)) 
    elif CorF == "F":
        temperature = (temperature -32) * 5/9
        print("Fahrenheit to Celsius = " + str(temperature))
        
        

if __name__ == "__main__":
    main()
            
        
                
            
        