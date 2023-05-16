import cv2
import os

# Load the pre-trained model for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize the video capture
video_capture = cv2.VideoCapture(0)  # Set the argument to the video file path if you want to detect faces in a video file

# Create a directory to save the detected faces
output_dir = 'detected_faces'
os.makedirs(output_dir, exist_ok=True)

# Initialize a counter for the face images
face_counter = 0

while True:
    # Read each frame of the video
    ret, frame = video_capture.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around the detected faces and save each face as a separate image file
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Save the detected face as an image file
        face_img = frame[y:y+h, x:x+w]
        face_filename = os.path.join(output_dir, f"face_{face_counter}.jpg")
        cv2.imwrite(face_filename, face_img)
        face_counter += 1

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Exit the program when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close the display window
video_capture.release()
cv2.destroyAllWindows()
