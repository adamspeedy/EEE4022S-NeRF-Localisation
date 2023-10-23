# Python program to convert text files with transform matrices 
#to JSON file of camera trajectories for nerfstudio

import json
import numpy as np

#the below is just to check if i can open the txt file
filename = "1.txt"
try:
    file1 = open("1.txt", "r")
    #read_content = file1.read()
    #print(read_content)
    print("txt File Exists")

finally:
    # close the file
    file1.close()

dict = {}
#adding all of the camera intrinsics, please come back and give some propper ones
dict["camera_model"]="OPENCV"
dict["fl_x"]= 531.14774
dict["fl_y"]= 531.26312
dict["k1"]= 0
dict["k2"]= 0
dict["k3"]= 0
dict["k4"]= 0
dict["p1"]= 0
dict["p2"]= 0
dict["cx"]= 637.87114

#make sure to comment this out if using normal images
dict["cy"]= 331.27469 #*0.9245

dict["w"]= 1280.0

#used for normal image
#dict["h"]= 720.0
#used for cropped imagee
dict["h"]= 665

dict["frames"]=[]

#flipping the transformation matrix

matrixB=[[1, 1, -1, 1],
[1, 1, -1 ,1],
[1, 1, -1, 1],
[1, 1, 1, 1]]

for i in range(0,869,5):
    Templine=[]
    matrixA=[]
    dict2={}

    #Used for normal images
    #dict2["file_path"]="./images/"+str(i)+".png"
    #used for cropped images
    dict2["file_path"]="./images/Crop-"+str(i)+".png"

    dict2["transform_matrix"]=[]
    filename=str(i)+".txt"
    # creating dictionary
    with open(filename) as fh:
        for line in fh:
            lineString =line.split()
            #print(lineString)
            #print(lineString[1])
            temp=[]
            for part in lineString:
                temp.append(float(part))
            Templine.append(temp)
        matrixA.append(Templine)
    #print(matrixA)
   # matrixResult=np.matmul(matrixB,matrixA)
    matrixResult=np.multiply(matrixB,matrixA)
    matrixResult=matrixResult[0]
    print(matrixResult[0])
    for k in range(4):
        temp=[]
        for i in range(4): #matrixResult[0]:
            temp.append((matrixResult[k]).tolist()[i])
        dict2["transform_matrix"].append(temp)
    dict["frames"].append(dict2)
    #print(dict) 



#the below is used for the normal converting txt files to json
"""
for i in range(0,180,5):
    dict2={}
    #if(i<10):
    dict2["file_path"]="./images/"+str(i)+".png"
    #else:
        #dict2["file_path"]="./images/frame_000"+str(i)+".png"
    dict2["transform_matrix"]=[]
    filename=str(i)+".txt"
    # creating dictionary
    with open(filename) as fh:
        for line in fh:
            #command, description = line.strip().split(None, 1)
            lineString =line.split()
            temp=[]
            for part in lineString:
                temp.append(float(part))
            dict2["transform_matrix"].append(temp)
    dict["frames"].append(dict2)
    print(dict)      
"""



# creating json file
# the JSON file is named as test1

out_file = open("transforms.json", "w")
json.dump(dict, out_file, indent = 4, sort_keys = False)
out_file.close()

"""

new_frame = {
    "file_path": "./images/frame_00001.png",
    "transform_matrix": [
        [-0.19613579881043192, -0.979508275070439, -0.04576338594910703, 0.15754341819475415],
        [-0.006700502856020352, -0.04532999724303263, 0.9989495956310421, 3.0904304752630085],
        [-0.9805538494577797, 0.1962364146087056, 0.002327637224731808, 0.8096105650076095],
        [0.0, 0.0, 0.0, 1.0]
    ]
}

# Check if the JSON file already exists
try:
    with open("test1.json", 'r') as json_file:
        data = json.load(json_file)
except FileNotFoundError:
    # If the file doesn't exist, initialize an empty dictionary
    data = {}

# Check if "frames" key exists, if not, create it as an empty list
if "frames" not in data:
    data["frames"] = []

# Append the new_frame to the "frames" list
data["frames"].append(new_frame)

# Write the updated data back to the JSON file
with open("test1.json", 'w') as json_file:
    json.dump(data, json_file, indent=4)
    
"""