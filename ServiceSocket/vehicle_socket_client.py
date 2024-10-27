import socketio
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import cv2
import json
import ipaddress
from base_station import BaseStation
import traceback
import time
import base64
import threading
from video_proc import VideoProcessor

# # -----------------------------------------------
# # Khởi tạo một client Socket.IO
sio = socketio.Client()

# Định nghĩa các event handler
@sio.event
def connect():
    print('Đã kết nối với server')
    sio.emit('create_room','192.168.1.25')
    sio.emit('join','192.168.1.25')

@sio.event
def disconnect():
    print('Đã ngắt kết nối với server')

# lang nghe thong bao
@sio.on('msg')
def handle_message(data):
    print('Thông báo server:', data)

@sio.on('frame')
def handle_frame(data):
    print('frame:', data)

@sio.on('sensor')
def handle_sensor(data):
    # print('sensor:', data)
    a = True

@sio.on('infor')
def handle_sensor(data):
    print(data)

# # Kết nối với server
sio.connect('http://10.0.0.35:5000')

sio.wait()



# import cv2

# # Mở camera nội bộ (thường là camera mặc định của máy tính xách tay)
# cap = cv2.VideoCapture(0)

# if not cap.isOpened():
#     print("Không thể mở camera")
#     exit()

# while True:
#     # Đọc một frame từ camera
#     ret, frame = cap.read()
    
#     if not ret:
#         print("Không thể nhận frame từ camera")
#         break
    
#     # Hiển thị frame
#     cv2.imshow('Camera', frame)
#     print(frame)
#     # Nhấn phím 'q' để thoát
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Giải phóng tài nguyên
# cap.release()
# cv2.destroyAllWindows()
