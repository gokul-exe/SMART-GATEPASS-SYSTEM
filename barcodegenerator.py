import os
import barcode
from barcode.writer import ImageWriter
import csv

# Read the roll numbers from the CSV file
roll_numbers = []
with open('data.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        roll_numbers.append(row['Roll Number'])

# Create the 'barcodes' directory if it doesn't exist
if not os.path.exists('barcodes'):
    os.makedirs('barcodes')

# Generate barcodes for each roll number
for roll_number in roll_numbers:
    barcode.generate('code128', roll_number, output='barcodes/' + roll_number, writer=ImageWriter())

print('Barcodes generated successfully.')



