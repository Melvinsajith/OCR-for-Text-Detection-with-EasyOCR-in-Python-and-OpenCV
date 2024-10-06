import cv2
import easyocr
import time  # Import time to handle delays

# Initialize EasyOCR Reader
reader = easyocr.Reader(["en"])

# Open the video file (or 0 for webcam)
cap = cv2.VideoCapture("C:\\Users\\USER\\Pictures\\cv_pro\ocr\\sample.mp4")  # Replace with your video file path or 0 for webcam

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  # Exit loop if video ends or there is an error

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
        cv2.imshow("Video", frame)
        
        # Wait for 1 second before proceeding to the next frame

    # Display the processed frame (if no text detected, it will show the frame without any rectangle or text)
    cv2.imshow("Video", frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close windows
cap.release()
cv2.destroyAllWindows()
