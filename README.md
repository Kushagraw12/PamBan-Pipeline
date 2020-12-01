# Using OpenCV and ROS to automate PamBan-Bridge
Software Architecture to automate the working of PamBan Bridge using OpenCV and ROS (Noetic).
  
## File Structure

```bash
  src
|-- CMakeLists.txt -> /opt/ros/noetic/share/catkin/cmake/toplevel.cmake
|-- launch
|   `-- final.launch              # Launch file that launches the whole pipeline
`-- perception_pipeline     
    |-- CMakeLists.txt
    |-- package.xml
    |-- soft_architecture
    |   |-- TrainSch.csv          # Sample CSV file that contains the Train Schedule
    |   `-- final_script.py       # Python script that runs the software_architecture
    `-- vision
        `-- urdf
            `-- hermes.xacro       # XACRO file that fetches model from google Colaboratory

 ```
 
 ## Installation Guide
 - Make sure you have the latest ROS Noetic verison installed and working!
 
 ``` bash
 $ git clone https://github.com/Kushagraw12/PamBan-Pipeline.git
 $ catkin_make
 $ roslaunch launch final.launch
 ```
 
 Developed by: <i>Kushagra Wadhwa</i> | [Linkedin](https://linkedin.com/in/kushagra-wadhwa12/)
 ```python
 print("Happy Coding!")
 ```
 
