import csv
import pickle
import os
import copy
import numpy as np
import cv2
import pickle

full_array = []
name_full = []
name_txt = []

def csv_dict_reader(file_obj):
    """
    Read a CSV file using csv.DictReader
    """
    reader = csv.DictReader(file_obj, delimiter=',')
    for line in reader:
        # print(line["filename"]),
        # print(line["x_from"])
        # print(line["y_from"]),
        # print(line["width"])
        # print(line["height"])
        # print(line["sign_class"]),
        # print(line["sign_id"])
        name_full.append(line["filename"])
        full_array.append([line["filename"], line["x_from"], line["y_from"], line["width"],
                                        line["height"], line["sign_class"], line["sign_id"]])
    # print(full_array)

if __name__ == "__main__":
    with open("/home/ivliev/Загрузки/full-gt.csv") as f_obj:
        csv_dict_reader(f_obj)

data = []
for i in range(len(full_array)):
    # img = cv2.imread("/home/ivliev/Загрузки/rtsd-frames/"+full_array[i][0])
    #
    # x = int(full_array[i][1])
    # y = int(full_array[i][2])
    # w = int(full_array[i][3])
    # h = int(full_array[i][4])
    sign_class = full_array[i][5]
    #
    # sign = img[y:y+h,x:x+w]
    # cv2.imwrite("test/" + str(i)+".jpg", sign)
    line = [i, sign_class]
    data.append(line)
    # print(img)
print(data)

with open('data.pickle', 'wb') as f:
    pickle.dump(data, f)
