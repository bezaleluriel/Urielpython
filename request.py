import requests
import re
import csv

# x = requests.get('http://www.google.com')
# print(x.status_code)
# print(x.text)

# find all 08-xxxxxxx phones from site to csv
x = requests.get('https://www.rehovot.muni.il/phonebook/').text
phone_pattern = "08-\d{7}"
# set to avoid duplicates
phones = set(re.findall(phone_pattern, x))
# Write the phone numbers to a CSV file
with open("phones.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    for phone_number in phones:
        writer.writerow([phone_number])



