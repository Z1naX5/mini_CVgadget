import cv2
import numpy as np
import yaml


def preProccessing(image):
    return image


def trace(video):
    ret, frame = video.read()
    if not ret:
        print("无法读取视频帧")
        exit()

    bbox = cv2.selectROI("Frame", frame, fromCenter=False, showCrosshair=True)
    frame = preProccessing(frame)
    tracker.init(frame, bbox)

    centers = []
    while True:

        ret, frame = video.read()
        if not ret:
            print("无法读取视频帧")
            return centers
            exit()

        frame0 = np.copy(frame)
        frame = preProccessing(frame)
        if not ret:
            break

        # 更新跟踪器并获取目标位置
        success, bbox = tracker.update(frame0)

        # 如果跟踪成功，则绘制目标区域
        if success:
            (x, y, w, h) = [int(v) for v in bbox]
            if w < 120 or h < 65:
                w += 10
                x -= 10
                h += 10
                y - +10
            cv2.rectangle(frame0, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            center = [x + w / 2, y + h / 2]
            centers.append(center)
            if w < 120 or h < 65:
                w += 10
                x -= 10

        # 显示当前帧
        cv2.imshow("Frame", frame0)
        cv2.imshow("Frame1", frame)

        # 按下'q'键退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == "__main__":
    tracker = cv2.legacy.TrackerCSRT_create()
    file_name = "filename"
    video = cv2.VideoCapture("{}.mp4".format(file_name))
    centers = trace(video)
    video.release()
    cv2.destroyAllWindows()
