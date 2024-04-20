import random
import faker
from openpyxl import Workbook
import re

# Initialize Faker to generate fake data
fake = faker.Faker('en_GB')

# Function to generate random date of birth
def generate_dob():
    return fake.date_of_birth(minimum_age=10, maximum_age=90)

# Function to generate random sex
def generate_gender():
    return random.choice(['Male', 'Female','Other'])

# Function to generate random address
def generate_address():
    address = fake.address().split('\n')
    # Ensure address has at least 4 lines
    while len(address) < 4:
        address.append('')
    return address[:4]

# Function to remove postcode from address
def remove_postcode(address):
   return re.sub(r'\b[A-Z]{1,2}[0-9R][0-9A-Z]? [0-9][ABD-HJLNP-UW-Z]{2}\b', '', address) if address else ''

# Function to generate random postcode
def generate_postcode():
    return fake.postcode()

# Function to generate random phone number
def generate_phone_number():
    return fake.phone_number()

# Function to generate random email
def generate_email(first_name, last_name):
    domain = random.choice(['gmail.com', 'live.com'])
    return f"{first_name.lower()}.{last_name.lower()}@{domain}"

# Function to remove honorifics from name
def remove_honorifics(name):
    return re.sub(r'\b(Mr|Dr|Ms|Mrs)\.?\b', '', name)

# Create Excel workbook
wb = Workbook()
ws = wb.active

# Define headers
headers = ['First Name', 'Last Name', 'Date of Birth', 'Gender', 'Address Line 1', 'Address Line 2', 'Address Line 3', 'Address Line 4', 'Postcode', 'Phone Number', 'Email']
ws.append(headers)

# Generate sample data
for _ in range(10000):
    full_name = remove_honorifics(fake.name()).split()
    first_name = full_name[0]
    last_name = " ".join(full_name[1:])
    dob = generate_dob()
    gender = generate_gender()
    address_lines = generate_address()
    postcode = generate_postcode()
    phone_number = generate_phone_number()
    email = generate_email(first_name, last_name)
    address_lines = [remove_postcode(line) for line in address_lines]
    row = [first_name, last_name, dob, gender] + address_lines + [postcode, phone_number, email]
    print(row)
    ws.append(row)

# Save the workbook
wb.save("sample_data.xlsx")

print("Sample data has been generated and saved to sample_data.xlsx")
