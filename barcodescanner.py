import cv2
from pyzbar import pyzbar
import winsound


def scan_barcodes():
    # Initialize the video capture
    cap = cv2.VideoCapture(0)

    while True:
        # Read frame from the video capture
        ret, frame = cap.read()

        # Convert the frame to grayscale for barcode detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect and decode barcodes
        barcodes = pyzbar.decode(gray)

        # Process each detected barcode
        for barcode in barcodes:
            # Extract the barcode data
            barcode_data = barcode.data.decode("utf-8")

            # Print the scanned barcode value
            #print("Scanned Barcode:", barcode_data)

            # Play the beep sound
            winsound.Beep(1000, 200)

            # Stop the program
            cap.release()
            cv2.destroyAllWindows()
            return barcode_data

        # Display the frame
        cv2.imshow("Barcode Scanner", frame)

        # Check for key press to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture and close the window
    cap.release()
    cv2.destroyAllWindows()


# Call the scan_barcodes function

if __name__=="__main__":
    scan_barcodes()
