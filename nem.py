import re
import platform

import execjs
import requests

from utils import *

# ===================================================================================================================================================================== #

api_url = "https://music.163.com/weapi/song/enhance/player/url/v1"

headers = {
    "Origin": "https://music.163.com",
    "Referer": "https://music.163.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
}

params = {"csrf_token": ""}


# ===================================================================================================================================================================== #
class GetSongIdError(Exception):
    pass


class GetDataError(Exception):
    pass


class GetResponseError(Exception):
    pass


class GetAudioUrlError(Exception):
    pass


class DownloadAudioError(Exception):
    pass


# ===================================================================================================================================================================== #


def get_song_id(url: str) -> str:
    try:
        # 正则匹配出歌曲的id
        return re.findall(r"song\?id=(\d+)", url)[0]
    except:
        raise GetSongIdError


def get_data(song_id: str) -> dict:
    try:
        # 调用js代码来加密表单数据
        javascript = execjs.compile(
            open("./scripts/nem.js", "r", encoding="utf-8").read()
        )
        return javascript.call("main", song_id)
    except:
        raise GetDataError


def get_response(data: dict) -> dict:
    try:
        # 向服务器请求audio的url
        response = requests.post(url=api_url, params=params, headers=headers, data=data)
        return response.json()
    except:
        raise GetResponseError


def get_audio_url(res: dict) -> str:
    try:
        # 解析响应并提取出audio的url
        if res["code"] == 200:
            return res["data"][0]["url"]
        else:
            error("The data's response code is not ok!")
    except:
        raise GetAudioUrlError


def download_audio(url: str):
    try:
        # 下载audio
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            audio_name = url.split("/")[-1]
            download_audio_path = (
                f"{download_path}\\{audio_name}"
                if platform.system() == "Windows"
                else f"{download_path}/{audio_name}"
            )
            with open(download_audio_path, "wb") as f:
                f.write(response.content)
            info(f"Downloaded audio to {download_audio_path}")
        else:
            error("The audio's response code is not ok!")
    except:
        raise DownloadAudioError


# ===================================================================================================================================================================== #


def neteasemusic(url: str):
    try:

        song_id: str = get_song_id(url)
        data: dict = get_data(song_id)
        response: dict = get_response(data)
        audio_url: str = get_audio_url(response)
        download_audio(audio_url)

    except GetSongIdError:
        error("Failed to get the song's id!")
    except GetDataError:
        error("Failed to get the form data!")
    except GetResponseError:
        error("Failed to get the response!")
    except GetAudioUrlError:
        error("Failed to get the audio's url!")
    except DownloadAudioError:
        error("Failed to download!")


# test
if __name__ == "__main__":
    neteasemusic("https://music.163.com/song?id=1827591485&userid=1932124612")
