# Task 1: Start
# Task 2: Temperature Conversion
# Task 3: User Experience

def get_temperature():
    while True:
        try:
            fahrenheit = float(input("Please enter the temperature in Fahrenheit: "))
            celsius = (fahrenheit - 32) * 5/9
        except ValueError:
            print("Please enter a valid number.")
        except Exception as e:
            print(f"An error occurred: {e}")
            break
        else:
            print("The temperature in Celsius is: ", celsius)
        finally:
            print("Thank you for using the temperature conversion")
            break

get_temperature()










