import os
import cv2
import csv


PATH = "politicalAdv/political-ads/video"
CSV = "politicalAdv/political-ads/1608696687_export.csv"
EXTENSION = ".mp4"


def load():
    ds = {}
    with open(CSV) as csv_file:
        data = csv.reader(csv_file)
        for item in data:
            ds[item[0]] = {"file": item[1]+EXTENSION, "subjects": item[5], "candidates": item[6], "message": item[10], "transcript": item[14]}
    for id in ds.keys():
        video_file = os.path.join(PATH, ds[id]["file"])
        video = cv2.VideoCapture(video_file)
        if not video.isOpened():
            print("Error opening video stream or file")
        while video.isOpened():
            ret, frame = video.read()
            if ret:
                print("add frame to list")
            else:
                break
        video.release()
    return ds


if __name__ == '__main__':
    ds = load()
