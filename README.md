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
   For OpenPCDet
   ```
   python -m pcdet.datasets.nuscenes.nuscenes_dataset --func create_nuscenes_infos \
    --cfg_file tools/cfgs/dataset_configs/nuscenes_dataset.yaml \
    --version v1.0-trainval
   ```
   For mmdetection3D
   ```
   python tools/create_data.py nuscenes --root-path ./data/nuscenes --out-dir ./data/nuscenes --extra-tag nuscenes
   ```
3. Download pretrained weight from official repo
4. Run evaluate python file
   For VoxelNext
   ```
   bash VoxelNeXt/tools/scripts/dist_test.sh 4 --cfg_file VoxelNeXt/tools/cfgs/nuscenes_models/cbgs_voxel0075_voxelnext.yaml --ckpt path/to/pretain_model
   ```
   For CenterPoint and PointPillar
   ```
   CONFIG_FILE=mmdetection3d/configs/centerpoint/centerpoint_0075voxel_second_secfpn_dcn_4x8_cyclic_20e_nus.py
   CONFIG_FILE=mmdetection3d/configs/pointpillars/hv_pointpillars_secfpn_sbn-all_4x8_2x_nus-3d.py
   /tools/dist_test.sh ${CONFIG_FILE} ${CHECKPOINT_FILE} ${GPU_NUM} --format-only --eval-options 'jsonfile_prefix=${OUTPUT_PREFIX}'
   ```
   evalution metrics in nuscenes format could be gained by run
   ```
   python eval_metric.py
   ```
