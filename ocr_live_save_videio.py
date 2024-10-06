import cv2
import easyocr
import datetime  # Import datetime to get the current time

# Initialize EasyOCR Reader
reader = easyocr.Reader(["en"])

# Open the webcam (0 for default webcam, change if you have multiple webcams)
cap = cv2.VideoCapture(0)

# Get the width and height of the video frame
frame_width = int(cap.get(3))  # Width of the frames
frame_height = int(cap.get(4))  # Height of the frames

# Get the current date and time for the filename
current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
output_filename = f'output_with_ocr_{current_time}.avi'

# Define the codec and create a VideoWriter object to save the output
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # You can also use 'MJPG', 'XVID', 'MP4V', etc.
out = cv2.VideoWriter(output_filename, fourcc, 20.0, (frame_width, frame_height))  # 20 fps

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  # Exit loop if there is an error or no frame is captured

    # Perform OCR on each frame
    ocr_results = reader.readtext(frame)
    
    # Check if OCR results are found
    if ocr_results:
        for result in ocr_results:
            top_left = tuple(map(int, result[0][0]))
            bottom_right = tuple(map(int, result[0][2]))
            text = result[1]
            
            # Draw a rectangle around the detected text
            frame = cv2.rectangle(frame, top_left, bottom_right, (0, 0, 255), 5)
            
            # Adjust the position for the text to be below the rectangle
            text_position = (top_left[0], bottom_right[1] + 30)  # Offset from bottom left of the rectangle
            
            # Put the detected text below the rectangle
            frame = cv2.putText(frame, text, text_position, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Write the processed frame to the video file
    out.write(frame)

    # Display the processed frame (whether or not text is detected)
    cv2.imshow("Live Webcam", frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and the video writer, then close all windows
cap.release()
out.release()
cv2.destroyAllWindows()

# Print the name of the saved file
print(f"Video saved as: {output_filename}")
