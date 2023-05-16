import cv2
import urllib.request
import argparse
import os
import time


# Load the pre-trained model for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def process_video_stream(video_url):
    # Open the video stream
    video_stream = urllib.request.urlopen(video_url)

    # Initialize the video capture object
    video_capture = cv2.VideoCapture()

    # Set the video source as the video stream
    video_capture.open(video_stream)

    # Create a directory to save the detected faces
    faces_dir = 'faces'
    os.makedirs(faces_dir, exist_ok=True)

    # Keep track of unique visitors
    unique_visitors = set()

    while True:
        # Read each frame of the video
        ret, frame = video_capture.read()

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

        # Process each detected face
        for (x, y, w, h) in faces:
            # Check if the face belongs to a unique visitor
            face_img = gray[y:y + h, x:x + w]
            face_hash = cv2.hash(face_img)

            if face_hash not in unique_visitors:
                # Add the face to unique visitors set
                unique_visitors.add(face_hash)

                # Save the first frame of the unique visitor
                face_filename = os.path.join(faces_dir, f"face_{face_hash}.jpg")
                cv2.imwrite(face_filename, frame)

                # Save the timestamp information
                timestamp_filename = "timestamps.txt"
                with open(timestamp_filename, "a") as timestamps_file:
                    timestamps_file.write(f"Visitor: {face_filename}\n")
                    timestamps_file.write(f"Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())}\n\n")

        # Draw rectangles around the detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Display the resulting frame
        cv2.imshow('Video', frame)

        # Exit the program when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture object and close the display window
    video_capture.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # Create a command line argument parser
    parser = argparse.ArgumentParser(description='Face detection on multiple video streams.')
    parser.add_argument('url_file', type=str, help='Path to the file containing the list of video URLs.')
    args = parser.parse_args()

    # Read the file containing the list of URLs
    url_file_path = args.url_file
    with open(url_file_path, 'r') as f:
        urls = f.read().splitlines()

    # Process each video stream URL
    for url in urls:
        print(f"Processing video stream: {url}")
        process_video_stream(url)
