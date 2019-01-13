import face_recognition
#Load Image

#--DataTest
#image = face_recognition.load_image_file("MyTeam.jpg")
#image = face_recognition.load_image_file("HinhTest.jpg")
image = face_recognition.load_image_file("HinhTest2.jpg")
#Location of Image
face_locations = face_recognition.face_locations(image)
#print
print("Da tim thay {} Doi tuong trong anh.".format(len(face_locations)))
