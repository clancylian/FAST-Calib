cmake_minimum_required(VERSION 3.8)
project(fast_calib)

if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Release)
endif()
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
add_compile_options(-O3)

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(pcl_conversions REQUIRED)
find_package(rosbag2_cpp REQUIRED)
find_package(rosbag2_storage REQUIRED)
find_package(livox_ros_driver2 REQUIRED)
find_package(PCL REQUIRED)
find_package(OpenCV REQUIRED)
find_package(Eigen3 REQUIRED)

include_directories(
  include
  ${PCL_INCLUDE_DIRS}
  ${OpenCV_INCLUDE_DIRS}
  ${EIGEN3_INCLUDE_DIR}
  ${livox_ros_driver2_INCLUDE_DIRS}
)

add_executable(fast_calib src/main.cpp)
ament_target_dependencies(fast_calib
  rclcpp
  sensor_msgs
  pcl_conversions
  rosbag2_cpp
  rosbag2_storage
)
target_link_libraries(fast_calib
  ${PCL_LIBRARIES}
  ${OpenCV_LIBS}
  livox_ros_driver2::livox_interfaces2__rosidl_typesupport_cpp
)

add_executable(multi_fast_calib src/multi_scene.cpp)
ament_target_dependencies(multi_fast_calib
  rclcpp
  sensor_msgs
  pcl_conversions
  rosbag2_cpp
  rosbag2_storage
)
target_link_libraries(multi_fast_calib
  ${PCL_LIBRARIES}
  ${OpenCV_LIBS}
  livox_ros_driver2::livox_interfaces2__rosidl_typesupport_cpp
)

install(TARGETS fast_calib multi_fast_calib
  DESTINATION lib/${PROJECT_NAME}
)

install(DIRECTORY launch config rviz_cfg
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
