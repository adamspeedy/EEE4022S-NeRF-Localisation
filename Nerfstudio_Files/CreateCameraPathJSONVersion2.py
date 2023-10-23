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

#matrix used to flip trakectories
matrixB=[[1, 1, -1, 1],
[1, 1, -1 ,1],
[1, 1, -1, 1],
[1, 1, 1, 1]]

#Uncropped
#matrixC=[[0.9983559250831604, 0.04119092971086502, 0.039859019219875336],      
#[0.04119092971086502, -0.03200852870941162, -0.9986384510993958],
#[-0.039859019219875336, 0.9986384510993958, -0.033652544021606445]]

#Cropped
#matrixC=[[0.998359203338623, 0.041146595031023026, 0.03982341289520264],      
#[0.041146595031023026, -0.03182721138000488, -0.998646080493927],
#[-0.03982341289520264, 0.998646080493927, -0.03346812725067139]]

#Sampled
matrixC=[[0.9983800649642944, 0.04088367894291878, 0.039569783955812454],      
[0.04088367894291878, -0.031817078590393066, -0.9986572265625],
[-0.039569783955812454, 0.9986572265625, -0.03343701362609863]]

dict = {}

#this is just temporary, setting keyframes to random values
dict["keyframes"]=[]
count=0
numkeyframes=869
time=60
#this will just change depending on how many keyframes you want
#for i in range(0,869,int(869/numkeyframes)):
for i in range(0,869,1):
    Templine=[]
    matrixTemp=[]
    dict3={}
    dict3["matrix"]=[]
    filename=str(i)+".txt"
    # This is just to change the camera view to the correct orientation
    with open(filename) as fh:
        for line in fh:
            lineString =line.split()
            #print(lineString)
            #print(lineString[1])
            temp=[]
            for part in lineString:
                temp.append(float(part))
            Templine.append(temp)
        matrixTemp.append(Templine)
    #print(matrixA)
   # matrixResult=np.matmul(matrixB,matrixA)
    #Now we actually add these numbers to the dictionary
    matrixResult=np.multiply(matrixB,matrixTemp)
    matrixResult=matrixResult[0]
    #print(matrixResult)
    
    temporary=[[0,0,0],[0,0,0],[0,0,0]]
    temporary=np.array(temporary)

    #for r in range(0, 3):
       # for c in range(0, 3):
        #   temporary[r,c] = matrixResult[r,c]
    temporary   = matrixResult[:3, :4]
    print(matrixResult)
    print(temporary)

    temporary=np.matmul(matrixC,temporary)
    #translation= np.array([[0.3622832298278815],  [0.7548952102661125], [-0.02299022488296039]])
    #translation= np.array([[2.792297601699829+matrixResult[0,3]],  [5.829122066497803+matrixResult[1,3]], [-0.18725623190402985+matrixResult[2,3]]])
    #translation= np.array([[(2.792297601699829+matrixResult[0,3])*0.13073409322342158],  [(5.829122066497803+matrixResult[1,3])*0.13073409322342158], [(-0.18725623190402985+matrixResult[2,3])*0.13073409322342158]])
    #translation= np.array([[(1-0.13073409322342158)/-10*matrixResult[0,3]],  [(1-0.13073409322342158)/-10+matrixResult[1,3]], [(1-0.13073409322342158)/-10+matrixResult[2,3]]])
   # temporary = np.append(temporary, translation, axis=1)
    fourthRow =np.array([0,0,0,1])


    temporary[0,3]=(temporary[0,3]+2.793013095855713)*0.13014844225095432
    temporary[1,3]=(temporary[1,3]+5.794294834136963)*0.13014844225095432
    temporary[2,3]=(temporary[2,3]+-0.18730394542217255)*0.13014844225095432

    row_n = temporary.shape[0] 
    temporary = np.insert(temporary,row_n,[fourthRow],axis= 0)
    print(temporary)
    matrixResult=temporary
    tempString=""
    first=True
    for k in range(4):    
        for i in range(4): #matrixResult[0]:
            if(first):
                tempString=tempString+str((matrixResult[k]).tolist()[i])
                first=False
            else:
                tempString=tempString+","+str((matrixResult[k]).tolist()[i])
            #print(tempString)
    dict3["matrix"].append(str(tempString))
    #dict2["camera_to_world"].append(temp)
    dict["keyframes"].append(dict3)
    dict3["fov"]= 64.09336
    #dict3["scale"]=5
    dict3["aspect"]=1
    dict3["properties"]="[[\"FOV\","+str(64.09336)+"],[\"NAME\",\"Camera "+str(count)+"\"],[\"TIME\","+str(count*time/numkeyframes)+"]]"
    count+=1

#adding all of the camera intrinsics, please come back and give some propper ones
dict["camera_type"]="perspective"
dict["render_height"]= 665
dict["render_width"]= 1280
dict["camera_path"]=[]

#flipping the transformation matrix

#take note of how many frames you want and fps
for i in range(0,869,1):
    Templine=[]
    matrixA=[]
    dict2={}
    dict2["camera_to_world"]=[]
    filename=str(i)+".txt"

    # This is just to change the camera view to the correct orientation
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

   #Now we actually add these numbers to the dictionary
    matrixResult=np.multiply(matrixB,matrixA)
    matrixResult=matrixResult[0]

    #print(matrixResult)
    
    temporary=[[0,0,0],[0,0,0],[0,0,0]]
    temporary=np.array(temporary)

    #for r in range(0, 3):
    #    for c in range(0, 3):
    #       temporary[r,c] = matrixResult[r,c]
    temporary   = matrixResult[:3, :4]

    temporary=np.matmul(matrixC,temporary)
    #translation= np.array([[(+2.792297601699829+matrixResult[0,3])*0.13073409322342158],  [(5.829122066497803+matrixResult[1,3])*0.13073409322342158], [(-0.18725623190402985+matrixResult[2,3])*0.13073409322342158]])
    #translation= np.array([[(1-0.13073409322342158)/-10*matrixResult[0,3]],  [(1-0.13073409322342158)/-10+matrixResult[1,3]], [(1+0.13073409322342158)/-10+matrixResult[2,3]]])
   # temporary = np.append(temporary, translation, axis=1)
    fourthRow =np.array([0,0,0,1])

    row_n = temporary.shape[0] 
    temporary = np.insert(temporary,row_n,[fourthRow],axis= 0)

    #Uncropped
    #temporary[0,3]=(temporary[0,3]+2.792297601699829)*0.13073409322342158
    #temporary[1,3]=(temporary[1,3]+5.829122066497803)*0.13073409322342158
    #temporary[2,3]=(temporary[2,3]+-0.18725623190402985)*0.13073409322342158

    #cropped and instant-ngp
    #temporary[0,3]=(temporary[0,3]+2.7989635467529297)*0.1302514646172108
    #temporary[1,3]=(temporary[1,3]+5.800684928894043)*0.1302514646172108
    #temporary[2,3]=(temporary[2,3]+-0.18986894190311432)*0.1302514646172108

     #sampled 5 cropped
    temporary[0,3]=(temporary[0,3]+2.793013095855713)*0.13014844225095432
    temporary[1,3]=(temporary[1,3]+5.794294834136963)*0.13014844225095432
    temporary[2,3]=(temporary[2,3]+-0.18730394542217255)*0.13014844225095432

   
    matrixResult=temporary

    #print(matrixResult[0])
    for k in range(4):    
        for i in range(4): #matrixResult[0]:
            dict2["camera_to_world"].append((matrixResult[k]).tolist()[i])
    #dict2["camera_to_world"].append(temp)
    dict["camera_path"].append(dict2)
    dict2["fov"]= 64.09336
    dict2["aspect"]= 1
    dict2["scale"]=5
    
    dict["fps"] = 14.5
    dict["seconds"]= 60
    dict["smoothness_value"]= 0.5
    dict["is_cycle"]=bool(True == 'false')
    dict["crop"] = None
    #print(dict) 


# creating json file
# the JSON file is named as test1
out_file = open("fov_testing_camera_path.json", "w")
json.dump(dict, out_file, indent = 4, sort_keys = False)
out_file.close()
