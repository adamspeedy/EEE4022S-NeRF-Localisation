echo "Building apt dependencies"
sudo apt-get update
sudo apt upgrade

sudo apt-get install libboost-all-dev libeigen3-dev libgflags-dev libtool libflann-dev

echo "Setup glog"
cd /
cd /notebooks/code/

# Clone source code
#git clone https://github.com/google/glog.git glog/src
cd glog/src

# Checkout v0.5.0
git checkout v0.5.0-rc2
cd ..

# make build directory
#mkdir build && cd build
cd build

# Compile project and install
sudo cmake ../src
sudo make -j8
sudo make install

echo "Setup protobuf"
cd ..
cd ..

#git clone https://github.com/protocolbuffers/protobuf.git
cd protobuf
git checkout tags/v3.14.0 -b v3.14-branch
git submodule update --init --recursive
./autogen.sh

./configure
make -j8
sudo make install
sudo ldconfig # refresh shared library cache.


echo "Setup pybind"
cd ..
#cd ~/code/

# Clone source code in your repos folder
#git clone https://github.com/pybind/pybind11.git pybind11/src
cd pybind11

# Make build directory
#mkdir build && cd build
cd build

# Compile project and install build files
sudo cmake ../src
sudo make -j8
sudo make install


echo "Setup pangolin"
# Get Pangolin
cd /
cd /notebooks/code/Pangolin
#git clone --recursive https://github.com/stevenlovegrove/Pangolin.git

# Install dependencies (as described above, or your preferred method)
./scripts/install_prerequisites.sh recommended

# Configure and build
cmake -B build
cmake --build build -j 4


echo "Install opencv"
cd ..
#cd ~/code/
# Clone opencv_contrib
git clone https://github.com/opencv/opencv_contrib
cd opencv_contrib
git checkout tags/4.1.0
cd ..

# Clone opencv
git clone https://github.com/opencv/opencv opencv/src
cd opencv/src
git checkout tags/4.1.0
cd ..

# Create build directory where the source code will be installed
#mkdir build && cd build
mkdir build
cd build

# Select path for python environment and opencv_contrib_path, thee are just examples you need to set your own
OPENCV_CONTRIB_PATH=/notebooks/code/opencv_contrib/modules

# Run the cmake command with the following flags
sudo cmake ../src -DCMAKE_BUILD_TYPE=RELEASE -DCMAKE_INSTALL_PREFIX=/usr/local -DOPENCV_EXTRA_MODULES_PATH=${OPENCV_CONTRIB_PATH} -DBUILD_opencv_python3=ON -DBUILD_opencv_xfeatures2d=ON -DOPENCV_ENABLE_NONFREE=ON -DBUILD_opencv_hdf=OFF

# Set number of cores for the installation and compile.
# This assumes you've got more than 8 cores on your pc. If you're in  doubt, use -j4
sudo make -j8
sudo make install
cd .. 
cd ..

cd aru_sil_core
cd build
cmake ..
sudo make -j8