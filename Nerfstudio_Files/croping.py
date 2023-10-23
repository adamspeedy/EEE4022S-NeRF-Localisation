import cv2
image = cv2.imread(r"C:\\Users\\adams\\Documents\\PythonStuff\\NerfStuff\\nerf\\images\\1.png")
 
#cv2.imshow("original", image)

#height, width = image.shape
y=0#image.shape[1]/2
x=0#image.shape[0]/2
print(image.shape)

h=int(image.shape[1])
w=int(image.shape[0]*9.245/10)
#temp="C:\Users\adams\Documents\PythonStuff\NerfStuff\cropped-images"+str("\'")+str(1)+".png"
for i in range(0,869,1):
    image = cv2.imread(r"C:\\Users\\adams\\Documents\\PythonStuff\\NerfStuff\\nerf\\images\\"+str(i)+".png")
   # print("C:\Users\adams\Documents\PythonStuff\NerfStuff\cropped-images\""+str(i)+".png")
    cv2.rectangle(image, (x, w), (y, h), (255, 0, 0), 2)

    crop_image = image[x:w, y:h]
    #print(print(crop_image.shape))
    #cv2.waitKey(0)
    cv2.imwrite("C:\\Users\\adams\\Documents\\PythonStuff\\NerfStuff\\cropped-images\\Crop-"+str(i)+".png", crop_image)

#cv2.imshow("Cropped", crop_image)
#cv2.waitKey(0)