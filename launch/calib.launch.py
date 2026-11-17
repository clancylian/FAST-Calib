import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

OVERRIDE_ARGS = ("bag_path", "image_path", "output_path", "lidar_topic")


def launch_setup(context, *args, **kwargs):
    pkg_share = get_package_share_directory("fast_calib")

    params = [os.path.join(pkg_share, "config", "qr_params.yaml")]
    overrides = {}
    for name in OVERRIDE_ARGS:
        value = LaunchConfiguration(name).perform(context)
        if value:
            overrides[name] = value
    if overrides:
        params.append(overrides)

    fast_calib_node = Node(
        package="fast_calib",
        executable="fast_calib",
        name="fast_calib",
        output="screen",
        parameters=params,
    )

    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="screen",
        arguments=["-d", os.path.join(pkg_share, "rviz_cfg", "fast_calib.rviz")],
        condition=IfCondition(LaunchConfiguration("rviz")),
    )

    return [fast_calib_node, rviz_node]


def generate_launch_description():
    return LaunchDescription(
        [
            DeclareLaunchArgument("rviz", default_value="true", description="是否启动 rviz2"),
            DeclareLaunchArgument("bag_path", default_value="", description="ros2 bag 目录"),
            DeclareLaunchArgument("image_path", default_value="", description="标定板图像路径"),
            DeclareLaunchArgument("output_path", default_value="", description="结果输出目录"),
            DeclareLaunchArgument("lidar_topic", default_value="", description="点云话题名"),
            OpaqueFunction(function=launch_setup),
        ]
    )
