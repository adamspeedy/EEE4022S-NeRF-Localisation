# EEE4022S-NeRF-Localisation
This is a repository containing all the relevant code used in my final year project which looks at investigating the use of Neural Radiance Fields(NeRF) usecase in appearance based localisation.

This project has been broken doen into two main areas, firstly looking at using the [Nerfstudio](https://github.com/nerfstudio-project/nerfstudio/tree/main) frame work, and then evaluating it's performance in localisation

## NerfStudio
The relevant code here can be foud under the Nerf folder in this repository, the code mainly delas with how data is being fed into the Nerfstudio framework, from converting it into JSON file formats so that it can be used during training and then creating frames that can be rendered into a video using Nerfstudio, and finally extracting the frames from this rendured video so that the images can be used in the localisation portion of this project. A python Notebook used for evaluating the rendered frames accuracy is also included

## Localisation
This project looks using a Bag of Visual Words approach for investigating the use of NeRF images in loclaisation, this portion of code is implemented in a python notebook which can be found in the Localisation folder of this notebook. 
