# Object detection with AutoML

## Introduction
Using AutoML to train the object localization task.

## Prepare the dataset
To train the model, we should prepare the dataset. The file "capture.py" is the file being used to record the video using `cv2.VideoCapture()`. After getting the recording video, we can use `ffmpeg` to extract the frames.

```bash
ffmpeg -i output.mp4 -vf "fps=20" "frame/out%02d.jpg"
```

