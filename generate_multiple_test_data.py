import json
from faker import Faker

# Initialize Faker for random data generation
faker = Faker()

# Function to generate test data for each placeholder
def generate_test_data(template):
    if isinstance(template, dict):  # If template is a dictionary
        return {key: generate_test_data(value) for key, value in template.items()}
    elif isinstance(template, list):  # If template is a list
        # Generate 3 test data items for the list (you can adjust the number)
        return [generate_test_data(template[0]) for _ in range(1)]
    elif isinstance(template, str):  # If template is a string (e.g., placeholder name)
        # Replace placeholder with generated data
        if template == "name":
            return faker.name()
        elif template == "age":
            return faker.random_int(min=18, max=65)
        elif template == "email":
            return faker.email()
        elif template == "street":
            return faker.street_address()
        elif template == "city":
            return faker.city()
        elif template == "postalCode":
            return faker.postcode()
        elif template == "skills":
            # Generate a list of random skills (e.g., 3 skills)
            return [faker.job() for _ in range(3)]
        else:
            return template  # Return the template as-is if it's not recognized
    else:
        return template  # Return the value as-is for unhandled types

# Function to generate multiple examples based on the input template
def generate_multiple_examples(template, count=5):
    # Create a list of generated data examples
    return [generate_test_data(template) for _ in range(count)]

# Main Execution
def main():
    # Read the input template JSON file
    with open("input.json", "r") as f:
        input_template = json.load(f)

    # Generate multiple test data examples (default is 5)
    test_data = generate_multiple_examples(input_template, count=5)

    # Save the generated test data to an output file
    with open("test_data.json", "w") as f:
        json.dump(test_data, f, indent=4)

    print("Test data generated and saved to 'test_data.json'.")

# Run the script
if __name__ == "__main__":
    main()
