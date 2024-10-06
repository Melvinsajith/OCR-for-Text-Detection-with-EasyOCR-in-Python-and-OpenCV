import cv2
import easyocr
import time  # Import time to handle delays

# Initialize EasyOCR Reader
reader = easyocr.Reader(["en"])

# Open the webcam (0 for default webcam, change if you have multiple webcams)
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  # Exit loop if there is an error or no frame is captured

    # Perform OCR on each frame
    ocr_results = reader.readtext(frame)
    
    # Check if OCR results are found, and only then apply a 1 second delay
    if ocr_results:
        for result in ocr_results:
            top_left = tuple(map(int, result[0][0]))
            bottom_right = tuple(map(int, result[0][2]))
            text = result[1]
            
            # Draw a rectangle around the detected text
            frame = cv2.rectangle(frame, top_left, bottom_right, (0, 0, 255), 5)
            # Put the detected text above the rectangle
            frame = cv2.putText(frame, text, top_left, cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)

        # Display the processed video frame with detection
        cv2.imshow("Live Webcam", frame)
        
        # Wait for 1 second before proceeding to the next frame
    else:
        # Display the frame without detection (in case no text is found)
        cv2.imshow("Live Webcam", frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()
