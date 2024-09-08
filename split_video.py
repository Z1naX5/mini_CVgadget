import cv2
import math
import numpy as np


def split_video(video, num_parts):
    # 获取视频的总帧数和帧率
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = video.get(cv2.CAP_PROP_FPS)

    frames_per_segment = math.ceil(total_frames / num_parts)

    # 逐帧读取视频并进行切分
    for i in range(num_parts):
        output_file = f"part_{i + 1}.mp4"
        output_video = cv2.VideoWriter(output_file, cv2.VideoWriter_fourcc(*"mp4v"), fps,
                                       (int(video.get(3)), int(video.get(4))))

        start_frame = i * frames_per_segment
        end_frame = min((i + 1) * frames_per_segment, total_frames)

        video.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

        # 逐帧写入当前分段的视频帧
        for frame_index in range(start_frame, end_frame):
            ret, frame = video.read()
            if ret:
                output_video.write(frame)

        output_video.release()

    video.release()


def split_ROI(video, flag):
    # 获取视频的帧率、宽度和高度
    fps = video.get(cv2.CAP_PROP_FPS)
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    output_video = cv2.VideoWriter('new_video.mp4', fourcc, fps,
                                   (int(width - 0), int(height - 0))) # 新视频的宽，高
    while True:
        ret, frame = video.read()
        if flag == 1:
            frame = frame[0:int(height), 0:int(width)] # 要保留的画面部分,先高后宽
        if not ret:
            break
        cv2.imshow('Frame', frame)

        # 保存结果帧到输出视频
        output_video.write(frame)

        # 按下 'q' 键退出循环
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video.release()


if __name__ == "__main__":
    video = cv2.VideoCapture("output_video.mp4")
    num_parts = 15  # 想要切分的份数
    split_video(video, num_parts)
    split_ROI(video, flag)
