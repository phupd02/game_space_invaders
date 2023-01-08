# Hướng dẫn chơi và cài đặt
## 1. Hướng dẫn cài đặt
### Bước 1: Cài đặt pygame (Lưu ý cần cài đặt python)
_**Window**_
*  Mở terminal và nhập dòng lệnh **pip install pygame**

_**Linux**_
* Chạy lệnh **sudo apt-get install python-pygame**

### Bước 2:
* Vào thư mục **game**, mở file **Main.py**, nhấn F5 hoặc Run trong IDE để thực hiện chạy chương trình
<img src="https://imgur.com/aypyLpJ">

## 2. Hướng dẫn chơi
_**Nhấn**_
* Chuột trái: Để bắt đầu trò chơi
* A: Để di chuyển sang trái
* D: Để di chuyển sang phải
* S: Để di chuyển xuống
* W: Để di chuyển lên
* Space: Để bắn các mục tiêu
* P: Để tạm dừng trò chơi

_**Luật chơi: Nhiệm vụ của người chơi là điều khiển tàu vũ trụ tiêu diệt các kẻ địch**_
* Nếu bắn trúng mục tiêu, điểm sổ của người chơi sẽ tăng lên 1
* Người chơi sẽ được cung cấp 5 mạng sống, cứ một kẻ địch thoát được cuộc tấn công, mạng sống của người chơi sẽ bị giảm đi 1 mạng
* Nếu bị kẻ địch bắn trúng hoặc va chạm với kẻ địch, thanh năng lượng của người chơi sẽ bị sụt giảm
* Số lượng kẻ địch ở mỗi level là khác nhau, level 1 có 5 địch, level 2 có 10 địch, từ level 3 số lượng quân địch là 15
* Cứ mỗi 10 điểm đạt được, đạn của người chơi được nâng cấp 1 lần. Khi đạt 10 điểm, background của game sẽ tự động thay đổi
* Game over nếu người chơi không còn mạng sống hoặc mất hết năng lượng
