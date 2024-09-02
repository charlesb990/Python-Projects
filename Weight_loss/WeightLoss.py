import csv


def calculate_average_weight(gender, data, weight_field="starting_weight"):
    """Calculates the average weight for a given gender in the data.

    Args:
        gender: The gender to calculate the average weight for (F or M).
        data: The list of dictionaries containing the weight loss data.
        weight_field: The field in the dictionary to use for weight calculation (default: "starting_weight").

    Returns:
        None
    """

    # Filter data for the specified gender
    filtered_data = [participant for participant in data if participant["gender"] == gender]

    # Calculate the average weight
    if filtered_data:
        average_weight = sum(participant[weight_field] for participant in filtered_data) / len(filtered_data)
        print(f"Average {weight_field} weight for {gender}: {average_weight:.2f}")
    else:
        print(f"No participants found for gender {gender}.")


def calculate_average_weight_by_age_range(min_age, max_age, data, weight_field="starting_weight"):
    """Calculates the average weight for a given age range in the data.

    Args:
        min_age: The minimum age for the age range.
        max_age: The maximum age for the age range.
        data: The list of dictionaries containing the weight loss data.
        weight_field: The field in the dictionary to use for weight calculation (default: "starting_weight").

    Returns:
        None
    """

    # Filter data for the specified age range
    filtered_data = [participant for participant in data if min_age <= participant["age"] <= max_age]

    # Calculate the average weight
    if filtered_data:
        average_weight = sum(participant[weight_field] for participant in filtered_data) / len(filtered_data)
        print(f"Average {weight_field} weight for ages {min_age}-{max_age}: {average_weight:.2f}")
    else:
        print(f"No participants found in the age range {min_age}-{max_age}.")


def main():
    """Reads weight loss data from a CSV file and performs analysis."""

    # Path to the CSV file (replace with your actual file path)
    csv_file_path = "weight_loss_data.csv"

    try:
        # Open the CSV file in read mode
        with open(csv_file_path, "r") as csv_file:
            # Create a DictReader object to read the CSV data as dictionaries
            reader = csv.DictReader(csv_file)

            # Convert the reader object to a list of dictionaries
            data = list(reader)

            # Print the number of records
            print(f"Number of records: {len(data)}")

            # Calculate and print average starting weight for each gender
            calculate_average_weight("F", data)
            calculate_average_weight("M", data)

            # Calculate average starting weight by age range
            age_ranges = [
                (21, 30),
                (31, 40),
                (41, 50),
                (51, 60),
            ]
            for min_age, max_age in age_ranges:
                calculate_average_weight_by_age_range(min_age, max_age, data)

    except FileNotFoundError:
        print(f"Error: CSV file '{csv_file_path}' not found.")


if __name__ == "__main__":
    main()
