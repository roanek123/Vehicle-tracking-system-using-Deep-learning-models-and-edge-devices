import os
HOME=os.getcwd()
print(HOME)

source_video_path=f"{HOME}/input/traffic.mp4"

from IPython import display
display.clear_output()

import ultralytics
ultralytics.checks()

from IPython import display
display.clear_output()

import supervision as sv
print("supervision.__version__:",sv.__version__)

MODEL = "yolov8x.pt"

from ultralytics import YOLO

model=YOLO(MODEL)
model.fuse

# dict maping class_id to class_name
CLASS_NAMES_DICT = model.model.names

# class_ids of interest - car, motorcycle, bus and truck
selected_classes = [2, 3, 5, 7]

import numpy as np

LINE_START = sv.Point(50, 1500)
LINE_END = sv.Point(3840-50, 1500)

TARGET_VIDEO_PATH = f"{HOME}/output/transtraffic1x.mp4"

byte_tracker = sv.ByteTrack(track_thresh=0.25, track_buffer=30, match_thresh=0.8, frame_rate=30)
video_info=sv.VideoInfo.from_video_path(source_video_path)
generator=sv.LineZone(start=LINE_START,end=LINE_END)
line_zone=sv.LineZone(start=LINE_START,end=LINE_END)
box_annotator=sv.BoxAnnotator(thickness=1,text_thickness=1,text_scale=0.5)
# trace_annotator=sv.TraceAnnotator(thickness=1,trace_length=50)
line_zone_annotator=sv.LineZoneAnnotator(thickness=1,text_thickness=1,text_scale=0.5)

def callback(frame: np.ndarray, index:int) -> np.ndarray:
    results = model(frame, verbose=False)[0]
    detections = sv.Detections.from_ultralytics(results)
    detections = detections[np.isin(detections.class_id, selected_classes)]
    detections = byte_tracker.update_with_detections(detections)
    labels = [
        f"{model.model.names[class_id]} {confidence:0.2f}"
        for confidence, class_id, tracker_id
        in zip(detections.confidence, detections.class_id, detections.tracker_id)
    ]
    # To trace the path of the detected object
    # annotated_frame = trace_annotator.annotate(
    #     scene=frame.copy(),
    #     detections=detections
    # ) 
    annotated_frame=box_annotator.annotate(
        # scene=annotated_frame,
        scene=frame.copy(),
        detections=detections,
        labels=labels)
    line_zone.trigger(detections)
    return  line_zone_annotator.annotate(annotated_frame, line_counter=line_zone)

sv.process_video(
    source_path = source_video_path,
    target_path = TARGET_VIDEO_PATH,
    callback=callback
)
