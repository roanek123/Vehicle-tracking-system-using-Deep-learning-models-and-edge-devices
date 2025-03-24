## AUTO TRACK: TRAFFIC MANAGEMENT SYSTEM USING AI MODELS.

The project aims to develop a Vehicle Counting System (VCS) using Image Recognition Technology (IRT), specifically leveraging the YOLOv8 model for its high accuracy, speed, and efficiency in object detection. It targets low-power platforms like the Raspberry Pi 3A+, making it suitable for widespread deployment in urban areas. The system captures traffic scenes, processes them to detect and count vehicles, and transmits data to support traffic management, contributing to improved flow and reduced congestion.


![Thumbnail](https://github.com/user-attachments/assets/71140960-f53e-4f57-85d5-2a8c8f497985)

## Features
The VCS offers a robust set of features, aligning with modern traffic management needs:

- **Real-Time Processing:** YOLOv8 enables instantaneous vehicle detection and counting, critical for dynamic traffic scenarios.
- **High Accuracy:** The model’s multi-scale feature extraction ensures reliable detection in complex urban environments, validated against ground truth data.
- **Low-Power Optimization:** Designed for Raspberry Pi, it minimizes energy consumption through model compression and efficient algorithms.
- **Scalability:** Supports multiple intersections via Wi-Fi and Bluetooth for data transmission, facilitating city-wide deployment.
- **Data Collection and Preprocessing:** Captures 10-second video bursts every minute, with preprocessing (e.g., noise reduction) enhancing detection accuracy.
- **Reliability and Testing:** Tested against ground truth data, showing reliable performance across varying traffic conditions, with results indicating practical deployment potential.


## Key Components
The system's hardware backbone is the Raspberry Pi 3A+, paired with its camera module for video capture. Software components include:

- YOLOv8 for real-time detection, pre-trained for vehicle classes.
- ByteTrack for tracking, ensuring vehicles are not recounted across frames.
- Supervision library for visual annotations and line zone counting.
- SCP for data transfer, leveraging paramiko for secure communication.
- FFmpeg for video format conversion, used in both C++ and shell scripts for compatibility.
- The integration with Raspberry Pi highlights its low-power optimization, using techniques like quantization and pruning to ensure efficiency, as noted in the documentation.
## Installation

The system requires several Python packages for operation:

- **ultralytics:** For YOLOv8 model implementation.
 - **supervision:** For object detection utilities, including annotations and line counting.
 - **numpy:** For numerical operations, particularly array handling in video processing.
 - **paramiko:** For secure file transfer via SCP.

```bash
  pip install ultralytics supervision numpy paramiko
```
Additionally, system dependencies include:

 - FFmpeg, installed via system package managers (e.g., sudo apt-get install ffmpeg on Linux).
- libcamera, part of Raspberry Pi OS, for video capture, requiring camera module enablement in Raspberry Pi configuration.
## Documentation

[Documentation: ](https://github.com/roanek123/Vehicle-tracking-system-using-Deep-learning-models-and-edge-devices/blob/main/Project%20Documentation%20(2).pdf)
The primary documentation is the Project Documentation (2).pdf, summarizing methodology, results, and system evaluation. For the repository, a comprehensive README should include:

- Project description, aligning with the brief provided.
- Installation instructions, detailing Python packages and system dependencies.
- Usage instructions, clarifying how to run run.sh on Raspberry Pi and run.ps1 on the processing machine.
- Setup for Raspberry Pi, including enabling the camera module and configuring network for SCP.
- Explanation of file paths, addressing potential inconsistencies (e.g., traffic.mp4 vs. test.h264).

## Script Role Table

| Script       | Role                                      | Execution Environment          |
|--------------|------------------------------------------|-------------------------------|
| `start.py`   | Processes video for detection and counting | Processing machine (Python)  |
| `transfer.py`| Transfers video file via SCP             | Processing machine (Python)  |
| `convert.cpp`| Converts H.264 to MP4 using FFmpeg       | Compile and run on machine   |
| `run.ps1`    | Automates transfer and processing        | Processing machine (PowerShell) |
| `run.sh`     | Captures and converts video on Raspberry Pi | Raspberry Pi (Bash)       |


## Run Locally
Download the following repository in your local environment.

```bash
  git clone https://github.com/roanek123/Vehicle-tracking-system-using-Deep-learning-models-and-edge-devices
```

install the following packages specified above. Then follow the below steps:
- On Raspberry Pi, run.sh captures video and converts it, ensuring continuous data collection.
- On the processing machine, run.ps1 automates transfer and processing, with start.py generating an annotated output video (transtraffic1x.mp4) in the output folder.
- Users should ensure file paths align, as start.py expects input/traffic.mp4, while transfer.py fetches test.h264, potentially requiring conversion via convert.cpp and renaming.


## Contributing
Contributions are always welcome!

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

