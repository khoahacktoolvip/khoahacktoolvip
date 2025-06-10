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

# Màu sắc cho hiển thị
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;39m"
end = '\033[0m'

# ─────────── CÀI ĐẶT ─────────── #
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# ─────────── MÀU CẦU VỒNG MƯỢT ─────────── #
def hsv2rgb(h, s, v):
    return colorsys.hsv_to_rgb(h, s, v)

def rgb_to_ansi(r, g, b):
    return 16 + (36 * round(r * 5)) + (6 * round(g * 5)) + round(b * 5)

def smooth_rainbow(length, offset=0, brightness=1.0, saturation=0.9, phase_offset=0):
    colors = []
    for i in range(length):
        hue = ((i + offset) / (length * 1.2) + phase_offset) % 1.0
        r, g, b = hsv2rgb(hue, saturation, brightness)
        ansi_code = rgb_to_ansi(r, g, b)
        colors.append(ansi_code)
    return colors

# ─────────── GRADIENT LINE + GLOW + SWEEP ─────────── #
def gradient_line(text, colors, light_sweep_pos=None, glow_strength=1):
    result = ""
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        distance = abs(i - light_sweep_pos) if light_sweep_pos is not None else 1000
        if distance < 3:
            intensity = max(0, (3 - distance) / 3) * glow_strength
            result += f"\033[1m\033[38;5;{color}m{char}\033[0m"
        else:
            result += f"\033[38;5;{color}m{char}"
    return result + "\033[0m"

# ─────────── LOGO BREATHING + LIGHT SWEEP ─────────── #
def render_logo_wave(frame, intensity=1):
    global max_logo_length  # Use global to access the variable
    output = ""
    pulse = 0.5 + 0.5 * math.sin(frame * 0.06)  # breathing chậm
    brightness = 0.85 + 0.15 * pulse
    saturation = 0.88 + 0.1 * pulse
    sweep_pos = int((math.sin(frame * 0.1) + 1) * (max_logo_length // 2))
    phase_offset = math.sin(frame * 0.03) * 0.2  # wave động nhẹ

    for i, line in enumerate(logo_lines):
        shift = (frame + i * intensity)
        colors = smooth_rainbow(len(line), shift, brightness, saturation, phase_offset)
        output += gradient_line(line, colors, light_sweep_pos=sweep_pos, glow_strength=1.2) + "\n"
    return output

# ─────────── TYPEWRITER DRIP EFFECT ─────────── #
def typewriter_effect(lines, base_delay=0.015, drip_max=0.03):
    for line in lines:
        output = ""
        start_offset = random.randint(0, 80)
        colors = smooth_rainbow(len(line), offset=start_offset)
        for i, char in enumerate(line):
            output += f"\033[38;5;{colors[i % len(colors)]}m{char}"
            sys.stdout.write("\r" + output + Style.RESET_ALL)
            sys.stdout.flush()
            time.sleep(base_delay + random.uniform(0, drip_max))  # drip
        print()
        time.sleep(0.3)

# ─────────── INTRO FADE-IN + MATRIX WAVE ─────────── #
def show_intro_fadein(lines, fade_steps=12, delay=0.07):
    base_offset = random.randint(0, 80)
    for fade in range(1, fade_steps + 1):
        clear()
        print(render_logo_wave(fade + base_offset))
        print()
        brightness = fade / fade_steps
        saturation = 0.75 + 0.25 * (fade / fade_steps)
        for idx, line in enumerate(lines):
            wave_offset = base_offset + fade * 4 + idx * 3
            phase_offset = math.sin(fade * 0.1 + idx * 0.5) * 0.2
            colors = smooth_rainbow(len(line), offset=wave_offset, brightness=brightness, saturation=saturation, phase_offset=phase_offset)
            light_sweep_pos = int((math.sin(fade * 0.15 + idx) + 1) * (len(line) // 2))
            print(gradient_line(line, colors, light_sweep_pos=light_sweep_pos, glow_strength=0.8))
        time.sleep(delay)

# ─────────── DATA ─────────── #
logo_lines = [
   "████████╗███╗░░░███╗  ██╗  ███╗░░██╗██████╗░██╗░░██╗  ██╗",
   "╚══██╔══╝████╗░████║  ╚═╝  ████╗░██║██╔══██╗██║░██╔╝  ██║",
   "░░░██║░░░██╔████╔██║  ░░░  ██╔██╗██║██║░░██║█████═╝░  ██║",
   "░░░██║░░░██║╚██╔╝██║  ░░░  ██║╚████║██║░░██║██╔═██╗░  ╚═╝",
   "░░░██║░░░██║░╚═╝░██║  ██╗  ██║░╚███║██████╔╝██║░╚██╗  ██╗",
   "░░░╚═╝░░░╚═╝░░░░░╚═╝  ╚═╝  ╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝  ╚═╝"
]

intro_lines = [
    "══════════════════════════════════════════════════════════════════════",
    ">$ Mua key inbox admin",
    "══════════════════════════════════════════════════════════════════════",
    "> Admin        : NGUYỄN ĐĂNG KHOA",
    "> Tik Tok      : @ndk_exploit",
    "> Zalo         : 0963121607",
    "> Telegram     : @dvmxh_toolsvip",
    "> Facebooks    : https://www.facebook.com/nguyen.ang.khoa.798421/",
    "> Group        : https://www.facebook.com/groups/1138876097614502",
    "═══════════════════════════════════════════════════════════════════════",
    "Bản Quyền © Nguyễn Đăng Khoa               Bản Quyền © Nguyễn Đăng Khoa",
    "═══════════════════════════════════════════════════════════════════════",
    "",
]

message_lines = [
   "[DangKhoa_Dev] Cảm Ơn Bạn Đã Đồng Hành Cùng Tool",
    "Chúc bạn gặt hái thành công trong hành trình kiếm tiền của mình!",
    "🔧 Đang Kích hoạt"
]

# Tính max_logo_length toàn cục
max_logo_length = max(len(line) for line in logo_lines)

# ─────────── BANNER ─────────── #
def banner():
    clear()
    typewriter_effect(message_lines)
    animated_banner(frames=60, delay=0.045)
    show_intro_fadein(intro_lines)

def animated_banner(frames=60, delay=0.045):
    start_offset = random.randint(0, 100)
    for f in range(frames):
        clear()
        print(render_logo_wave(f + start_offset))
        time.sleep(delay)

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
        print(f"\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;31mĐịa chỉ IP : {ip_address}")
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
    key = f'NDK{key1}{ip_numbers}'
    expiration_date = datetime.now().replace(hour=23, minute=59, second=0, microsecond=0)
    url = f'https://www.webkey.x10.mx/?ma={key}'
    return url, key, expiration_date

def da_qua_gio_moi():
    now = datetime.now()
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
    return now >= midnight

def get_shortened_link_phu(url):
    """
    Hàm để rút gọn URL bằng một dịch vụ API.
    """
    try:
        token = "6648c8f016f35d42cd052655"  # Thay bằng API Token Của Bạn
        api_url = f"https://link4m.co/api-shorten/v2?api={token}&url={url}"

        response = requests.get(api_url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return {"status": "error", "message": "Không thể kết nối đến dịch vụ rút gọn URL."}
    except Exception as e:
        return {"status": "error", "message": f"Lỗi khi rút gọn URL: {e}"}

def main():
    ip_address = get_ip_address()
    display_ip_address(ip_address)

    if ip_address:
        existing_key = kiem_tra_ip(ip_address)
        if existing_key:
            print(f"\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;35mTool còn hạn, mời bạn dùng tool...")
            time.sleep(2)
        else:
            if da_qua_gio_moi():
                print("\033[1;33mQuá giờ sử dụng tool !!!")
                return

            url, key, expiration_date = generate_key_and_url(ip_address)

            with ThreadPoolExecutor(max_workers=2) as executor:
                print("\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;32mNhập 1 Để Lấy Key \033[1;33m( Free )")

                while True:
                    try:
                        choice = input("\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;34mNhập lựa chọn: ")
                        print("\033[97m════════════════════════════════════════════════")
                        if choice == "1":
                            yeumoney_future = executor.submit(get_shortened_link_phu, url)
                            yeumoney_data = yeumoney_future.result()
                            if yeumoney_data and yeumoney_data.get('status') == "error":
                                print(yeumoney_data.get('message'))
                                return
                            else:
                                link_key_yeumoney = yeumoney_data.get('shortenedUrl')
                                print('\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;35mLink Để Vượt Key Là \033[1;36m:', link_key_yeumoney)

                            while True:
                                keynhap = input('\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;33mKey Đã Vượt Là: \033[1;32m')
                                if keynhap == key:
                                    print('Key Đúng Mời Bạn Dùng Tool')
                                    sleep(2)
                                    luu_thong_tin_ip(ip_address, keynhap, expiration_date)
                                    return
                                else:
                                    print('\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;35mKey Sai Vui Lòng Vượt Lại Link \033[1;36m:', link_key_yeumoney)
                    except ValueError:
                        print("Vui lòng nhập số hợp lệ.")
                    except KeyboardInterrupt:
                        print("\n\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;31mCảm ơn bạn đã dùng Tool !!!")
                        sys.exit()

if __name__ == '__main__':
    main()
    
# ─────────── IMPORT ─────────── #
import os, sys, time, math, random
from colorama import init, Style
import colorsys

init(autoreset=True)

# ─────────── CÀI ĐẶT ─────────── #
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# ─────────── MÀU CẦU VỒNG MƯỢT ─────────── #
def hsv2rgb(h, s, v):
    return colorsys.hsv_to_rgb(h, s, v)

def rgb_to_ansi(r, g, b):
    return 16 + (36 * round(r * 5)) + (6 * round(g * 5)) + round(b * 5)

def smooth_rainbow(length, offset=0, brightness=1.0, saturation=0.9, phase_offset=0):
    colors = []
    for i in range(length):
        hue = ((i + offset) / (length * 1.2) + phase_offset) % 1.0
        r, g, b = hsv2rgb(hue, saturation, brightness)
        ansi_code = rgb_to_ansi(r, g, b)
        colors.append(ansi_code)
    return colors

# ─────────── GRADIENT LINE + GLOW + SWEEP ─────────── #
def gradient_line(text, colors, light_sweep_pos=None, glow_strength=1):
    result = ""
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        distance = abs(i - light_sweep_pos) if light_sweep_pos is not None else 1000
        if distance < 3:
            intensity = max(0, (3 - distance) / 3) * glow_strength
            # tăng sáng nhẹ (bold)
            result += f"\033[1m\033[38;5;{color}m{char}\033[0m"
        else:
            result += f"\033[38;5;{color}m{char}"
    return result + "\033[0m"

# ─────────── LOGO BREATHING + LIGHT SWEEP ─────────── #
def render_logo_wave(frame, intensity=1):
    output = ""
    pulse = 0.5 + 0.5 * math.sin(frame * 0.06)  # breathing chậm
    brightness = 0.85 + 0.15 * pulse
    saturation = 0.88 + 0.1 * pulse
    sweep_pos = int((math.sin(frame * 0.1) + 1) * (max_logo_length // 2))
    phase_offset = math.sin(frame * 0.03) * 0.2  # wave động nhẹ

    for i, line in enumerate(logo_lines):
        shift = (frame + i * intensity)
        colors = smooth_rainbow(len(line), shift, brightness, saturation, phase_offset)
        output += gradient_line(line, colors, light_sweep_pos=sweep_pos, glow_strength=1.2) + "\n"
    return output

def animated_banner(frames=60, delay=0.045):
    start_offset = random.randint(0, 100)
    for f in range(frames):
        clear()
        print(render_logo_wave(f + start_offset))
        time.sleep(delay)

# ─────────── TYPEWRITER DRIP EFFECT ─────────── #
def typewriter_effect(lines, base_delay=0.015, drip_max=0.03):
    for line in lines:
        output = ""
        start_offset = random.randint(0, 80)
        colors = smooth_rainbow(len(line), offset=start_offset)
        for i, char in enumerate(line):
            output += f"\033[38;5;{colors[i % len(colors)]}m{char}"
            sys.stdout.write("\r" + output + Style.RESET_ALL)
            sys.stdout.flush()
            time.sleep(base_delay + random.uniform(0, drip_max))  # drip
        print()
        time.sleep(0.3)

# ─────────── INTRO FADE-IN + MATRIX WAVE ─────────── #
def show_intro_fadein(lines, fade_steps=12, delay=0.07):
    base_offset = random.randint(0, 80)
    for fade in range(1, fade_steps + 1):
        clear()
        print(render_logo_wave(fade + base_offset))
        print()
        brightness = fade / fade_steps
        saturation = 0.75 + 0.25 * (fade / fade_steps)
        for idx, line in enumerate(lines):
            wave_offset = base_offset + fade * 4 + idx * 3
            phase_offset = math.sin(fade * 0.1 + idx * 0.5) * 0.2
            colors = smooth_rainbow(len(line), offset=wave_offset, brightness=brightness, saturation=saturation, phase_offset=phase_offset)
            light_sweep_pos = int((math.sin(fade * 0.15 + idx) + 1) * (len(line) // 2))
            print(gradient_line(line, colors, light_sweep_pos=light_sweep_pos, glow_strength=0.8))
        time.sleep(delay)

# ─────────── DATA ─────────── #
logo_lines = [
   "████████╗███╗░░░███╗  ██╗  ███╗░░██╗██████╗░██╗░░██╗  ██╗",
   "╚══██╔══╝████╗░████║  ╚═╝  ████╗░██║██╔══██╗██║░██╔╝  ██║",
   "░░░██║░░░██╔████╔██║  ░░░  ██╔██╗██║██║░░██║█████═╝░  ██║",
   "░░░██║░░░██║╚██╔╝██║  ░░░  ██║╚████║██║░░██║██╔═██╗░  ╚═╝",
   "░░░██║░░░██║░╚═╝░██║  ██╗  ██║░╚███║██████╔╝██║░╚██╗  ██╗",
   "░░░╚═╝░░░╚═╝░░░░░╚═╝  ╚═╝  ╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝  ╚═╝"
]

intro_lines = [
    "══════════════════════════════════════════════════════════════════════",
    ">$ Mua key inbox admin",
    "══════════════════════════════════════════════════════════════════════",
    "> Admin        : NGUYỄN ĐĂNG KHOA",
    "> Tik Tok      : @ndk_exploit",
    "> Zalo         : 0963121607",
    "> Telegram     : @dvmxh_toolsvip",
    "> Facebooks    : https://www.facebook.com/nguyen.ang.khoa.798421/",
    "> Group        : https://www.facebook.com/groups/1138876097614502",
    "═══════════════════════════════════════════════════════════════════════",
    "Bản Quyền © Nguyễn Đăng Khoa               Bản Quyền © Nguyễn Đăng Khoa",
    "═══════════════════════════════════════════════════════════════════════",
    "",
]

message_lines = [
   "[DangKhoa_Dev] Cảm Ơn Bạn Đã Đồng Hành Cùng Tool",
    "Chúc bạn gặt hái thành công trong hành trình kiếm tiền của mình!",
    "🔧 Đang Kích hoạt"
]

# ─────────── MAIN ─────────── #
if __name__ == "__main__":
    max_logo_length = max(len(line) for line in logo_lines)
    clear()
    typewriter_effect(message_lines)
    animated_banner()
    show_intro_fadein(intro_lines)




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
                "\033[1;37mD\033[1;36ma\033[1;35mn\033[1;32mg\033[1;31mK\033[1;37mh\033[1;37mo\033[1;37ma\033[1;37m_\033[1;37mD\033[1;37me\033[1;37mv \033[1;34mD\033[1;33me\033[1;36mv\033[1;36m🚀 - Tool\033[1;36m Vip \033[1;31m\033[1;32m",
                "\033[1;37mD\033[1;36ma\033[1;35mn\033[1;32mg\033[1;31mK\033[1;37mh\033[1;37mo\033[1;37ma\033[1;37m_\033[1;37mD\033[1;37me\033[1;37mv \033[1;34mD\033[1;33me\033[1;36mv\033[1;36m🚀 - Tool\033[1;36m Vip \033[1;31m\033[1;32m",
                "\033[1;37mD\033[1;36ma\033[1;35mn\033[1;32mg\033[1;31mK\033[1;37mh\033[1;37mo\033[1;37ma\033[1;37m_\033[1;37mD\033[1;37me\033[1;37mv \033[1;34mD\033[1;33me\033[1;36mv\033[1;36m🚀 - Tool\033[1;36m Vip \033[1;31m\033[1;32m",
                "\033[1;37mD\033[1;36ma\033[1;35mn\033[1;32mg\033[1;31mK\033[1;37mh\033[1;37mo\033[1;37ma\033[1;37m_\033[1;37mD\033[1;37me\033[1;37mv \033[1;34mD\033[1;33me\033[1;36mv\033[1;36m🚀 - Tool\033[1;36m Vip \033[1;31m\033[1;32m",
                "\033[1;37mD\033[1;36ma\033[1;35mn\033[1;32mg\033[1;31mK\033[1;37mh\033[1;37mo\033[1;37ma\033[1;37m_\033[1;37mD\033[1;37me\033[1;37mv \033[1;34mD\033[1;33me\033[1;36mv\033[1;36m🚀 - Tool\033[1;36m Vip \033[1;31m\033[1;32m",
                "\033[1;37mD\033[1;36ma\033[1;35mn\033[1;32mg\033[1;31mK\033[1;37mh\033[1;37mo\033[1;37ma\033[1;37m_\033[1;37mD\033[1;37me\033[1;37mv \033[1;34mD\033[1;33me\033[1;36mv\033[1;36m🚀 - Tool\033[1;36m Vip \033[1;31m\033[1;32m",
                "\033[1;37mD\033[1;36ma\033[1;35mn\033[1;32mg\033[1;31mK\033[1;37mh\033[1;37mo\033[1;37ma\033[1;37m_\033[1;37mD\033[1;37me\033[1;37mv \033[1;34mD\033[1;33me\033[1;36mv\033[1;36m🚀 - Tool\033[1;36m Vip \033[1;31m\033[1;32m",                                                                                
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


<!---
khoahacktoolvip/khoahacktoolvip is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
