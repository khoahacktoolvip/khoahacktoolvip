import threading
import base64
import os
import time
import re
import json
import random
import requests
import socket
import sys
from time import sleep
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import colorsys
from colorama import init, Style
import math

# Kiểm tra và cài đặt thư viện cần thiết
try:
    from faker import Faker
    from requests import session
    from colorama import Fore, Style
    import pystyle
except ImportError:
    os.system("pip install faker requests colorama bs4 pystyle")
    os.system("pip3 install requests pysocks")
    print('__Vui Lòng Chạy Lại Tool__')
    sys.exit()

init(autoreset=True)

# Tạo hoặc đọc khóa mã hóa bằng base64
secret_key = base64.urlsafe_b64encode(os.urandom(32))

# Mã hóa và giải mã dữ liệu bằng base64
def encrypt_data(data):
    return base64.b64encode(data.encode()).decode()

def decrypt_data(encrypted_data):
    return base64.b64decode(encrypted_data.encode()).decode()

import requests
import random
import string
import hashlib,os

trang = "\033[1;37m\033[1m"
xanh_la = "\033[1;32m\033[1m"
xanh_duong = "\033[1;34m\033[1m"
xanhnhat = '\033[1m\033[38;5;51m'
do = "\033[1;31m\033[1m\033[1m"
xam = '\033[1;30m\033[1m'
vang = "\033[1;33m\033[1m"
tim = "\033[1;35m\033[1m"
hongnhat = "#FFC0CB"
kt_code = "</>"
dac_biet = "\033[32;5;245m\033[1m\033[38;5;39m"
vua = "\033[1;37m[>_<]\033[1;37m \033[1;37mNGUYENDANGKHOA\033[1;37m \033[1;37m=> \033[1;34m\033[1m"

import os
try:
    from faker import Faker
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import pad
    import requests
except ImportError:
    os.system('pip install Faker')
    os.system('pip install requests')
    os.system('pip install pycryptodome')
    
    
#import lại sau khi cài đặt
from faker import Faker
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import requests

trang = "\033[1;37m\033[1m"
xanh_la = "\033[1;32m\033[1m"
xanh_duong = "\033[1;34m\033[1m"
xanhnhat = '\033[1m\033[38;5;51m'
do = "\033[1;31m\033[1m\033[1m"
xam='\033[1;30m\033[1m'
vang = "\033[1;33m\033[1m"
tim = "\033[1;35m\033[1m"
hongnhat = "#FFC0CB"
kt_code = "</>"
dac_biet = "\033[32;5;245m\033[1m\033[38;5;39m"
vua = "\033[1;37m[>_<]\033[1;37m \033[1;37mNGUYENDANGKHOA\033[1;37m \033[1;37m=> \033[1;34m\033[1m"


import os, json, sys, requests 
from sys import platform
from time import sleep
from datetime import datetime
from random import randint
from pystyle import Colors, Colorate
import uuid, re
from bs4 import BeautifulSoup
import os, sys, time, math, random, colorsys

# ────────── KÍCH HOẠT ANSI (Windows) ──────────
if os.name == "nt":
    import ctypes
    kernel32 = ctypes.windll.kernel32
    ENABLE_VT = 0x0004
    handle = kernel32.GetStdHandle(-11)  # STD_OUTPUT_HANDLE = -11
    mode = ctypes.c_ulong()
    if kernel32.GetConsoleMode(handle, ctypes.byref(mode)):
        kernel32.SetConsoleMode(handle, mode.value | ENABLE_VT)

# ────────── HÀM TIỆN ÍCH ──────────
def hsv2rgb(h, s, v): return colorsys.hsv_to_rgb(h, s, v)

def rgb_to_ansi(r, g, b):
    return 16 + (36 * round(r * 5)) + (6 * round(g * 5)) + round(b * 5)

def pastel_rainbow(length, offset=0, bright=0.95, sat=0.42, phase=0):
    return [
        rgb_to_ansi(*hsv2rgb(((i + offset) / (length * 1.2) + phase) % 1, sat, bright))
        for i in range(length)
    ]

def gradient_line(text, colors, sweep=None):
    out = []
    for i, ch in enumerate(text):
        c = colors[i % len(colors)]
        if sweep is not None and abs(i - sweep) < 3:
            out.append(f"\033[1m\033[38;5;{c}m{ch}\033[0m")
        else:
            out.append(f"\033[38;5;{c}m{ch}")
    return "".join(out) + "\033[0m"

def render_frame(f):
    pulse = 0.5 + 0.5 * math.sin(f * 0.03)
    bright = 0.9 + 0.1 * pulse
    sat    = 0.38 + 0.08 * pulse
    sweep  = int((math.sin(f * 0.05) + 1) * max_len // 2)
    phase  = math.sin(f * 0.025) * .25

    lines = []
    for idx, raw in enumerate(logo):
        shift = f + idx * .6
        colors = pastel_rainbow(len(raw), shift, bright, sat, phase)
        lines.append(gradient_line(raw, colors, sweep))
    return lines

def center_text(text, width):
    return text.center(width)

# ────────── LOGO ASCII ──────────
logo = [
    "╔═══════════════════════════════════════════════════════════════╗",
    "║   ████████╗███╗   ███╗  ██╗  ███╗  ██╗██████╗ ██╗  ██╗  ██╗   ║",
    "║   ╚══██╔══╝████╗ ████║  ╚═╝  ████╗ ██║██╔══██╗██║ ██╔╝  ██║   ║",
    "║      ██║   ██╔████╔██║       ██╔██╗██║██║  ██║█████═╝   ██║   ║",
    "║      ██║   ██║╚██╔╝██║       ██║╚████║██║  ██║██╔═██╗   ╚═╝   ║",
    "║      ██║   ██║ ╚═╝ ██║  ██╗  ██║ ╚███║██████╔╝██║ ╚██╗  ██╗   ║",
    "║      ╚═╝   ╚═╝     ╚═╝  ╚═╝  ╚═╝  ╚══╝╚═════╝ ╚═╝  ╚═╝  ╚═╝   ║",
    "╚═══════════════════════════════════════════════════════════════╝"
]
max_len   = max(len(l) for l in logo)
logo_h    = len(logo)
duration  = 3          # giây chạy
delay     = 0.06
frames    = int(duration / delay)
offset    = random.randint(0, 3)

# ────────── BANNER SETUP ──────────
banner_width = max_len + 4
title = "[>_<] NGUYENDANGKHOA /// DANGKHOA_DEV"
footer = "YOUTOBE SHARE TOOL :  https://www.youtube.com/channel/UCGJmaIZ_JbAwoOrHeBZru6A"
start_message = "NHÓM ZALO : https://zalo.me/g/wyboil196"
end_message = """ 
[>_<] NGUYENDANGKHOA                          source by DangKhoa_Dev
______________________________________________________________________
NHÓM ZALO : https://zalo.me/g/wyboil196 
______________________________________________________________________
SHARE TOOL :  https://www.youtube.com/channel/UCGJmaIZ_JbAwoOrHeBZru6A
______________________________________________________________________

Phiên bản :
[>_<] NGUYENDANGKHOA /// DANGKHOA_DEV...
╔═══════════════════════════════════════════════════════════════════╗
║                           Golike TikTok                           ║
╚═══════════════════════════════════════════════════════════════════╝
"""
# ────────── IN BANNER ──────────
# Clear screen
print("\033[2J\033[H", end="")

# Print title
title_colors = pastel_rainbow(len(title), offset)
print(center_text(gradient_line(title, title_colors), banner_width))

# Print top border
border = "═" * (banner_width - 2)
print(f"╔{border}╗")

# Print initial logo
first = render_frame(offset)
for line in first:
    print(f"║ {line.ljust(max_len)} ║")

# Print bottom border
print(f"╚{border}╝")

# Print start message
start_colors = pastel_rainbow(len(start_message), offset)
print(center_text(gradient_line(start_message, start_colors), banner_width), flush=True)

# ────────── VÒNG LẶP ANIMATION ──────────
for f in range(1, frames):
    time.sleep(delay)
    # Move cursor to start of logo
    sys.stdout.write(f"\033[{logo_h + 2}F")
    # Print top border
    sys.stdout.write(f"╔{border}╗\n")
    # Print animated logo
    for line in render_frame(f + offset):
        sys.stdout.write(f"║ {line.ljust(max_len)} ║\n")
    # Print bottom border
    sys.stdout.write(f"╚{border}╝\n")
    sys.stdout.flush()

# ────────── KẾT THÚC BANNER & CHUYỂN SANG API ──────────
time.sleep(delay)
# Clear below logo
sys.stdout.write(f"\033[{logo_h + 2}F\033[J")
# Reprint title
print(center_text(gradient_line(title, title_colors), banner_width))
# Reprint top border
print(f"╔{border}╗")
# Print final frame
for line in render_frame(frames + offset):
    print(f"║ {line.ljust(max_len)} ║")
# Reprint bottom border
print(f"╚{border}╝")
# Print transition message
end_colors = pastel_rainbow(len(end_message), offset)
print(center_text(gradient_line(end_message, end_colors), banner_width))
import sys
from time import sleep
def banner(): 
	""

# ─────────── BANNER ─────────── #
def get_ip_address():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        ip_data = response.json()
        ip_address = ip_data['ip']
        return ip_address
    except Exception as e:
        print(f"Lỗi khi lấy địa chỉ IP: {e}")
        return None

def display_ip_address(ip_address):
    if ip_address:
        banner()
        print(f"╔═══════════════════════════════════════════════════════════════════╗")        
        print(f"\033[1;31m[>_<] NGUYENDANGKHOA => \033[1;31mĐỊA CHỈ IP : {ip_address}")
    else:
        print("Không thể lấy địa chỉ IP của thiết bị.")

def luu_thong_tin_ip(ip, key, expiration_date):
    data = {ip: {'key': key, 'expiration_date': expiration_date.isoformat()}}
    encrypted_data = encrypt_data(json.dumps(data))

    with open('ip_key.json', 'w') as file:
        file.write(encrypted_data)

def tai_thong_tin_ip():
    try:
        with open('ip_key.json', 'r') as file:
            encrypted_data = file.read()
        data = json.loads(decrypt_data(encrypted_data))
        return data
    except FileNotFoundError:
        return None

def kiem_tra_ip(ip):
    data = tai_thong_tin_ip()
    if data and ip in data:
        expiration_date = datetime.fromisoformat(data[ip]['expiration_date'])
        if expiration_date > datetime.now():
            return data[ip]['key']
    return None

def generate_key_and_url(ip_address):
    ngay = int(datetime.now().day)
    key1 = str(ngay * 27 + 27)
    ip_numbers = ''.join(filter(str.isdigit, ip_address))
    key = f'DANGKHOA_DEV{key1}{ip_numbers}'
    expiration_date = datetime.now().replace(hour=23, minute=59, second=0, microsecond=0)
    url = f'https://www.webkey.x10.mx/?ma={key}'
    return url, key, expiration_date

def da_qua_gio_moi():
    now = datetime.now()
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
    return now >= midnight

def get_shortened_link_phu(url):
    try:
        token = "e5ce8b377f21aa9ea4e38d6a55f44d8048189fee5ca75b4963b200b705622dbd"  # Thay bằng token của bạn
        api_url = f"https://yeumoney.com/QL_api.php?token={token}&format=json&url={url}"

        response = requests.get(api_url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            if data['status'] == 'success':
                return {"status": "success", "shortenedUrl": data['shortenedUrl']}
            else:
                return {"status": "error", "message": "Lỗi khi rút gọn link!"}
        else:
            return {"status": "error", "message": "Không kết nối được với API Yeumoney."}
    except Exception as e:
        return {"status": "error", "message": f"Lỗi: {e}"}


def main():
    ip_address = get_ip_address()
    display_ip_address(ip_address)

    if ip_address:
        existing_key = kiem_tra_ip(ip_address)
        if existing_key:
            print(f"\033[1;97m[>_<] NGUYENDANGKHOA => \033[1;35mTool còn hạn, mời bạn dùng tool...")
            time.sleep(2)
        else:
            if da_qua_gio_moi():
                print("\033[1;33mQuá giờ sử dụng tool !!!")
                return

            url, key, expiration_date = generate_key_and_url(ip_address)

            with ThreadPoolExecutor(max_workers=2) as executor:
                print("\033[2;32m[>_<] NGUYENDANGKHOA => \033[2;32m NHẬP 1 ĐỂ LẤY KEY FREE ")
                print("\033[2;32m[>_<] NGUYENDANGKHOA => \033[2;32m NHẬP 2 ĐỂ NHẬP KEY VĨNH VIỄN ")

                while True:
                    try:
                        choice = input("\033[1;97m[>_<] NGUYENDANGKHOA => \033[1;34mNhập lựa chọn: ")
                        print("\033[97m╚═══════════════════════════════════════════════════════════════════╝")
                        
                        if choice == "1":
                            yeumoney_future = executor.submit(get_shortened_link_phu, url)
                            yeumoney_data = yeumoney_future.result()
                            if yeumoney_data and yeumoney_data.get('status') == "error":
                                print(yeumoney_data.get('message'))
                                return
                            else:
                                link_key_yeumoney = yeumoney_data.get('shortenedUrl')
                                print('\033[1;31;47m[>_<] NGUYENDANGKHOA => \033[1;31;47mLINK ĐỂ VƯỢT KEY LÀ \033[1;36m:', link_key_yeumoney)

                            while True:
                                keynhap = input('\033[5;33;44m[>_<] NGUYENDANGKHOA => \033[5;33;44mKEY ĐÃ VƯỢT LÀ: \033[1;32m')
                                if keynhap == key:
                                    print('Key Đúng Mời Bạn Dùng Tool')
                                    sleep(2)
                                    luu_thong_tin_ip(ip_address, keynhap, expiration_date)
                                    return
                                else:
                                    print('\033[1;97m[>_<] NGUYENDANGKHOA => \033[1;35mKEY SAI VUI LÒNG VƯỢT LẠI LINK \033[1;36m:', link_key_yeumoney)

                        elif choice == "2":
                            keynhap = input('\033[5;33;44m[>_<] NGUYENDANGKHOA => \033[5;33;44mNHẬP KEY VĨNH VIỄN: \033[1;32m')
                            if keynhap == "DANGKHOA_DEV123":
                                print('Key Vĩnh Viễn Đúng Mời Bạn Dùng Tool')
                                sleep(2)
                                luu_thong_tin_ip(ip_address, keynhap, datetime.now() + timedelta(days=3650))  # Lưu key 10 năm
                                return
                            else:
                                print('\033[1;97m[>_<] NGUYENDANGKHOA => \033[1;35mKEY VĨNH VIỄN KHÔNG ĐÚNG !!!')

                        else:
                            print("Lựa chọn không hợp lệ, vui lòng nhập lại.")
                            
                    except ValueError:
                        print("Vui lòng nhập số hợp lệ.")
                    except KeyboardInterrupt:
                        print("\n\033[1;97m[>_<] NGUYENDANGKHOA => \033[1;31m Cảm ơn bạn đã dùng tool !!!")
                        sys.exit()

if __name__ == '__main__':
    main() 


import requests
import random
import string
import hashlib,os

trang = "\033[1;37m\033[1m"
xanh_la = "\033[1;32m\033[1m"
xanh_duong = "\033[1;34m\033[1m"
xanhnhat = '\033[1m\033[38;5;51m'
do = "\033[1;31m\033[1m\033[1m"
xam = '\033[1;30m\033[1m'
vang = "\033[1;33m\033[1m"
tim = "\033[1;35m\033[1m"
hongnhat = "#FFC0CB"
kt_code = "</>"
dac_biet = "\033[32;5;245m\033[1m\033[38;5;39m"
vua = "\033[1;37m[>_<]\033[1;37m \033[1;37mNGUYENDANGKHOA\033[1;37m \033[1;37m=> \033[1;34m\033[1m"

import os
try:
    from faker import Faker
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import pad
    import requests
except ImportError:
    os.system('pip install Faker')
    os.system('pip install requests')
    os.system('pip install pycryptodome')
    
    
#import lại sau khi cài đặt
from faker import Faker
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import requests

trang = "\033[1;37m\033[1m"
xanh_la = "\033[1;32m\033[1m"
xanh_duong = "\033[1;34m\033[1m"
xanhnhat = '\033[1m\033[38;5;51m'
do = "\033[1;31m\033[1m\033[1m"
xam='\033[1;30m\033[1m'
vang = "\033[1;33m\033[1m"
tim = "\033[1;35m\033[1m"
hongnhat = "#FFC0CB"
kt_code = "</>"
dac_biet = "\033[32;5;245m\033[1m\033[38;5;39m"
vua = "\033[1;37m[>_<]\033[1;37m \033[1;37mNGUYENDANGKHOA\033[1;37m \033[1;37m=> \033[1;34m\033[1m"


import os, json, sys, requests 
from sys import platform
from time import sleep
from datetime import datetime
from random import randint
from pystyle import Colors, Colorate
import uuid, re
from bs4 import BeautifulSoup
import os, sys, time, math, random, colorsys

# ────────── KÍCH HOẠT ANSI (Windows) ──────────
if os.name == "nt":
    import ctypes
    kernel32 = ctypes.windll.kernel32
    ENABLE_VT = 0x0004
    handle = kernel32.GetStdHandle(-11)  # STD_OUTPUT_HANDLE = -11
    mode = ctypes.c_ulong()
    if kernel32.GetConsoleMode(handle, ctypes.byref(mode)):
        kernel32.SetConsoleMode(handle, mode.value | ENABLE_VT)

# ────────── HÀM TIỆN ÍCH ──────────
def hsv2rgb(h, s, v): return colorsys.hsv_to_rgb(h, s, v)

def rgb_to_ansi(r, g, b):
    return 16 + (36 * round(r * 5)) + (6 * round(g * 5)) + round(b * 5)

def pastel_rainbow(length, offset=0, bright=0.95, sat=0.42, phase=0):
    return [
        rgb_to_ansi(*hsv2rgb(((i + offset) / (length * 1.2) + phase) % 1, sat, bright))
        for i in range(length)
    ]

def gradient_line(text, colors, sweep=None):
    out = []
    for i, ch in enumerate(text):
        c = colors[i % len(colors)]
        if sweep is not None and abs(i - sweep) < 3:
            out.append(f"\033[1m\033[38;5;{c}m{ch}\033[0m")
        else:
            out.append(f"\033[38;5;{c}m{ch}")
    return "".join(out) + "\033[0m"

def render_frame(f):
    pulse = 0.5 + 0.5 * math.sin(f * 0.03)
    bright = 0.9 + 0.1 * pulse
    sat    = 0.38 + 0.08 * pulse
    sweep  = int((math.sin(f * 0.05) + 1) * max_len // 2)
    phase  = math.sin(f * 0.025) * .25

    lines = []
    for idx, raw in enumerate(logo):
        shift = f + idx * .6
        colors = pastel_rainbow(len(raw), shift, bright, sat, phase)
        lines.append(gradient_line(raw, colors, sweep))
    return lines

def center_text(text, width):
    return text.center(width)

# ────────── LOGO ASCII ──────────
logo = [
    "╔══════════════╤════════════════════════════════════════════════╗",
    "║»» Phiên bản  ☓                Golike TikTok                   ║",
    "╚══════════════╧════════════════════════════════════════════════╝",
    "╔═══════════════════════════════════════════════════════════════╗",
    "║   ████████╗███╗   ███╗  ██╗  ███╗  ██╗██████╗ ██╗  ██╗  ██╗   ║",
    "║   ╚══██╔══╝████╗ ████║  ╚═╝  ████╗ ██║██╔══██╗██║ ██╔╝  ██║   ║",
    "║      ██║   ██╔████╔██║       ██╔██╗██║██║  ██║█████═╝   ██║   ║",
    "║      ██║   ██║╚██╔╝██║       ██║╚████║██║  ██║██╔═██╗   ╚═╝   ║",
    "║      ██║   ██║ ╚═╝ ██║  ██╗  ██║ ╚███║██████╔╝██║ ╚██╗  ██╗   ║",
    "║      ╚═╝   ╚═╝     ╚═╝  ╚═╝  ╚═╝  ╚══╝╚═════╝ ╚═╝  ╚═╝  ╚═╝   ║",
    "╚═══════════════════════════════════════════════════════════════╝"
]
max_len   = max(len(l) for l in logo)
logo_h    = len(logo)
duration  = 3          # giây chạy
delay     = 0.06
frames    = int(duration / delay)
offset    = random.randint(0, 3)

# ────────── BANNER SETUP ──────────
banner_width = max_len + 4
title = "[>_<] NGUYENDANGKHOA /// DANGKHOA_DEV"
footer = "YOUTOBE SHARE TOOL :  https://www.youtube.com/channel/UCGJmaIZ_JbAwoOrHeBZru6A"
start_message = "NHÓM ZALO : https://zalo.me/g/wyboil196"
end_message = """ 
[>_<] NGUYENDANGKHOA                          source by DangKhoa_Dev
══════════════════════════════════════════════════════════════════════
NHÓM ZALO : https://zalo.me/g/wyboil196 
══════════════════════════════════════════════════════════════════════
SHARE TOOL :  https://www.youtube.com/channel/UCGJmaIZ_JbAwoOrHeBZru6A
══════════════════════════════════════════════════════════════════════
----------------------------------------------------------------------
"""
# ────────── IN BANNER ──────────
# Clear screen
print("\033[2J\033[H", end="")

# Print title
title_colors = pastel_rainbow(len(title), offset)
print(center_text(gradient_line(title, title_colors), banner_width))

# Print top border
border = "═" * (banner_width - 2)
print(f"╔{border}╗")

# Print initial logo
first = render_frame(offset)
for line in first:
    print(f"║ {line.ljust(max_len)} ║")

# Print bottom border
print(f"╚{border}╝")

# Print start message
start_colors = pastel_rainbow(len(start_message), offset)
print(center_text(gradient_line(start_message, start_colors), banner_width), flush=True)

# ────────── VÒNG LẶP ANIMATION ──────────
for f in range(1, frames):
    time.sleep(delay)
    # Move cursor to start of logo
    sys.stdout.write(f"\033[{logo_h + 2}F")
    # Print top border
    sys.stdout.write(f"╔{border}╗\n")
    # Print animated logo
    for line in render_frame(f + offset):
        sys.stdout.write(f"║ {line.ljust(max_len)} ║\n")
    # Print bottom border
    sys.stdout.write(f"╚{border}╝\n")
    sys.stdout.flush()

# ────────── KẾT THÚC BANNER & CHUYỂN SANG API ──────────
time.sleep(delay)
# Clear below logo
sys.stdout.write(f"\033[{logo_h + 2}F\033[J")
# Reprint title
print(center_text(gradient_line(title, title_colors), banner_width))
# Reprint top border
print(f"╔{border}╗")
# Print final frame
for line in render_frame(frames + offset):
    print(f"║ {line.ljust(max_len)} ║")
# Reprint bottom border
print(f"╚{border}╝")
# Print transition message
end_colors = pastel_rainbow(len(end_message), offset)
print(center_text(gradient_line(end_message, end_colors), banner_width))
import sys
from time import sleep
def banner(): ""
""

# Nhập auth
try:
  Authorization = open("Authorization.txt","x")
  t = open("token.txt","x")
except:
  pass
Authorization = open("Authorization.txt","r")
t = open("token.txt","r")
author = Authorization.read()
token = t.read()
if author == "":
  author = input("\033[1;97mNHẬP AUTHORIZATION : ")
  token = input("\033[1;31mNHẬP T : ")
  Authorization = open("Authorization.txt","w")
  t = open("token.txt","w")
  Authorization.write(author)
  t.write(token)
else:
  select = input("\033[1;97m║ Đăng\033[1;96m Nhập \033[1;95mTài \033[1;94mKhoản \033[1;93mHiện \033[1;92mCó\033[1;91m ( Enter Để Bỏ Qua ,Nhập AUTHORIZATION Tại Đây \033[1;97m║\033[1;91m Để Đổi )  \n\033[1;97m╚⟩⟩⟩ ")

  if select != "":
    author = select
    token = input("\033[1;36mNhập T : ")
    Authorization = open("Authorization.txt","w")
    t = open("token.txt","w")
    Authorization.write(author)
    t.write(token)
Authorization.close()
t.close()
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json;charset=utf-8',
    'Authorization': author,
    't': token,
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'Referer': 'https://app.golike.net/account/manager/tiktok',
}


def chonacc():
  json_data = {}

  response = requests.get('https://gateway.golike.net/api/tiktok-account', headers=headers, json=json_data).json()
  return response
def nhannv(account_id):

  params = {
    'account_id': account_id,
    'data': 'null',
  }

  json_data = {}

  response = requests.get('https://gateway.golike.net/api/advertising/publishers/tiktok/jobs',params=params,headers=headers,json=json_data,).json()
  return response
def hoanthanh(ads_id,account_id):
  json_data = {
    'ads_id': ads_id,
    'account_id': account_id,
    'async': True,
    'data': None,
  }

  response = requests.post(
    'https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',
    headers=headers,
    json=json_data,
  ).json()
  return response
def baoloi(ads_id,object_id,account_id,loai):
  json_data1 = {
    'description': 'Tôi đã làm Job này rồi',
    'users_advertising_id': ads_id,
    'type': 'ads',
    'provider': 'tiktok',
    'fb_id': account_id,
    'error_type': 6,
  }

  response = requests.post('https://gateway.golike.net/api/report/send', headers=headers, json=json_data1).json()

  json_data = {
    'ads_id': ads_id,
    'object_id': object_id,
    'account_id': account_id,
    'type': loai,
  }

  response = requests.post(
    'https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs',
    headers=headers,
    json=json_data,
  ).json()  
chontktiktok = chonacc()  
def dsacc():
  if(chontktiktok["status"]!=200):
    print("\033[1;34mAuthorization hoặc T sai hãy nhập lại!!!")
    quit()

  for i in range(len(chontktiktok["data"])):
    # print(f'\033[1;97m•[✩]➭\033[1;36m [{i+1}] \033[1;91m=> \033[1;97mTên Tài Khoản┊\033[1;32m㊪ :\033[1;93m {chontktiktok["data"][i]["nickname"]}  ')
    print(f'\033[1;36m[{i+1}] \033[1;36m✈ \033[1;97mTài Khoản┊\033[1;32m㊪ :\033[1;93m {chontktiktok["data"][i]["nickname"]} \033[1;97m|\033[1;31m㊪ :\033[1;32m Hoạt Động')
dsacc() 
while True:
  try:
    luachon = int(input("\033[1;35m\033[1;97m║ Chọn \033[1;96mTài \033[1;95mKhoản \033[1;94mĐể \033[1;93mChạy \n\033[1;97m╚⟩⟩⟩ "))
    while luachon > len((chontktiktok)["data"]):
      luachon = int(input("\033[1;32mAcc Này Không Có Trong Danh Sách , Hãy Nhập Lại : "))
    account_id = chontktiktok["data"][luachon - 1]["id"]
    break  
  except:
    print("\033[1;35mSai Định Dạng !!!") 
while True:
  try:
    delay = int(input("\033[1;97m║ Nhập\033[1;91m Delay \n\033[1;97m╚⟩⟩⟩ "))
    break
  except:
    print("\033[1;31mSai Định Dạng !!!")
while True:
  try: 
    doiacc = int(input("\033[1;97m║ \033[1;99mNhận\033[1;91m Tiền\033[1;96m Thất\033[1;95m Bại\033[1;94m Bao\033[1;93m Nhiu\033[1;92m Lần\033[1;91m Thì\033[1;96m Dừng\033[1;93m \n\033[1;97m╚⟩⟩⟩ "))
    break
  except:
    print("\033[1;31mNhập Vào 1 Số!!!")    
os.system('cls' if os.name== 'nt' else 'clear')    
dem = 0
tong = 0
checkdoiacc = 0
dsaccloi = []
accloi = ""
os.system('cls' if os.name== 'nt' else 'clear')

for x in banner:
  print(x,end = "")
  sleep(0.001)
print(f'\033[1;36m|STT\033[1;97m| \033[1;33mThời gian ┊ \033[1;32mStatus | \033[1;31mType Job | \033[1;32mID Acc | \033[1;32mXu |\033[1;33m Tổng')

while True:
  if checkdoiacc == doiacc:
    dsaccloi.append(chontktiktok["data"][luachon - 1]["nickname"])
    print(f"\033[1;36mCác Acc Tiktok {dsaccloi} Có Vẻ Gặp Vấn Đề Nên Đổi Acc Chạy Đê ")
    dsacc()
    while True:
      try:
        luachon = int(input("\033[1;35m\033[1;97m║ Chọn \033[1;96mTài \033[1;95mKhoản \033[1;94mĐể \033[1;93mChạy \n\033[1;97m╚⟩⟩⟩  "))
        while luachon > len((chontktiktok)["data"]):
          luachon = int(input("\033[1;32mAcc Này Không Có Trong Danh Sách, Hãy Nhập Lại : "))
        account_id = chontktiktok["data"][luachon - 1]["id"]
        checkdoiacc = 0
        break  
      except:
        print("\033[1;35mSai Định Dạng !!!")

     
  print(f'\033[1;97mĐang \033[1;96mLấy \033[1;95mNhiệm \033[1;91mVụ\033[1;93m Follow',end="\r")    
  # while True:
  #     try:  
  #         nhanjob = nhannv(account_id)
  #         break
  #     except:
  #         time.sleep(1)  # Thêm thời gian chờ 1 giây trước khi thử lại
  #         pass
  while True:
    try:
        nhanjob = nhannv(account_id)
        if nhanjob:  # Kiểm tra nếu nhanjob tồn tại và không rỗng
            break  # Thoát khỏi vòng lặp nếu nhận được nhiệm vụ thành công
        else:
            print("\033[1;31mHệ thống đang tính toán jobs dành cho bạn,bấm load jobs lại sau 10 giây !")
    except:
        print("\033[1;31mHệ thống đang tính toán jobs dành cho bạn,bấm load jobs lại sau 10 giây !")
        pass
    time.sleep(1)
  if(nhanjob["status"] == 200):
    ads_id = nhanjob["data"]["id"]
    link = nhanjob["data"]["link"]
    object_id = nhanjob["data"]["object_id"]
    if(nhanjob["data"]["type"] != "follow"):
      baoloi(ads_id,object_id,account_id,nhanjob["data"]["type"])
      continue
    os.system(f"termux-open-url {link}")
    for remaining_time in range(delay, -1, -1):
            colors = [
                "\033[1;37mD\033[1;36ma\033[1;35mn\033[1;32mg \033[1;31mK\033[1;34mh\033[1;33mo\033[1;36ma\033[1;36m🎓 - Tool\033[1;36m Vip \033[1;31m\033[1;32m",
                "\033[1;37mD\033[1;36ma\033[1;35mn\033[1;32mg \033[1;31mK\033[1;34mh\033[1;33mo\033[1;36ma\033[1;36m🎓 - Tool\033[1;36m Vip \033[1;31m\033[1;32m",
                "\033[1;37mD\033[1;36ma\033[1;35mn\033[1;32mg \033[1;31mK\033[1;34mh\033[1;33mo\033[1;36ma\033[1;36m🎓 - Tool\033[1;36m Vip \033[1;31m\033[1;32m",
                "\033[1;37mD\033[1;36ma\033[1;35mn\033[1;32mg \033[1;31mK\033[1;34mh\033[1;33mo\033[1;36ma\033[1;36m🎓 - Tool\033[1;36m Vip \033[1;31m\033[1;32m",
                "\033[1;37mD\033[1;36ma\033[1;35mn\033[1;32mg \033[1;31mK\033[1;34mh\033[1;33mo\033[1;36ma\033[1;36m🎓 - Tool\033[1;36m Vip \033[1;31m\033[1;32m",
                "\033[1;37mD\033[1;36ma\033[1;35mn\033[1;32mg \033[1;31mK\033[1;34mh\033[1;33mo\033[1;36ma\033[1;36m🎓 - Tool\033[1;36m Vip \033[1;31m\033[1;32m",
                "\033[1;37mD\033[1;36ma\033[1;35mn\033[1;32mg \033[1;31mK\033[1;34mh\033[1;33mo\033[1;36ma\033[1;36m🎓 - Tool\033[1;36m Vip \033[1;31m\033[1;32m",
            ]
            for color in colors:
                print(f"\r{color}|{remaining_time}| \033[1;31m", end="")
                time.sleep(0.12)
                        
                        
    print("\r                          \r", end="") 
    print("\033[1;35mĐang Nhận Tiền         ",end = "\r")
# Vòng lặp cố gắng nhận tiền với tối đa 2 lần thử
    max_attempts = 2
    attempts = 0
    nhantien = None

    while attempts < max_attempts:
        try:
            nhantien = hoanthanh(ads_id, account_id)
            if nhantien["status"] == 200:  # Nhận tiền thành công
                break
        except:
            pass  # Bỏ qua ngoại lệ và thử lại nếu có

        attempts += 1  # Tăng số lần thử

    # Kiểm tra kết quả của việc nhận tiền
    if nhantien and nhantien["status"] == 200:
        dem += 1
        tien = nhantien["data"]["prices"]
        tong += tien
        local_time = time.localtime()
        hour = local_time.tm_hour
        minute = local_time.tm_min
        second = local_time.tm_sec
        h = hour
        m = minute
        s = second
        if hour < 10:
            h = "0" + str(hour)
        if minute < 10:
            m = "0" + str(minute)
        if second < 10:
            s = "0" + str(second)

        chuoi = (f"\033[1;31m| \033[1;36m{dem}\033[1;31m\033[1;97m | "
                f"\033[1;33m{h}:{m}:{s}\033[1;31m\033[1;97m | "
                f"\033[1;32msuccess\033[1;31m\033[1;97m | "
                f"\033[1;31m{nhantien['data']['type']}\033[1;31m\033[1;32m\033[1;32m\033[1;97m |"
                f"\033[1;32m Ẩn ID\033[1;97m |\033[1;97m \033[1;32m+{tien} \033[1;97m| "
                f"\033[1;33m{tong}")

        print("                                                    ", end="\r")
        print(chuoi)
        checkdoiacc = 0
    else:
        # Nếu cả 2 lần thử đều thất bại, bỏ qua nhiệm vụ
        while True:
            try:
                baoloi(ads_id, object_id, account_id, nhanjob["data"]["type"])
                print("                                              ", end="\r")
                print("\033[1;31mBỎ QUA NHIỆM VỤ ", end="\r")
                sleep(1)
                checkdoiacc += 1
                break
            except:
                qua = 0
                pass
