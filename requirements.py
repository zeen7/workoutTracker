absl-py==1.4.0
attrs==22.2.0
contourpy==1.0.7
cycler==0.11.0
flatbuffers==23.3.3
fonttools==4.39.3
importlib-resources==5.12.0
kiwisolver==1.4.4
matplotlib==3.7.1
mediapipe-silicon==0.9.1
numpy==1.24.2
opencv-contrib-python==4.7.0.72
packaging==23.0
Pillow==9.5.0
protobuf==3.20.1
pyparsing==3.0.9
python-dateutil==2.8.2
six==1.16.0
zipp==3.15.0
mediapipe; platform_system != "Darwin" or platform.machine != "arm64"
mediapipe-silicon; platform_system == "Darwin" and platform.machine == "arm64"
protobuf>=3.11,<4