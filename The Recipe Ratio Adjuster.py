# Task 1: Start
# Ask the user for the number of servings the recipe is originally for and the number of servings they wish to make.
# Ensure that the user inputs are valid numbers and handle any ValueError that arises from improper input.

# Task 2: Quantity Calculation
# Calculate the adjustment factor by dividing the desired servings by the original servings.
# Use a try block to catch any arithmetic errors that may occur during the calculation.

# Task 3: Serving Success
# If the calculation is successful, display the adjusted recipe quantities to the user.

# Use a finally block to print a message encouraging the user to enjoy their cooking, regardless of the outcome of the calculation.


def get_recipe_ratio():
    while True:
        try:
            original_servings = float(input("Please enter the number of servings the recipe is originally for: "))
            desired_servings = float(input("Please enter the number of servings you wish to make: "))
            recipe_ratio = desired_servings / original_servings
        except ValueError:
            print("Please enter a valid number. Try again")
        except Exception as e:
            print(f"An error occurred: {e}")
        except ZeroDivisionError:
            print("Please enter a number greater than zero.")
            break
        else:
            print("The adjusted recipe is as follows:")
            print(f"Original servings: {original_servings}")
            print(f"Desired servings: {desired_servings}")
            print(f"Recipe ratio: {recipe_ratio}")
            print(f"Adjusted ingredients:")
            print(f"Flour: {recipe_ratio * 2} cups")
            print(f"Sugar: {recipe_ratio * 1} cups")
            print(f"Eggs: {recipe_ratio * 3}")
            print(f"Butter: {recipe_ratio * 1} cups")
            print(f"Milk: {recipe_ratio * 1} cups")
            print(f"Vanilla extract: {recipe_ratio * 1} tsp")
            print(f"Baking powder: {recipe_ratio * 1} tsp")
            print(f"Baking soda: {recipe_ratio * 1} tsp")
            print(f"Salt: {recipe_ratio * 1} tsp")
            print(f"Cinnamon: {recipe_ratio * 1} tsp")
            print(f"Chocolate chips: {recipe_ratio * 1} cups")
        finally:
            print("Enjoy your cooking!")
            break


get_recipe_ratio()








