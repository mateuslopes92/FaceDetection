# import json
# from deepface import DeepFace
import cv2
import face_recognition
import numpy as np

#DeepFace test
# result = DeepFace.verify(img1_path="me1.jpeg", img2_path="me2.jpeg")
# print(json.dumps(result, indent=2))

image_path = 'holding2.jpeg'
image = cv2.imread(image_path)

# Convert the image from BGR (OpenCV format) to RGB (face_recognition format)
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Detect all faces in the image
face_locations = face_recognition.face_locations(rgb_image)

# Ensure that at least two faces are detected
if len(face_locations) >= 2:
    # Assume the first detected face is the person's face and the second is the document's face
    person_face_location = face_locations[0]
    document_face_location = face_locations[1]

    # Extract the faces
    person_face_image = rgb_image[person_face_location[0]:person_face_location[2], person_face_location[3]:person_face_location[1]]
    document_face_image = rgb_image[document_face_location[0]:document_face_location[2], document_face_location[3]:document_face_location[1]]

    # Get the face encodings
    person_face_encoding = face_recognition.face_encodings(rgb_image, [person_face_location])
    document_face_encoding = face_recognition.face_encodings(rgb_image, [document_face_location])

    if person_face_encoding and document_face_encoding:
        # Compare the faces
        results = face_recognition.compare_faces([person_face_encoding[0]], document_face_encoding[0])
        face_distance_value = face_recognition.face_distance([person_face_encoding[0]], document_face_encoding[0])[0]

        # Check if the faces match
        if results[0]:
            print("The faces match.")
        else:
            print("The faces do not match.")

        print(f"Face distance: {face_distance_value}")
    else:
        print("Could not encode one or both faces.")
else:
    raise ValueError("Could not detect both faces in the image.")