import time

def calc_tax(base_salary):
    """
    Calculate the tax amount for a given base salary.
    The tax rate is assumed to be 15%.
    
    Args:
    base_salary (float): The base salary amount.
    
    Returns:
    float: The calculated tax amount.
    """
    return base_salary * 0.15

def get_positive_float(prompt):
    """
    Prompt the user for a positive float value with input validation.
    
    Args:
    prompt (str): The input prompt message.
    
    Returns:
    float: A positive float value entered by the user.
    """
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    salary = get_positive_float("Enter your base salary: ")

    if input("Did you get a bonus this month? (yes/y to confirm): ").strip().lower() in ["yes", "y"]:
        bonus = get_positive_float("How much bonus did you get? ")
        salary += bonus

    final_salary = salary - calc_tax(salary)

    time.sleep(3)
    print("Calculating your total salary... please wait")

    time.sleep(2)
    print("Finding the tax amount in Morocco... please wait")

    time.sleep(2)
    print(f"Final Salary after tax: ${final_salary:.2f}")

if __name__ == "__main__":
    main()
