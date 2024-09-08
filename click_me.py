import cv2
import numpy as np
import yaml


def write_to_yaml(key, value):
    data_dict[key] = value
    with open('output.yaml', 'w') as outfile:
        yaml.dump(data_dict, outfile)


def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        xy = "%d,%d" % (x, y)
        cv2.circle(img, (x, y), 1, (255, 0, 0), thickness=-1)
        cv2.putText(img, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
                    1.0, (0, 0, 0), thickness=1)
        cv2.imshow("image", img)
        flg = -1
        if key_list is not None and isinstance(key_list, list):
            flg += 1
            if len(key_list) > 0:
                key = key_list.pop(0)
            else:
                key = chr(len(data_dict) + 65 - flg)
        else:
            key = chr(len(data_dict) + 65)

        value = (x, y)

        write_to_yaml(key, value)


if __name__ == "__main__":
    img = cv2.imread('bg.png')
    data_dict = {}
    key_list = None  # key
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)
    while (1):
        cv2.imshow("imaGge", img)
        if cv2.waitKey(0) & 0xFF == 27:  # 按下esc退出
            break

    cv2.destroyAllWindows()
