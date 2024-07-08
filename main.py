import platform
import subprocess
import sys
# from pyfiglet import Figlet
import time

def get_windows_version():
    version = platform.version()
    release = platform.release()
    system = platform.system()
    version_info = {
        "system": system,
        "release": release,
        "version": version
    }
    return version_info

def get_windows_edition():
    try:
        cmd = 'powershell "Get-WmiObject -Class Win32_OperatingSystem | Select-Object Caption, Version"'
        output = subprocess.check_output(cmd, shell=True, text=True)
        lines = output.strip().split('\n')
        lines = [line.strip() for line in lines if line.strip()]
        if len(lines) >= 3:
            caption, version = lines[2].rsplit(' ', 1)
            edition_info = {
                "Caption": caption.strip(),
                "Version": version.strip()
            }
        else:
            edition_info = {
                "error": "Unable to parse edition information"
            }
    except Exception as e:
        edition_info = {
            "error": str(e)
        }
    return edition_info

def kms_activate(edition):
    try:
        if edition == "Microsoft Windows 11 Pro":
            kms_cmd = 'slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX'
        elif edition == "Microsoft Windows 11 Home":
            kms_cmd = 'slmgr /ipk TX9XD-98N7V-6WMQ6-BX7FG-H8Q99'
        elif edition == "Microsoft Windows 10 Pro":
            kms_cmd = 'slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX'
        elif edition == "Microsoft Windows 10 Home":
            kms_cmd = 'slmgr /ipk TX9XD-98N7V-6WMQ6-BX7FG-H8Q99'
        else:
            print("ERROR: 알맞는 KMS Key를 찾을 수 없습니다.\n프로그램을 종료합니다.")
            sys.exit(0)
        
        # 실제 KMS 서버 주소로 변경 필요
        kms_server_cmd = 'slmgr /skms kms.srv.crsoo.com' # 작동 안될시 변경 바람
        kms_activate_cmd = 'slmgr /ato'
        
        subprocess.check_output(kms_cmd, shell=True)
        subprocess.check_output(kms_server_cmd, shell=True)
        activation_output = subprocess.check_output(kms_activate_cmd, shell=True, text=True)
        
        print(f"KMS Activation Output for {edition}:\n{activation_output}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to activate {edition}: {str(e)}")


# f = Figlet(font='slant')
# print(f.renderText('OctaX KMS Auto'))
print("""
  ___       _       __  __  _  ____  __ ____       _         _        
 / _ \  ___| |_ __ _\ \/ / | |/ /  \/  / ___|     / \  _   _| |_ ___  
| | | |/ __| __/ _` |\  /  | ' /| |\/| \___ \    / _ \| | | | __/ _ \ 
| |_| | (__| || (_| |/  \  | . \| |  | |___) |  / ___ \ |_| | || (_) |
 \___/ \___|\__\__,_/_/\_\ |_|\_\_|  |_|____/  /_/   \_\__,_|\__\___/ 
""")
print("Copyright 2024. Gaegeumchi & OctaX. all rights reserved.")
print("V 0.0.1 Beta")
print("Made By Gaegeumchi")
print("")
print("Loading...")
time.sleep(2)

windows_version = get_windows_version()
windows_edition = get_windows_edition()

print("")
print("감지된 윈도우 버전:", windows_edition.get("Caption", "N/A"))
print("")
print("감지한 윈도우 버전이 실제 윈도우 버전과 일치하나요?")
vq = input("Y/N: ")

if vq.upper() == "Y":
    print("수행할 작업을 선택해주세요")
    print("0 윈도우 정품인증")
    wi = input("Select Number: ")
    if wi == "0":
        print("윈도우 정품 인증을 시작합니다")
        edition = windows_edition.get("Caption", "N/A")
        kms_activate(edition)
    else:
        print("알수 없는 번호입니다. 프로그램을 종료합니다.")
        sys.exit(0)
elif vq.upper() == "N":
    print("수동으로 윈도우 버전을 입력해주세요. ex) Microsoft Windows 10 Pro")
    cwv = input("Version: ")
    print("윈도우 정품 인증을 시작합니다")
    edition = cwv
    kms_activate(edition)
else:
    print("프로그램을 종료합니다.")
    sys.exit(0)

input("Press Enter to exit...")
