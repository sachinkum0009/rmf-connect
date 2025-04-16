from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    start_turtlebot4_ignition_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            FindPackageShare('turtlebot4_ignition_bringup'),
            '/launch/turtlebot4_ignition.launch.py'
        ])
    )

    return LaunchDescription([
        start_turtlebot4_ignition_cmd,
    ])
