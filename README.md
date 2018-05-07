# Vibration Feedback

 # Installation

 # mobile app

   From the git repository download https://github.com/massygaetano/progettoSofAR/blob/master/android/release/mobile-release.apk            and follow   steps at the git repository https://github.com/EmaroLab/imu_stream

  # wearable app

   Follow steps at the git repository https://github.com/EmaroLab/imu_stream, the apk is the same of mobile app, downaloaded                before
  
  # mqtt_ros_bridge
        
   Clone the repository in the source folder of your catkin workspace
   
      git clone https://github.com/massygaetano/progettoSofAR/ros/mqtt_ros_bridge.git
  
   Then follow steps at the git repository https://github.com/EmaroLab/mqtt_ros_bridge

   # Test
   
   In order to test the code:

   1. Check the Mosquitto broker status, if the broker is already active skip step 2.
      
            sudo service mosquitto status
    
   2. Start the Mosquitto broker.
       
             mosquitto
   
   3. In a new terminal tab launch the imu_bridge.

             roslaunch mqtt_ros_bridge imu_bridge.launch 
  
   4. In a new terminal tab subscribe a vibration/vel
    
             mosquitto_sub -h localhost -t "vibration/vel"
             
   5. In a new terminal tab 
            
             rostopic pub /vibration_vel std_msgs/String \"1\"
             
   # How to use vibration_feedback
  
   Follow all steps at the git repository https://github.com/EmaroLab/imu_stream 
  
  
