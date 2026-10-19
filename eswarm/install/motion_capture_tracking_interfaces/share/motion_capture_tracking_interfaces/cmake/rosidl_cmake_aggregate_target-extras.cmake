# generated from rosidl_cmake/cmake/rosidl_cmake_aggregate_target-extras.cmake.in

# Create a convenience aggregate target motion_capture_tracking_interfaces::motion_capture_tracking_interfaces
# that links all generated interface targets, so downstream packages can use
# a single modern CMake target name instead of ${motion_capture_tracking_interfaces_TARGETS}.
if(motion_capture_tracking_interfaces_TARGETS AND NOT TARGET motion_capture_tracking_interfaces::motion_capture_tracking_interfaces)
  add_library(motion_capture_tracking_interfaces::motion_capture_tracking_interfaces INTERFACE IMPORTED)
  set_target_properties(motion_capture_tracking_interfaces::motion_capture_tracking_interfaces PROPERTIES
    INTERFACE_LINK_LIBRARIES "${motion_capture_tracking_interfaces_TARGETS}")
endif()
