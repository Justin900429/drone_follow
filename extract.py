import cv2
import argparse
import os

# Add the argument parse
arg_p = argparse.ArgumentParser()
arg_p.add_argument("-n", "--name",
                   required=True,
                   help="Path to the input video")
arg_p.add_argument("-l", "--location",
                   required=True,
                   help="The folder for saving the images"
                   )
arg_p.add_argument("-f", "--fps",
                   type=int,
                   default=20,
                   help="Frame per second for the extracted images")
arg_p.add_argument("-p", "--prefix",
                   type=str,
                   default="out",
                   help="Prefix for the output files' name")
args = vars(arg_p.parse_args())

# Open the video
cap = cv2.VideoCapture(args["name"])

# Init the counter and set the filename
count = 1
filename = f"{args['location']}/{args['prefix']}_{str(count)}.jpg"

# If the folder is not exit
#  create an folder
if not os.path.exists(args["location"]):
    os.makedirs(args["location"])

# Find the exist file name
#  and start with next counter
if os.path.isfile(filename):
    for file in os.listdir(args["location"]):
        if file.endswith(".jpg") & file.startswith(f"{args['prefix']}_"):
            count += 1

# Start extracting video
#  the FPS of the output images
#  will equal to the original video
while True:
    # Read the frame
    success, frame = cap.read()

    # Break after the video finished
    if not success:
        break

    # The output filename
    filename = f"{args['location']}/{args['prefix']}_{str(count)}.jpg"
    # Write in the images
    cv2.imwrite(filename, frame)

    # increase the counter
    count += 1

cap.release()
