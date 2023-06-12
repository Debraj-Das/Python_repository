# it is intiallsed correctly for this virtual environment

import re


s = "My phone number is 408-555-1234 \
    and my friend phone number is 4085554321 \
        and my other friend phone number is (408)-5551111 \
            and my other friend phone number is 408455-2222 "

pattern = r"\d{10}|\(?\d{3}\)?-?\d{3}-?\d{4}"

phone_numbers = re.findall(pattern, s)

for phone in phone_numbers:
    print(phone)
