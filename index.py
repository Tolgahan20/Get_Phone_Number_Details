import phonenumbers
from phonenumbers import carrier, geocoder, timezone


mobileNo = input("Enter Mobile Number with Country Code: ")
mobileNo = phonenumbers.parse(mobileNo)

# getting the timezone of the phone number
print(timezone.time_zones_for_number(mobileNo))

# Getting the carrier of the phone number
print(carrier.name_for_number(mobileNo, "en"))

# Getting the region information
print(geocoder.description_for_number(mobileNo, "en"))

# Validating the phone number
print("Valid Phone Number: ", phonenumbers.is_valid_number(mobileNo))

# Checking Possibility of phone number
print("Checking Possibility of the Number: ",
      phonenumbers.is_possible_number(mobileNo))
