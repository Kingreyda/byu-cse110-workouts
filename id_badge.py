print()
print("Please enter the following information: ")
print()

first_name = input("First Name: ")
last_name = input("Last Name: ")
email_address = input("Email address: ")
phone_number = input("Phone number: ")
job_title = input("Job title: ")
id_number = input("ID number: ")

print("\nThe ID Card is: ")
print("-----------------------")
print(f"{last_name.upper()}, {first_name.capitalize()}")
print(f"Job Title: {job_title.title()}")
print(f"ID Number: {id_number}")


print(f"\nEmail Address: {email_address.lower()}")
print(f"Phone Number: {phone_number:.10f}")
print("-----------------------")
