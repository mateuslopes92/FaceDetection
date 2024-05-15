import json
from deepface import DeepFace

result = DeepFace.verify(img1_path="me1.jpeg", img2_path="me2.jpeg")

print(json.dumps(result, indent=2))