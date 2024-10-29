import socketio
import cv2
import json
import ipaddress
import traceback
from PIL import Image
import time
import base64
import threading
from video_proc import VideoProcessor
import signal
import sys

class BaseStation:
    def __init__(self, mode='detect'):
        self.connected = False
        self.mode = mode
    
    def connect(self, host, port=65432):
        self.vproc = VideoProcessor(host)
        self.connected = True
    
    def real_time_control(self):
        if self.connected and self.vproc.cam_cleaner.running:
            try:
                frame = self.vproc.get_latest_frame()
            except Exception:
                traceback.print_exc()
                return False, None
            return True, frame
        else:
            return False, None 

    def close(self):
        self.vproc.close()

def show_frame():
    ret, frame = bs.real_time_control()
    frame_b64 = ''
    if ret:
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ret, frame = cv2.imencode('.jpg', frame)
        frame = frame.tobytes()
        frame_b64 = base64.b64encode(frame).decode('utf-8')
        
    else:
        img = Image.open('config/video_404.png') 
        frame_b64 = base64.b64encode(img).decode('utf-8')
    data_sent = {
        'room_name': host,
        'data': frame_b64,
    }
    data_sent = json.dumps(data_sent)
    sio.emit('frame', data_sent)
    # time.sleep(0.05)  
    # show_frame()

def thread_frame():
    while True:
        time.sleep(1/15)  
        try:
           show_frame()
        except Exception:
            # frame.e
            a = True

# Init base station
bs = False
host = ''
# -----------------------------------------------
# Khởi tạo một client Socket.IO
sio = socketio.Client()

# khoi tao cac luong
frame = threading.Thread(target=thread_frame, name='Stream frame')

# Định nghĩa các event handler
@sio.event
def connect():
    print('Đã kết nối với server')
@sio.event
def disconnect():
    print('Đã ngắt kết nối với server')

# created
@sio.on('create_room')
def handle_create(data):
    global bs
    global host
    print('create_room:', data)
    host = data
    host = host.replace('v','')
    time.sleep(5)
    sio.emit('join',host)
    bs = BaseStation()
    bs.connect(host)
    frame.start()

# Kết nối với server
sio.connect('http://localhost:5000')


def signal_handler(sig, frame):
    print('Đang dừng server...')
    sys.exit(0)

# Bắt tín hiệu ngắt (Ctrl+C) và tín hiệu dừng chương trình (SIGTERM)
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)
sio.wait()

