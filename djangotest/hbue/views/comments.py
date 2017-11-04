import string

from django.http import Http404
from django.shortcuts import render

from hbue.models import *


def main(request, current_page="1"):
    try:
        current_page = int(current_page)
    except TypeError:
        raise Http404('current_page 失败')

    comments = Comment.objects.all()
    #print("所有评论：", comments)
    # request.session['hasLogedin']=False
    return render(request,"main.html",
                  {
                      'current_page':current_page,
                      'len':len(comments),
                      'comments':comments,
                  })

def search(request, cOrt):
    try:
        cOrt = string(cOrt)
    except ValueError:
        raise Http404()

    return render(request, 'search.html',{})

def index(input, current_page):
    # 每页显示10条数据
    per_page_count = 10
    length = len(input)
    start = (current_page - 1) * per_page_count  # start >= 0
    end = current_page * per_page_count
    if end > length:
        data = input[start:]
    else:
        data = input[start:end]
    end_page = int((length + 5) / 10 + 1)
    if current_page > 5:
        if end_page < current_page + 2:
            len_list = range(end_page - 4, end_page)
        else:
            len_list = range(current_page - 2, current_page + 2)
    else:
        if end_page < 5:
            len_list = range(1, end_page)
        else:
            len_list = range(1, 5)

    return data, len_list,
