execute_process(COMMAND "/home/ur3/ECE470_Project/catkin_ckyao2/build/drivers/universal_robot/ur_driver/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/ur3/ECE470_Project/catkin_ckyao2/build/drivers/universal_robot/ur_driver/catkin_generated/python_distutils_install.sh) returned error code ")
endif()