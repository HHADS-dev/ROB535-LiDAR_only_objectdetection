# ROB535-LiDAR_only_objectdetection
Our ROB535 final project focus on comparing performance of three different 3D detection models on nuScenes dataset. The voxelnext is implemented based on OpenPCDet, the PointPillars and CenterPoint are implemented based on the mmdetection3D. All models evaluated on the validation set of nuScenes V1.0. 

1. Installation
   Follow the instruction in VoxelNext and mmdetection3D to install required environment
2. Data Preparation
   Download nuScenes dataset from official [website](https://www.nuscenes.org/download).
   Install the nuscenes-devkit with version 1.0.5 by running the following command:
   ```
   pip install nuscenes-devkit==1.0.5
   ```
  
