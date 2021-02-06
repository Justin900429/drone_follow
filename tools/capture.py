#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import argparse

# Add the argument parse
arg_p = argparse.ArgumentParser()
arg_p.add_argument("-W", "--width",
                   type=int,
                   default=640,
                   help="Width of the output video")
arg_p.add_argument("-H", "--height",
                   type=int,
                   default=480,
                   help="Height of the output video")
arg_p.add_argument("-n", "--name",
                   type=str,
                   default="output",
                   help="Name of the output video")
arg_p.add_argument("-f", "--fps",
                   type=int,
                   default=20,
                   help="Frame per second for the extracted images")
args = vars(arg_p.parse_args())


if __name__ == "__main__":
    # Open the web cam
    cap = cv2.VideoCapture(0)

    # Set the width and height
    cap.set(3, args["width"])  # Width
    cap.set(4, args["height"])  # Height

    # Recorder
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    video_writer = cv2.VideoWriter("{}.mp4".format(args["name"]),
                                   fourcc,
                                   args["fps"],
                                   (args["width"], args["height"])
                                   )

    # Check whether the camera is opened or not
    if not cap.isOpened():
        print("Camera not opened")
        exit(1)

    # record video
    while True:
        # Read in the frame
        success, frame = cap.read()

        # Write in the video if successfully captured the frame
        if success:
            video_writer.write(frame)
            cv2.imshow('Video', frame)

        # Wait key for the video
        if cv2.waitKey(args["fps"]) == 27:  # ESC
            break

    # Release all the using resources
    cap.release()
    video_writer.release()
    cv2.destroyAllWindows()
