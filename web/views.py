from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from .models import Scheduler
from .models import Job
from .models import Activity
from .models import Post

import requests
from bs4 import BeautifulSoup

def main(request):
    return render(request, 'web/main.html', {})

def scholarship(request):
    return render(request, 'web/scholarship.html', {})

### 장학금 구분에 따른 URL ###W
def scholarship1(request):
    return render(request, 'web/scholarship/scholarship1.html', {})

def scholarship2(request):
    return render(request, 'web/scholarship/scholarship2.html', {})
#############################
    
def schedule(request):
    req = requests.get('https://sejong.korea.ac.kr/academics/administration/calendar/undergraduate', verify=False) #학사일정 크롤링
    raw = req.text
    html = BeautifulSoup(raw, 'html.parser')
    infos = html.select('div.listWrap')
    List = []
    num = 0
    for i in infos:
        S = Scheduler()
        S.titleList = i.select_one('dt').text
        S.descriptionList = i.select_one('dd').text
        S.set_lndex(num)
        List.append(S)
        num+=1
    return render(request, 'web/schedule.html', {"scheduler": List})

def job(request):
    clip = []
    clip_section = []
    href_link = []
    num = 0
    List = []
    req = requests.get('https://sejong.korea.ac.kr/user/boardList.do?handle=70991&siteId=cdc&id=cdc_030400000000', verify=False) #채용정보 크롤링
    raw = req.text
    html = BeautifulSoup(raw, 'html.parser')

    infos = html.select('#board_list05 > table> tbody> tr')

    for i in range(len(infos)): #게시글 추가
        clip.append(infos[i])

    for j in clip:
        clip_section.append(j.select('td'))
        href_link.append(j.find("a")["href"])

    for k in clip_section: #모델에 각 정보들 저장
        J = Job()
        J.title = k[1].text 
        J.author = k[2].text
        J.due = k[3].text
        J.link = href_link[num]
        List.append(J)
        num+=1
    return render(request, 'web/job.html', {"job" : List})

def activity(request):
    clip = []
    clip_section = []
    href_link = []
    num = 0
    List = []
    req = requests.get('https://sejong.korea.ac.kr/user/boardList.do?handle=71015&siteId=cdc&id=cdc_030600000000', verify=False) #대외활동 크롤링
    raw = req.text
    html = BeautifulSoup(raw, 'html.parser')

    infos = html.select('#board_list05 > table> tbody> tr')

    for i in range(len(infos)): #게시글 추가
        clip.append(infos[i])

    for j in clip:
        clip_section.append(j.select('td'))
        href_link.append(j.find("a")["href"])

    for k in clip_section: #모델에 각 정보들 저장
        J = Activity()
        J.title = k[1].text 
        J.author = k[2].text
        J.due = k[3].text
        J.link = href_link[num]
        List.append(J)
    return render(request, 'web/activity.html', {"job" : List})

###게시판 만들기###
def list(request):
    boards = {'boards':Post.objects.all()}
    return render(request, 'web/blog.html', boards)

def post(request):
    if(request.method == "POST"):
        author = request.POST['author']
        title = request.POST['title']
        content = request.POST['content']
        board = Post(author=author, title=title, content=content)
        board.save()
        return HttpResponseRedirect(reverse('blog'))
    else:
        return render(request, 'web/post.html', {})
    
def detail(request, id):
    try:
        board = Post.objects.get(pk=id)
    except Post.DoesNotExist:
        raise Http404("404발생! 존재하지 않습니다!!")
    return render(request, 'web/detail.html', {'board': board})