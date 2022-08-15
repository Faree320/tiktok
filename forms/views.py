import time

from django.shortcuts import render
from .forms import GetLinkForm
import urllib
import random
from moviepy.editor import VideoFileClip, concatenate_videoclips, clips_array
import os

# Create your views here.


def upload_link_form(request):
    if request.method == "POST":
        form = GetLinkForm(request.POST)
        PATH_1 = "./static/video/your_video_name1.mp4"
        PATH_2 = "./static/video/your_video_name2.mp4"
        PATH_3 = "./static/video/your_video_name3.mp4"
        urllib.request.urlretrieve(request.POST['link1'], PATH_1)
        urllib.request.urlretrieve(request.POST['link2'], PATH_2)
        urllib.request.urlretrieve(request.POST['link3'], PATH_3)
        clip1 = VideoFileClip("./static/video/your_video_name1.mp4", audio=True)
        clip2 = VideoFileClip("./static/video/your_video_name2.mp4", audio=True)
        clip3 = VideoFileClip("./static/video/your_video_name3.mp4", audio=True)
        ran = random.randint(0, 1000)
        final_clip = clips_array([[clip1, clip2, clip3]])
        final_clip.write_videofile(f"./static/video/{ran}merged.mp4")
        os.remove(PATH_1)
        os.remove(PATH_2)
        os.remove(PATH_3)
    else:
        form = GetLinkForm()

    # print(request.POST['link1'])

    return render(request, './forms/form.html', {"form": form})
