import cv2
import threading
import time

class CameraBufferCleanerThread(threading.Thread):
    def __init__(self, camera, name='camera-buffer-cleaner-thread'):
        self.camera = camera
        self.last_frame = None
        self.running = True
        super(CameraBufferCleanerThread, self).__init__(name=name)
        self.start()

    def run(self):
        while self.running:
            ret, self.last_frame = self.camera.read()
            if not ret:
                self.running = False
                raise Exception("Couldn't capture video")

class VideoProcessor:
    def __init__(self, host):
        self.cap = cv2.VideoCapture(f"rtsp://{host}:8554/video_stream")
        self.cam_cleaner = CameraBufferCleanerThread(self.cap)

    def get_latest_frame(self):
        # Đợi cho đến khi khung hình đầu tiên được nạp
        while self.cam_cleaner.last_frame is None:
            pass
        return self.cam_cleaner.last_frame

    def show_video(self):
        while True:
            frame = self.get_latest_frame()
            if frame is not None:
                cv2.imshow('Video Stream', frame)

            # Nhấn 'q' để thoát
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    def close(self):
        self.cam_cleaner.running = False
        time.sleep(1)
        self.cap.release()
        cv2.destroyAllWindows()

# # Khởi tạo và chạy video
# if __name__ == "__main__":
#     host = "192.168.1.100"  # Thay thế bằng địa chỉ IP của Pi hoặc nguồn RTSP
#     processor = VideoProcessor(host)

#     try:
#         processor.show_video()
#     except Exception as e:
#         print(f"Error: {e}")
#     finally:
#         processor.close()
