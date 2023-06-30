import asyncio
import csv
from datetime import datetime
from functools import partial
from barcodescanner import scan_barcodes
from searchdata import binary_search_data
from timer import start_timer
from mail import mail

async def main():
    welcome()
    while True:
        barcode = await asyncio.to_thread(scan_barcodes)
        asyncio.create_task(process_barcode(barcode))

def welcome():
    print("WELCOME TO STUDENTS SMART GATEPASS SYSTEM")

async def process_barcode(barcode):
    roll_number, name, dept,staff= await search_details(barcode)
    await asyncio.to_thread(start_timer, roll_number, name, dept)
    message = "This mail is to inform that "+name+" of "+dept+ " Gone Out Of the College "
    mail(message)
    await save_data(name, dept,staff)

async def search_details(barcode):
    print("Scanned barcode:", barcode)
    data = await asyncio.to_thread(partial(binary_search_data, barcode))
    return data["Roll Number"], data["Name"], data["Department"],data["Staff"]

async def save_data(name, dept,staff):
    now = datetime.now() 
    timestamp = now.strftime("%I:%M:%S")   
    day = now.strftime("%A")
    year = now.strftime("%Y")
    month = now.strftime("%B")
    
    data = [name, dept, staff," At ",timestamp,  day+"-"+month+"-"+year]
    
    with open("student_data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(data)

# Start the main event loop
asyncio.run(main())
