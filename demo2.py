from PIL import Image
import face_recognition

image = face_recognition.load_image_file("Test7.jpg")#Change Image here to test
face_locations = face_recognition.face_locations(image)
print("Tim thay {} khuon mat trong anh.".format(len(face_locations)))

for face_location in face_locations:
    top, right, bottom, left = face_location
    print("Phat hien khuon mat tai vi tri: Top: {}, Right: {}, Bottom: {}, Left: {}".format(top,right,bottom,left))
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.show()