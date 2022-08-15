from django.shortcuts import render
from .forms import GetLinkForm
import urllib
from moviepy.editor import VideoFileClip, concatenate_videoclips
import os

# Create your views here.


def upload_link_form(request):
    if request.method == "POST":
        form = GetLinkForm(request.POST)
        urllib.request.urlretrieve(request.POST['link1'], f"./static/video/your_video_name1.mp4")
        urllib.request.urlretrieve(request.POST['link2'], f"./static/video/your_video_name2.mp4")
        urllib.request.urlretrieve(request.POST['link3'], f"./static/video/your_video_name3.mp4")
        clip1 = VideoFileClip("./static/video/your_video_name1.mp4", audio=True)
        clip2 = VideoFileClip("./static/video/your_video_name2.mp4", audio=True)
        clip3 = VideoFileClip("./static/video/your_video_name3.mp4", audio=True)
        final_clip = concatenate_videoclips([clip1, clip2, clip3], method="compose")
        final_clip.write_videofile("./static/video/merged.mp4")
        os.remove("./static/video/your_video_name1.mp4")
        os.remove("./static/video/your_video_name2.mp4")
        os.remove("./static/video/your_video_name3.mp4")
    else:
        form = GetLinkForm()

    # print(request.POST['link1'])

    return render(request, './forms/form.html', {"form": form})
