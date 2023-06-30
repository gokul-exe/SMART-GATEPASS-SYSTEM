import time
import threading
from mail import mail

active_timers = {}  # Dictionary to keep track of active timers
lock = threading.Lock()  # Lock for synchronizing timer operations

def timer_function(barcode, name, dept):
    duration = 1800  # Timer duration in seconds
    print(f"Timer started for '{barcode}'")

    start_time = time.time()
    end_time = start_time + duration

    # Check cancellation flag in each iteration
    while time.time() < end_time and not active_timers[barcode]['cancelled']:
        remaining = int(end_time - time.time())
        minutes = remaining // 60
        seconds = remaining % 60
        #timer_display = f"{minutes:02d}:{seconds:02d}"

        # Update the timer display in a single place
        # print(f"Timer for '{barcode}': {timer_display}")
        time.sleep(1)

    if not active_timers[barcode]['cancelled']:
        print(f"Timer completed for '{barcode}'")
        send_mail(barcode, name, dept)  # Call the send_mail function after the timer completes

    with lock:
        del active_timers[barcode]  # Remove the timer from the active timers dictionary

def send_mail(barcode, name, dept):
    # Implement your mail sending logic here
    message = "This mail is to inform that "+name+" of "+dept+ " Didnt return even After the lunch is over"
    mail(message)
    print(f"Mail sent for '{barcode}'")

def start_timer(barcode, name, dept):
    with lock:
        if barcode in active_timers:
            print(f"Cancelling timer for '{barcode}'")
            active_timers[barcode]['cancelled'] = True  # Mark the timer for cancellation

        if barcode not in active_timers:
            active_timers[barcode] = {'cancelled': False}  # Initialize the cancellation flag
            timer_thread = threading.Thread(target=timer_function, args=(barcode, name, dept,))
            timer_thread.start()
        else:
            print(f"Timer for '{barcode}' is already active")

if __name__ == "__main__":
    # Example usage
    start_timer("19TH0483", "John Doe", "Department A")
    time.sleep(2)  # Wait for some time
    start_timer("19TH0483", "Jane Smith", "Department B")
