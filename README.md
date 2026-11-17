# FAST-Calib

## FAST-Calib: LiDAR-Camera Extrinsic Calibration in One Second

FAST-Calib is an efficient target-based extrinsic calibration tool for LiDAR-camera systems (eg., [FAST-LIVO2](https://github.com/hku-mars/FAST-LIVO2)). 

**Key highlights include:** 

1. Support solid-state and mechanical LiDAR.
2. No need for any initial extrinsic parameters.
3. Achieve highly accurate calibration results **in just one seconds**.

In short, it makes extrinsic calibration as simple as intrinsic calibration.

**Related paper:** 

[FAST-Calib: LiDAR-Camera Extrinsic Calibration in One Second](https://www.arxiv.org/pdf/2507.17210)

📬 For further assistance or inquiries, please feel free to contact Chunran Zheng at zhengcr@connect.hku.hk.

<p align="center">
  <img src="./pics/calib.jpg" width="100%">
  <font color=#a0a0a0 size=2>Left: Example of Mid360 LiDAR calibration. Right: Point cloud colored with the calibrated extrinsics.</font>
</p>

<p align="center">
  <img src="./pics/all_lidar_type.jpg" width="100%">
  <font color=#a0a0a0 size=2>Circular hole extraction supports multiple LiDAR models.</font>
</p>

## 1. Prerequisites
ROS 2 Humble, PCL>=1.8, OpenCV>=4.0, `livox_ros_driver2` (for `livox_ros_driver2/msg/CustomMsg`).

Build this package as a colcon package:

```bash
cd /home/ztl/PointPanoramaTex/lidar_cam_extr_calib
./build.sh
```

## 2. Run our examples
1. Prepare the static acquisition data in the `calib_data` folder (ROS 2 bag directories recorded by `ros2 bag record -o <dir> <topic>`, plus the corresponding image):
- ros2 bag containing point cloud messages (ROS 1 `.bag` files cannot be read by rosbag2)
- corresponding image

2. Run the single-scene calibration process:
```bash
ros2 launch fast_calib calib.launch.py bag_path:=/abs/path/to/bag_dir image_path:=/abs/path/to/image.png
```

3. After completing Step 2 for at least three different scenes, you can perform multi-scene joint calibration:
```bash
ros2 launch fast_calib multi_calib.launch.py
```

## 3. Run on your own sensor suite
1. Customize the calibration target in the image below, with the CAD model available [here](https://drive.google.com/file/d/1hdC8xGCHNP47a-wSLPyjr_tpOeynNFEG/view?usp=sharing).
2. Collect data from three scenes, with placement illustrated below, and record them into the corresponding ros2 bags.
3. Provide the instrinsic matrix in `qr_params.yaml` (ROS 2 parameter file: `/**/ros__parameters:`).
4. Set distance filter in `qr_params.yaml` for board point cloud (extra points are acceptable).
5. Calibrate now!

💡 **Note:** You can run `scripts/distance_filter_tool.py` to quickly obtain suitable filter parameters.
<p align="center">
  <img src="./pics/calibration_target.jpg" width="100%">
  <font color=#a0a0a0 size=2>Left: Actual calibration target | Right: Technical drawing with annotated dimensions.</font>
</p>
<p align="center">
  <img src="./pics/multi-scene.jpg" width="100%">
  <font color=#a0a0a0 size=2>Placement of the calibration target for multi-scene data collection: (a) facing forward, (b) oriented to the right, (c) oriented to the left.</font>
</p>

## 4. Appendix
The calibration target design is based on the [velo2cam_calibration](https://github.com/beltransen/velo2cam_calibration).

For further details on the algorithm workflow, see [this document](https://github.com/xuankuzcr/FAST-Calib/blob/main/workflow.md).
## 5. Acknowledgments

Special thanks to [Jiaming Xu](https://github.com/Xujiaming1) for his support, [Haotian Li](https://github.com/luo-xue) for the equipment, and the [velo2cam_calibration](https://github.com/beltransen/velo2cam_calibration) algorithm.
