# To Capture Frame
import cv2

# To process image array
import numpy as np


# import the tensorflow modules and load the model
import tensorflow as tf
model = tf.keras.models.load_model("PRO-C110-Project-Boilerplate-main/keras_model.h5")

# Attaching Cam indexed as 0, with the application software
camera = cv2.VideoCapture(0)

# Infinite loop
while True:

	# Reading / Requesting a Frame from the Camera 
	status , frame = camera.read()

	# if we were sucessfully able to read the frame
	if status:

		# Flip the frame
		frame = cv2.flip(frame , 1)
		
		
		
		#resize the frame
		img = cv2.resize (frame, (224, 224))
		# expand the dimensions
		test_img = np.expand_dims(img, axis=0)
		# normalize it before feeding to the model
		normalised_img = test_img/255.0
		# get predictions from the model
		prediction = model.predict(normalised_img)
		print("rock :",prediction[0][0]," paper:",prediction[0][1]," scissor:",prediction[0][2])
		
		# displaying the frames captured
		cv2.imshow('feed' , frame)

		# waiting for 1ms
		code = cv2.waitKey(1)
		
		# if space key is pressed, break the loop
		if code == 32:
			break

# release the camera from the application software
camera.release()

# close the open window
cv2.destroyAllWindows()
