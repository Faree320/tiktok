from django.shortcuts import render, redirect
from .controllers import get_links, merdge, auto_generator_c

# Create your views here.



def upload_link_form(request):
    query = request.GET.get('genre')

    PATH_1 = "./static/video/your_video_name1.mp4"
    PATH_2 = "./static/video/your_video_name2.mp4"
    PATH_3 = "./static/video/your_video_name3.mp4"
    # print(data)
    if request.method == "POST":

        d = request.POST
        data = []
        for key, value in d.items():
            data.append(value)

    #     form = GetLinkForm(request.POST)
    #     link1 = request.POST['link1']
    #     link2 = request.POST['link2']
    #     link3 = request.POST['link3']

        merdge(data, PATH_1, PATH_2, PATH_3)
        return redirect("final-result/")
    list1, list2 = get_links(query)
    mylist = zip(list1, list2)
    context = {'data': mylist}
    return render(request, './forms/form.html', context)


def key_search(request):
    return render(request, './forms/keySearch.html')


def wait_screen(request):
    if request.method == "POST":
        a = []
        for i in range(3):
            a.append(i)
        request.session['a'] = a
        return redirect('test')
    return render(request, './forms/waitScreen.html')


def test(request):
    data = request.session['a']
    print(data)
    return render(request, './forms/test.html')


def final_result(request):
    return render(request, './forms/finalResult.html')


def auto_generator(request):

    PATH_1 = "./static/video/your_video_name1.mp4"
    PATH_2 = "./static/video/your_video_name2.mp4"
    PATH_3 = "./static/video/your_video_name3.mp4"
    if request.method == "POST":
        global a
        a = []
        limit = int(request.POST['loopValue'])

        request = ["https://www.tiktok.com/music/original-sound-7067201969491823386",
                   "https://www.tiktok.com/music/Love-Me-Like-You-Do-6732341891376875522",
                   "https://www.tiktok.com/music/original-sound-7135791676018248474"]
        for i in range(limit):
            a.append(auto_generator_c(request[i], PATH_1, PATH_2, PATH_3))

        return redirect('auto-final-result')

    return render(request, './forms/autoGenerator.html')


def autoFinalResult(request):
    print(a)
    context = {'data': a}
    return render(request, './forms/autoFinalResult.html', context)

