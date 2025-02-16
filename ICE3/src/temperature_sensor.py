import statistics

# Validate individual temperature inputs
def validate_temperature(value):
    try:
        # Try converting the value to a float
        temp = float(value)
    except ValueError:
        # If conversion fails, raise ValueError for invalid input
        raise ValueError("Invalid input detected.")

    # Check if the value is within the valid range (-50°C to 150°C)
    if temp < -50 or temp > 150:
        # If out of bounds, raise ValueError for out-of-bounds input
        raise ValueError("Out-of-bound value detected.")

    return temp


def process_temperatures(temp_list):
    # List to store valid temperature values
    valid_temps = []

    # Check if the input list is empty
    if not temp_list:
        raise ValueError("No input provided.")  # Raise error if empty list

    for temp in temp_list:
        try:
            # Validate each temperature input
            valid_temps.append(validate_temperature(temp))
        except ValueError as e:
            # Raise the exception if a ValueError is encountered
            raise e

    # Compute the minimum, maximum, and average of valid temperatures
    min_temp = min(valid_temps)
    max_temp = max(valid_temps)
    avg_temp = format(statistics.mean(valid_temps),".2f")

    # Return the formatted result
    return f"Min: {min_temp}°C, Max: {max_temp}°C, Avg: {avg_temp}°C"

#  test cases
test_cases = [
        [20],
        [15, 35],
        [],
        [10, -10, 30],
        [-50, 20, 150, 25],
        [10, "abc", 30],
        [2 ** 31 - 1, - 2 ** 31],
        [10, 10, 10],
        [10, "@", -40],
        [-51, 151],
        [55, 65, 85, 100, 102],
        [34, -12, "hh", 121],
        [75, -87],
    ]
for i, case in enumerate(test_cases, start=1):
        print(f"Test Case {i}: {case}")
        try:
            print(process_temperatures(case))
        except ValueError as e:
            print(f"Error: {e}")
        print("-" * 40)

