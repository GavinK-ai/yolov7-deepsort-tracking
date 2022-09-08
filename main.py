from detection_helpers import *
from tracking_helpers import *
from  bridge_wrapper import *
from PIL import Image

detector = Detector()

tracker = YOLOv7_DeepSORT(reID_model_path="./deep_sort/model_weights/mars-small128.pb", detector=detector)

tracker.track_video("vid/CF254_3_1.mp4", output="vid/CF254_3_1_#", show_live = True, skip_frames = 0, count_objects = True, verbose=1)