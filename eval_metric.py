from nuscenes import NuScenes
from nuscenes.eval.detection.evaluate import DetectionEval
from nuscenes.eval.detection.config import config_factory

nusc = NuScenes(version='v1.0-trainval', dataroot='/path/to/nuscenes', verbose=True)


config = config_factory("detection_cvpr_2019")  

results_path = "/path/to/results.json"  
output_dir = "/path/to/output/"  


detection_eval = DetectionEval(
    nusc=nusc,
    config=config,
    result_path=results_path,
    eval_set='val',  # 评估数据集（train 或 val）
    output_dir=output_dir,
    verbose=True
)

metrics = detection_eval.main()
