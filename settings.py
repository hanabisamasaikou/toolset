import os
import platform

types = {
    "BiliBili": "https://www.bilibili.com/video/",
    "NetEaseMusic": "https://music.163.com/song",
}

user_path = os.path.expanduser("~")


download_path = (
    user_path + "\\Downloads"
    if platform.system() == "Windows"
    else user_path + "/Downloads"
)
