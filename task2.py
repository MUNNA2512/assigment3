import math

def calculate_math_operations():
    try:
        number = float(input("Enter a number: "))
        
        # Calculate square root
        sqrt_result = math.sqrt(number)
        
        # Calculate natural logarithm
        log_result = math.log(number)
        
        # Calculate sine (assuming input is in radians)
        sin_result = math.sin(number)
        
        print(f"\nResults for number: {number}")
        print(f"Square root: {sqrt_result:.4f}")
        print(f"Natural logarithm: {log_result:.4f}")
        print(f"Sine: {sin_result:.4f}")
        
    except ValueError:
        print("Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    calculate_math_operations()