"""
Author: Betty Kang
Descriptions: To convert Temp Celsius to Fahrenheit; or Fahrenheit to Celsius at any time.
Date Updated:
Verson 1: 11/19/2022
Comments: Make a basic convertaion between C and F and list the initial degrees.
Verson 2: 2/19/2022
Commentss: Take an input and convert the temperatuer for the user.
"""
def f_to_c(f_temp): #Fahrenheit Tempeture
  c_temp = (f_temp - 32) * 5/9
  rounded_c = round(c_temp, 1)
  print(str(f_temp) + "F is " + str(rounded_c) + "C degrees.")
  return c_temp

def c_to_f(c_temp): #Celsius Tempeture
  f_temp = c_temp  * (9/5) + 32
  print(str(c_temp) + "C is " + str(f_temp) + "F degrees.")
  return f_temp

def main():
    print("Here are the initial degrees:")
    c_to_f(0)
    f_to_c(75)
    print("---------------------------")
    temp = float(input("Enter your degree: "))
    choice = input("Enter C for Celsius or F for Fahrenheit: ")
    if choice == "C" or choice == "c":
        c_to_f(temp)
    elif choice == "F" or choice == "f":
        f_to_c(temp)
    else:
        print("Errors.")
main()
