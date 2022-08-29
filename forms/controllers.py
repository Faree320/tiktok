import requests
import os
from urllib.request import Request, urlopen
import urllib
from bs4 import BeautifulSoup
import json
import random
from moviepy.editor import VideoFileClip, concatenate_videoclips, clips_array
import cv2
import datetime


def get_links(params):
    print(params)
    links = []
    covers = []
    cookies = {"passport_csrf_token": "24d3cf05dcfd2eb4eb5e36bd0a1916f1; passport_csrf_token_default=24d3cf05dcfd2eb4eb5e36bd0a1916f1; __tea_cache_tokens_1988={%22user_unique_id%22:%227130525750311257602%22%2C%22timestamp%22:1660295754860%2C%22_type_%22:%22default%22}; cmpl_token=AgQQAPO4F-RO0rCObg9uv907-JUuV6aLP4AzYMXW9g; passport_auth_status=373931e3ade6dda24eeea7d0aaa7401d%2Ce0de0ee68a30a8e706a8e263db3c5965; passport_auth_status_ss=373931e3ade6dda24eeea7d0aaa7401d%2Ce0de0ee68a30a8e706a8e263db3c5965; sid_guard=2521529f814bfa493a3c78728bb9a75d%7C1660569732%7C5184000%7CFri%2C+14-Oct-2022+13%3A22%3A12+GMT; uid_tt=5951779a07e06f1355e0d19b6eb773cc956edc3674c90c42f25edbc37de07cdd; uid_tt_ss=5951779a07e06f1355e0d19b6eb773cc956edc3674c90c42f25edbc37de07cdd; sid_tt=2521529f814bfa493a3c78728bb9a75d; sessionid=2521529f814bfa493a3c78728bb9a75d; sessionid_ss=2521529f814bfa493a3c78728bb9a75d; sid_ucp_v1=1.0.0-KDdiMDI4MDRjOTBiYzRhODI0ZDA5YWZkZGFmYWU1MzNlMmIzNzQ2NDYKHwiCiLS0jpWg2GAQhJHplwYYswsgDDDWpsKFBjgIQBIQAxoGbWFsaXZhIiAyNTIxNTI5ZjgxNGJmYTQ5M2EzYzc4NzI4YmI5YTc1ZA; ssid_ucp_v1=1.0.0-KDdiMDI4MDRjOTBiYzRhODI0ZDA5YWZkZGFmYWU1MzNlMmIzNzQ2NDYKHwiCiLS0jpWg2GAQhJHplwYYswsgDDDWpsKFBjgIQBIQAxoGbWFsaXZhIiAyNTIxNTI5ZjgxNGJmYTQ5M2EzYzc4NzI4YmI5YTc1ZA; store-idc=useast2a; store-country-code=pk; tt-target-idc=alisg; _abck=9E413CE6509575293B9D2CD825C1DAA7~-1~YAAQD5ywtj1qj5aCAQAAFqYypQiUoLVbqQQgPl3XgpzGWXyODX+2+MY0UhOi30JXpgAWHg2wDzr4aGoyr2o05Y/p/X5GzKVaX6GylirRv4ZeMKADpsThY9Uqf7/sh8wgJWprQwA1i4bnRAL3ZNLS+g+sDlFZU8F+QcdVj0tAvoa+vyJLDZD05EHUTYKSn8OESwsIxr4cHOPPGuEOkdTHPSaSbQqFcKeQIT6asHBDv8VQFJ6kuGl1e+LChnFMB4suhBGaZHZgppUMGlUUZKNzM1/dUC702RZ+SZeqqjLmWyXVQvD69IOpaAnRcacnn6lmh41GfCSU0mU/0dnECoOFHJMKbftRudmpWumc/xR6HrkqOUqNR+KlgkGWXZVFK6vu+nqL2ixB57kJKw==~-1~-1~-1; bm_sz=502E80472648817979D780C33282AFD2~YAAQD5ywtj5qj5aCAQAAFqYypRCvvb7tQvMRpTLNOjyX2Km3+xIdCE1e6TTojMASGMK+2iwwN91Yx0PWdj89kdD2A1jl4dL8iI8PidXZ2lzMVE5gRc/0G6lpGfuOaOUtbu3sXYW3fgffWB5D+GOnH5qySbOKK/n+aCBWxjIhelPt9EDWkWokW+fI6DnYKMr05dsZ2O74AXZENCWCtITtGWg0pygtki02V8RT45XvCHxRIKdWvjb8j+ZsXSnc725lc3ULJXCqdLUoGPI5FXV/AOpuyqlAuZ1oniS5g85r3qZS+io=~3683123~3162947; ak_bmsc=61E5532B3CCCD8A70CEA1AF7DC8631F9~000000000000000000000000000000~YAAQD5ywtnpqj5aCAQAAeh4zpRBahV+b1/J+smDuxlIFM1xx1UPS4CyzMSKQ7CT58mrHpiKlxVH9oFRsgh1PBBK+OzSgsbmZ5qQVAvECKKqAy6a7qVc26QvWZPAyBnzgXsIcfVr8hb5Sn4F/hIg75GijQ1xopyIBBx0rvt2rg9fkQsWqkG5Z5q4GK0Rn3DbFXSyV8O6cCeCw3RCrquINKwUQXhv0F/VeyqP37VBhL0ufWZz2gSdPIZLDI0Yq22q3tSssRZHDpWQCI5CeXiNRJ7zGx4m90p0ZuApK2d6RmdTRg293yzWRKfZr5C9F2eZ0igIBl7KSCvz1xbbez/cLlirt8ImadoGEO7Pa2PCFtQwbSTGza3wHetoKFoVkOYIoCOG1sTF049V8IA==; tt_csrf_token=GXMkC0Zo-fQGBDDU7od1gtVP0VdYKAC9UZ_c; passport_fe_beating_status=true; odin_tt=e6b54787a2721aa91cf808ac8559abd397443c82e7b03d3e02128daac8b70385cb4eb8b07b4647476641a25da51867bc6632c69484e7e627fe6f4b3a4e42939d5648ff976fea5503ed3a077c3eb57fee; ttwid=1%7C5aHP662LIIjOmzFdf7FK29RhSiBxMhgny-m41kDwKi0%7C1660635600%7Cab3cc40f68cd837c90b1249122a84b6d80b8f93d610693f66823b8c97644e292; msToken=J5UWCvmNkaaBPTWKuMFI1KrzY-xeENg4c-REPwa8Lg0KWUFvcpBm1jnqPF1d5SN7_uWYoVD4WnaPr1Ur69F5Bky6O1qcALOi686NChle-tcokNTyhUNCLvQFpTV2Xvk-4f5FjU9fF4oUZcpr4A==; msToken=sg1GsxSxYlfgVrOJkWnyui2L-IMN1Irp22UekOysfIBmsHSnSk30nZeB81HwpbPU0WRWqKMZiM1N4pd-zr--VthOmyN_rMckcwYJA59WVqJBGZ3imSSQx3sN6kdJtv-PtJ2yKh0wV5DXb_fAaQ==; bm_sv=A734D6606B4ED005BD0C601D9E48294B~YAAQFlxnO8xtKWWCAQAAOYOZpRAzeFsedDWmntQEkukaMB34ncFa/8iwvSedc35gSQSKezhHbtKIhTpipxWRpT51slWRhOvaGaucTh27kNJUN/oec9VPdPo3KaYhP5f1+lFStCsK0JduAr6UmAdhUbGZGFYh/uFqAIvzsMv4Ri6yx9kQDLXqMBR7IgfJ8T/2kvuzFEngWdOetsc3kLkNqNV1IjZYjZk8FK4UYyciV2GHxDhJI2gEE38G0Pk5KTQh2w==~1"}
    if params is None:
        print("I am If")
        url = "https://www.tiktok.com/api/recommend/item_list/?aid=1988&app_language=en&app_name=tiktok_web&battery_info=0.83&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F104.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&count=30&device_id=7130525750311257602&device_platform=web_pc&focus_state=false&from_page=fyp&history_len=5&is_fullscreen=false&is_page_visible=true&os=windows&priority_region=PK&referer=&region=PK&screen_height=720&screen_width=1280&tz_name=Asia%2FKarachi&webcast_language=en&msToken=vZ2O6wUp2EWEqzKB_KvwFqItDyADbQtAdbMPw0rhAJdk8GFRWmZvwzZo4BWWIi-luMxs4qfVeIhT3WoBQB8MWi6ilNtsfLKP2W9iH4ig97f5STdb93brQuQgC5S--jvKrUuRhTs6Iso7pspxPVQ=&X-Bogus=DFSzswjYza2ANrJgS6CKKOYklT6E&_signature=_02B4Z6wo000012fhGYwAAIDCuZdBKEgofFdn4RUAALsOed"
        res = requests.get(url, cookies=cookies)
        j_res = res.json()
        print(j_res["statusCode"])
        link_list = j_res["itemList"]
        for i in link_list:
            # data = cv2.VideoCapture(i['video']['playAddr'])
            #
            # frames = data.get(cv2.CAP_PROP_FRAME_COUNT)
            # fps = data.get(cv2.CAP_PROP_FPS)

            # calculate duration of the video
            # seconds = round(frames / fps)
            # video_time = datetime.timedelta(seconds=seconds)
            # print(f"duration in seconds: {seconds}")
            # print(f"video time: {video_time}")
            links.append(i['video']['playAddr'])
            covers.append(i["video"]['dynamicCover'])
        return links, covers
    elif 'https://www.tiktok.com/music' in params:
        # covers = []
        #
        # headers = {
        #     "x-tt-params": f"{params}"}
        # res = requests.get(
        #     'https://www.tiktok.com/api/music/item_list/?aid=1988&app_language=en&app_name=tiktok_web&battery_info=0.32&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F104.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&device_id=7130525750311257602&device_platform=web_pc&focus_state=true&from_page=music&history_len=7&is_fullscreen=false&is_page_visible=true&os=windows&priority_region=PK&referer=&region=PK&screen_height=720&screen_width=1280&tz_name=Asia%2FKarachi&webcast_language=en&msToken=rYipv0pWXZXFpxCUHqErYA00z79wRMZBX8sRlTOPlOyCcpI8bqoLpvM_UJjMYB4l8FUvx48DLzcWSiilPk9D99u8uwiUsUipvkbHmxLbyx3RDqIeAIFfrdDrd34lXnwYHhhmyaX_0uWkP5KD2A==&X-Bogus=DFSzswVOJL0ANcvUSBn-rQYklT6O&_signature=_02B4Z6wo00001LPoPJAAAIDBbZ5kNcHmwWyz6DgAAE.35b',
        #     cookies=cookies, headers=headers)
        #
        # j_res = res.json()
        # print(j_res["statusCode"])
        # link_list = j_res["itemList"]
        # for i in link_list:
        #     links.append(i['video']['playAddr'])
        # for i in link_list:
        #     covers.append(i["video"]['dynamicCover'])
        headers = {
            "user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36"}
        res = requests.get(f'{params}', cookies=cookies,
                           headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")
        a = soup.find("script", attrs={"id": "SIGI_STATE"})
        try:
            length = json.loads(a.text)['MobileItemModule']
            for i in length:
                links_arr = length[i]['video']['playAddr']
                cover_arr = length[i]['video']['dynamicCover']
                if "https://v16-webapp.tiktok.com" in links_arr:
                    links.append(links_arr)
                    covers.append(cover_arr)
        except KeyError:
            pass
        print(covers)
        print(links)
        return links, covers
    else:
        print("I am else")
        url = f"https://t.tiktok.com/api/search/general/full/?aid=1988&app_language=en&app_name=tiktok_web&battery_info=0.92&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F104.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&device_id=7130525750311257602&device_platform=web_pc&focus_state=true&from_page=search&history_len=6&is_fullscreen=false&is_page_visible=true&keyword={params}&offset=12&os=windows&priority_region=PK&referer=&region=PK&screen_height=720&screen_width=1280"
        res = requests.get(url, cookies=cookies).json()
        link_list = res["data"]
        for i in link_list:
            try:
                links.append(i["item"]["video"]["playAddr"])
                covers.append(i["item"]["video"]["dynamicCover"])
                # print("hi")
            except KeyError:
                pass
        return links, covers


def merdge(data, PATH_1, PATH_2, PATH_3):
    urllib.request.urlretrieve(data[1], PATH_1)
    urllib.request.urlretrieve(data[2], PATH_2)
    urllib.request.urlretrieve(data[3], PATH_3)
    clip1 = VideoFileClip("./static/video/your_video_name1.mp4", audio=True).subclip(0, 7)
    clip2 = VideoFileClip("./static/video/your_video_name2.mp4", audio=True).subclip(0, 7)
    clip3 = VideoFileClip("./static/video/your_video_name3.mp4", audio=True).subclip(0, 7)
    final_clip = clips_array([[clip1, clip2, clip3]])
    final_clip.write_videofile(f"./static/video/merged.mp4")
    try:
        os.remove(PATH_1)
        os.remove(PATH_2)
        os.remove(PATH_3)
    except PermissionError:
        print('as expected')
    clip1.close()
    clip2.close()
    clip3.close()
    try:
        os.remove(PATH_1)
        os.remove(PATH_2)
        os.remove(PATH_3)
        print('success')
    except PermissionError:
        print('you will not see this')


def auto_generator_c(params, PATH_1, PATH_2, PATH_3):
    links = []
    covers = []
    cookies = {
        "passport_csrf_token": "24d3cf05dcfd2eb4eb5e36bd0a1916f1; passport_csrf_token_default=24d3cf05dcfd2eb4eb5e36bd0a1916f1; __tea_cache_tokens_1988={%22user_unique_id%22:%227130525750311257602%22%2C%22timestamp%22:1660295754860%2C%22_type_%22:%22default%22}; cmpl_token=AgQQAPO4F-RO0rCObg9uv907-JUuV6aLP4AzYMXW9g; passport_auth_status=373931e3ade6dda24eeea7d0aaa7401d%2Ce0de0ee68a30a8e706a8e263db3c5965; passport_auth_status_ss=373931e3ade6dda24eeea7d0aaa7401d%2Ce0de0ee68a30a8e706a8e263db3c5965; sid_guard=2521529f814bfa493a3c78728bb9a75d%7C1660569732%7C5184000%7CFri%2C+14-Oct-2022+13%3A22%3A12+GMT; uid_tt=5951779a07e06f1355e0d19b6eb773cc956edc3674c90c42f25edbc37de07cdd; uid_tt_ss=5951779a07e06f1355e0d19b6eb773cc956edc3674c90c42f25edbc37de07cdd; sid_tt=2521529f814bfa493a3c78728bb9a75d; sessionid=2521529f814bfa493a3c78728bb9a75d; sessionid_ss=2521529f814bfa493a3c78728bb9a75d; sid_ucp_v1=1.0.0-KDdiMDI4MDRjOTBiYzRhODI0ZDA5YWZkZGFmYWU1MzNlMmIzNzQ2NDYKHwiCiLS0jpWg2GAQhJHplwYYswsgDDDWpsKFBjgIQBIQAxoGbWFsaXZhIiAyNTIxNTI5ZjgxNGJmYTQ5M2EzYzc4NzI4YmI5YTc1ZA; ssid_ucp_v1=1.0.0-KDdiMDI4MDRjOTBiYzRhODI0ZDA5YWZkZGFmYWU1MzNlMmIzNzQ2NDYKHwiCiLS0jpWg2GAQhJHplwYYswsgDDDWpsKFBjgIQBIQAxoGbWFsaXZhIiAyNTIxNTI5ZjgxNGJmYTQ5M2EzYzc4NzI4YmI5YTc1ZA; store-idc=useast2a; store-country-code=pk; tt-target-idc=alisg; _abck=9E413CE6509575293B9D2CD825C1DAA7~-1~YAAQD5ywtj1qj5aCAQAAFqYypQiUoLVbqQQgPl3XgpzGWXyODX+2+MY0UhOi30JXpgAWHg2wDzr4aGoyr2o05Y/p/X5GzKVaX6GylirRv4ZeMKADpsThY9Uqf7/sh8wgJWprQwA1i4bnRAL3ZNLS+g+sDlFZU8F+QcdVj0tAvoa+vyJLDZD05EHUTYKSn8OESwsIxr4cHOPPGuEOkdTHPSaSbQqFcKeQIT6asHBDv8VQFJ6kuGl1e+LChnFMB4suhBGaZHZgppUMGlUUZKNzM1/dUC702RZ+SZeqqjLmWyXVQvD69IOpaAnRcacnn6lmh41GfCSU0mU/0dnECoOFHJMKbftRudmpWumc/xR6HrkqOUqNR+KlgkGWXZVFK6vu+nqL2ixB57kJKw==~-1~-1~-1; bm_sz=502E80472648817979D780C33282AFD2~YAAQD5ywtj5qj5aCAQAAFqYypRCvvb7tQvMRpTLNOjyX2Km3+xIdCE1e6TTojMASGMK+2iwwN91Yx0PWdj89kdD2A1jl4dL8iI8PidXZ2lzMVE5gRc/0G6lpGfuOaOUtbu3sXYW3fgffWB5D+GOnH5qySbOKK/n+aCBWxjIhelPt9EDWkWokW+fI6DnYKMr05dsZ2O74AXZENCWCtITtGWg0pygtki02V8RT45XvCHxRIKdWvjb8j+ZsXSnc725lc3ULJXCqdLUoGPI5FXV/AOpuyqlAuZ1oniS5g85r3qZS+io=~3683123~3162947; ak_bmsc=61E5532B3CCCD8A70CEA1AF7DC8631F9~000000000000000000000000000000~YAAQD5ywtnpqj5aCAQAAeh4zpRBahV+b1/J+smDuxlIFM1xx1UPS4CyzMSKQ7CT58mrHpiKlxVH9oFRsgh1PBBK+OzSgsbmZ5qQVAvECKKqAy6a7qVc26QvWZPAyBnzgXsIcfVr8hb5Sn4F/hIg75GijQ1xopyIBBx0rvt2rg9fkQsWqkG5Z5q4GK0Rn3DbFXSyV8O6cCeCw3RCrquINKwUQXhv0F/VeyqP37VBhL0ufWZz2gSdPIZLDI0Yq22q3tSssRZHDpWQCI5CeXiNRJ7zGx4m90p0ZuApK2d6RmdTRg293yzWRKfZr5C9F2eZ0igIBl7KSCvz1xbbez/cLlirt8ImadoGEO7Pa2PCFtQwbSTGza3wHetoKFoVkOYIoCOG1sTF049V8IA==; tt_csrf_token=GXMkC0Zo-fQGBDDU7od1gtVP0VdYKAC9UZ_c; passport_fe_beating_status=true; odin_tt=e6b54787a2721aa91cf808ac8559abd397443c82e7b03d3e02128daac8b70385cb4eb8b07b4647476641a25da51867bc6632c69484e7e627fe6f4b3a4e42939d5648ff976fea5503ed3a077c3eb57fee; ttwid=1%7C5aHP662LIIjOmzFdf7FK29RhSiBxMhgny-m41kDwKi0%7C1660635600%7Cab3cc40f68cd837c90b1249122a84b6d80b8f93d610693f66823b8c97644e292; msToken=J5UWCvmNkaaBPTWKuMFI1KrzY-xeENg4c-REPwa8Lg0KWUFvcpBm1jnqPF1d5SN7_uWYoVD4WnaPr1Ur69F5Bky6O1qcALOi686NChle-tcokNTyhUNCLvQFpTV2Xvk-4f5FjU9fF4oUZcpr4A==; msToken=sg1GsxSxYlfgVrOJkWnyui2L-IMN1Irp22UekOysfIBmsHSnSk30nZeB81HwpbPU0WRWqKMZiM1N4pd-zr--VthOmyN_rMckcwYJA59WVqJBGZ3imSSQx3sN6kdJtv-PtJ2yKh0wV5DXb_fAaQ==; bm_sv=A734D6606B4ED005BD0C601D9E48294B~YAAQFlxnO8xtKWWCAQAAOYOZpRAzeFsedDWmntQEkukaMB34ncFa/8iwvSedc35gSQSKezhHbtKIhTpipxWRpT51slWRhOvaGaucTh27kNJUN/oec9VPdPo3KaYhP5f1+lFStCsK0JduAr6UmAdhUbGZGFYh/uFqAIvzsMv4Ri6yx9kQDLXqMBR7IgfJ8T/2kvuzFEngWdOetsc3kLkNqNV1IjZYjZk8FK4UYyciV2GHxDhJI2gEE38G0Pk5KTQh2w==~1"}
    headers = {
        "user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36"}
    res = requests.get(f'{params}', cookies=cookies,
                       headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    a = soup.find("script", attrs={"id": "SIGI_STATE"})
    try:
        length = json.loads(a.text)['MobileItemModule']
        for i in length:
            links_arr = length[i]['video']['playAddr']
            cover_arr = length[i]['video']['dynamicCover']
            if "https://v16-webapp.tiktok.com" in links_arr:
                if len(links) < 3:
                    links.append(links_arr)
                    covers.append(cover_arr)
                else:
                    break
    except KeyError:
        pass

    urllib.request.urlretrieve(links[0], PATH_1)
    urllib.request.urlretrieve(links[1], PATH_2)
    urllib.request.urlretrieve(links[2], PATH_3)
    clip1 = VideoFileClip(PATH_1, audio=True).subclip(0, 7)
    clip2 = VideoFileClip(PATH_2, audio=True).subclip(0, 7)
    clip3 = VideoFileClip(PATH_3, audio=True).subclip(0, 7)
    final_clip = clips_array([[clip1, clip2, clip3]])
    file_no = random.random()
    final_clip.write_videofile(f"./static/video/merged{file_no}.mp4")

    try:
        os.remove(PATH_1)
        os.remove(PATH_2)
        os.remove(PATH_3)
    except PermissionError:
        print('as expected')
    clip1.close()
    clip2.close()
    clip3.close()
    try:
        os.remove(PATH_1)
        os.remove(PATH_2)
        os.remove(PATH_3)
        print('success')
    except PermissionError:
        print('you will not see this')

    return file_no
