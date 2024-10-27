import requests

# Đường dẫn tới tệp cục bộ bạn muốn tải lên
file_path = 'path/to/your/file.txt'

# URL của API nơi bạn muốn tải lên tệp
url = 'https://example.com/upload'

# Các tham số khác (nếu cần)
data = {
    'param1': 'value1',
    'param2': 'value2',
}

# Mở tệp ở chế độ đọc nhị phân
with open(file_path, 'rb') as file:
    # Định nghĩa tệp gửi đi trong yêu cầu POST
    files = {'file': file}
    
    # Gửi yêu cầu POST với tệp đính kèm
    response = requests.post(url, files=files, data=data)

# Kiểm tra phản hồi từ máy chủ
if response.status_code == 200:
    print('Tải lên thành công!')
    print('Phản hồi từ máy chủ:', response.json())
else:
    print('Tải lên thất bại!')
    print('Mã trạng thái:', response.status_code)
    print('Phản hồi từ máy chủ:', response.text)
