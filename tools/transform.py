import os
import argparse

import pandas as pd

# Add the argument parse
arg_p = argparse.ArgumentParser()
arg_p.add_argument("-p", "--prefix",
                   required=True,
                   type=str,
                   help="Prefix of the cloud storage path")
arg_p.add_argument("-l", "--location",
                   type=str,
                   required=True,
                   help="Location of the label files")
arg_p.add_argument("-o", "--output",
                   type=str,
                   default="res.csv",
                   help="Output of csv file")
args = vars(arg_p.parse_args())

# Class labels
class_labels = [
    "follow",
    "one",
    "two",
    "three",
    "four",
    "five"
]
# Prefix of the cloud storage
prefix = f"gs://{args['prefix']}"

# Array for final csv file
res = []

# Get all the file in dir
for dir in os.listdir(args["location"]):
    # Get the dirname
    dir_name = f"{args['location']}/{dir}"

    # Check whether is dir
    if not os.path.isdir(dir_name):
        continue

    prefix = f"{prefix}/{dir}"

    # Process the files
    for file in os.listdir(dir_name):

        # Check the class ends with txt
        #  and not class.txt
        if (not file.endswith(".txt")) | \
                (file == "classes.txt"):
            continue

        # Get the file name
        file_whole_name = f"{dir_name}/{file}"

        # Read in txt as csv
        df_txt = pd.read_csv(file_whole_name, sep=" ", header=None)

        # Create data for each labels
        for index, row in df_txt.iterrows():
            # Temp array for csv
            temp_csv = ["UNASSIGNED"]

            # gs://prefix/name/{image_name}
            cloud_path = f"{prefix}/{os.path.splitext(file)[0]}.jpg"
            temp_csv.append(cloud_path)

            # Class label
            temp_csv.append(class_labels[int(row[0])])

            # Add the upper left coordinate
            temp_csv.extend([row[1], row[2]])

            # Add the lower left coordinate (not necessary, left blank)
            temp_csv.extend(["", ""])

            # Add the lower right coordinate
            temp_csv.extend([row[1] + row[3], row[2] + row[4]])

            # Add the upper right coordinate (not necessary, left blank)
            temp_csv.extend(["", ""])

            # Append to the res
            res.append(temp_csv)


# Write to the result csv
res_csv = pd.DataFrame(res,
                       columns=["set", "path", "label",
                                "x_min", "y_min",
                                "x_max", "y_min",
                                "x_max", "y_max",
                                "x_min", "y_max"])
res_csv.to_csv("res.csv", index=False, header=False)
