import yaml
import cv2
from math import sqrt


def stay(centers):
    select = []
    skip = 16
    l = len(centers)
    i = 0
    while i < l:
        current = centers[i]
        if i + 5 < l:
            next_center = centers[i + 1]
            next5_center = centers[i + 5]
            next3_center = centers[i + 3]
            if distance(current, next_center) <= 1 and distance(current, next3_center) <= 1.4 and distance(current, next5_center) <= 2:
                select.append(current)
                i += skip
        i += 1
    return select


def search(select, data):
    dis_threshold = 45
    keys = list(data.keys())
    print(keys)
    with open("output.txt", "a") as file:
        for center in select:
            min_dis = float('inf')
            min_key = None
            for key in keys:
                value = list(data[key])
                dis = distance(center, value)
                if dis < min_dis:
                    min_dis = dis
                    min_key = key
            if min_dis <= dis_threshold:
                file.write(str(min_key))
            else:
                file.write("\nSorry,QAQ\n")
G

def distance(x, y):
    distance = sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)
    #print(distance)
    return distance


if __name__ == "__main__":
    centers = [[x,y]] # 用你喜欢的方式导入中心点坐标，格式应当是[[x0,y0],[x1,y1],...]
    select = stay(centers)
    search(select, data)
