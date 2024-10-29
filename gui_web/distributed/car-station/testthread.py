# import threading
# import time

# def worker():
#     i = 0
#     while i < 1000:
#         i = i + 1
#         print(f"Worker started on ${i} thread {threading.current_thread().name}")
    
# def worker2():
#     print(f"Worker started on thread {threading.current_thread().name}")
#     time.sleep(0.52)
#     print(f"Worker finished on thread {threading.current_thread().name}")
# def worker3():
#     print(f"Worker started on thread {threading.current_thread().name}")
#     time.sleep(0.52)
#     print(f"Worker finished on thread {threading.current_thread().name}")
# # Tạo và bắt đầu 3 thread
# t1 = threading.Thread(target=worker, name='Thread 1')
# t2 = threading.Thread(target=worker2, name='Thread 2')
# t3 = threading.Thread(target=worker3, name='Thread 3')

# t1.start()
# t2.start()
# t3.start()

# # # Chờ đợi các thread hoàn thành
# # t1.join()
# # t2.join()
# # t3.join()

# print("All workers finished")


# import cv2
# import gc

# def main():
#     # Mở kết nối đến camera. Thông thường, camera mặc định sẽ là camera 0.
#     cap = cv2.VideoCapture(0)

#     # Kiểm tra xem camera có mở được không
#     if not cap.isOpened():
#         print("Không thể mở camera")
#         return

#     while True:
#         # Đọc một khung hình từ camera
#         ret, frame = cap.read()

#         # Kiểm tra xem có đọc được khung hình không
#         if not ret:
#             print("Không thể nhận khung hình (kết thúc phát trực tiếp?)")
#             break

#         # Hiển thị khung hình
#         cv2.imshow('Camera', frame)

#         # Chờ phím 'q' để thoát khỏi vòng lặp
#         if cv2.waitKey(1) == ord('q'):
#             break

#         # Giải phóng bộ nhớ cho khung hình
#         del frame
#         gc.collect()

#     # Giải phóng camera và đóng tất cả cửa sổ
#     cap.release()
#     cv2.destroyAllWindows()
    
# main()

import cv2
import time

# Mở camera
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Không thể mở camera")
    exit()

# Chụp và xử lý hình ảnh màu
start_time = time.time()
for _ in range(1000):  # Tăng số lượng khung hình
    ret, frame_color = cap.read()
    if not ret:
        break
end_time = time.time()
print(f"Thời gian xử lý hình ảnh màu: {end_time - start_time} giây")

# Chụp và chuyển đổi sang grayscale và xử lý
start_time = time.time()
for _ in range(1000):  # Tăng số lượng khung hình
    ret, frame_color = cap.read()
    if not ret:
        break
    frame_gray = cv2.cvtColor(frame_color, cv2.COLOR_BGR2GRAY)
end_time = time.time()
print(f"Thời gian xử lý hình ảnh đen trắng: {end_time - start_time} giây")

# Giải phóng tài nguyên
cap.release()
