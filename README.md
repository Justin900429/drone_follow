# Object detection with AutoML

## Introduction
Using AutoML to train the object localization task.

## Prepare the dataset
To train the model, we should prepare the dataset. The file **capture.py** can be used to record the video using `cv2.VideoCapture()`. After getting the recording video, feel free to use `ffmpeg` to extract the frames **Noted that ffmpeg will overwrite the existing images**. Alternativly, readers can use **extract.py** to extract the image without overwritting the images.

```bash
# Using ffmpeg
ffmpeg -i output.mp4 -vf "fps=20" "frame/out%02d.jpg"

# Using extract.py
python extract.py -n <input file> -l <location of output files> -p <prefix of extracted files>
```

