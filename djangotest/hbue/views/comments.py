from django.shortcuts import render
from django.http import Http404
import string

from hbue.static.function import index
from ..models import *

def main(request, current_page="1"):
    try:
        current_page = int(current_page)
    except TypeError:
        raise Http404('current_page 失败')

    comments = [{
        'userName': '1',
        'teachName': '2',
        'userId': current_page,
        'teachId': 1,
        'commentTime': '2017-02-02',
        'comment': '1234567890',
        'photo': '#',
    }, {
        'userName': '2',
        'teachName': '3',
        'userId': current_page,
        'teachId': 1,
        'commentTime': '2017-02-02',
        'comment': '1234567890',
        'photo': '#',
    }, {
        'userName': '223',
        'teachName': '2123',
        'userId': current_page,
        'teachId': 1,
        'commentTime': '2017-02-02',
        'comment': '1234567890',
        'photo': '#',
    }, {
        'userName': '1123',
        'teachName': '2123123',
        'userId': current_page,
        'teachId': 1,
        'commentTime': '2017-02-02',
        'comment': '1234567890',
        'photo': '#',
    }, {
        'userName': '1123123',
        'teachName': '212412',
        'userId': current_page,
        'teachId': 1,
        'commentTime': '2017-02-02',
        'comment': '1234567890',
        'photo': '#',
    }, {
        'userName': '1asf',
        'teachName': 'sdfsdf2',
        'userId': current_page,
        'teachId': 1,
        'commentTime': '2017-02-02',
        'comment': '1234567890',
        'photo': '#',
    }, {
        'userName': '1sdf',
        'teachName': '2sdf',
        'userId': current_page,
        'teachId': 1,
        'commentTime': '2017-02-02',
        'comment': '1234567890',
        'photo': '#',
    }, {
        'userName': '1sdfsdf',
        'teachName': '2',
        'userId': current_page,
        'teachId': 1,
        'commentTime': '2017-02-02',
        'comment': '1234567890',
        'photo': '#',
    }, {
        'userName': '1',
        'teachName': '2',
        'userId': current_page,
        'teachId': 1,
        'commentTime': '2017-02-02',
        'comment': '1234567890',
        'photo': '#',
    }, ]

    data, len_list = index(comments, current_page)

    return render(request, "ok_main.html", {
        'comments': data,
        'len_list': len_list,
        'urlNum': current_page,
        'total': 100,
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


