from django.conf.urls import url,include
from django.contrib import admin
from hbue.views import comments,courses,other,search,sign,teacher,user

urlpatterns = [
    url(r'^$', comments.main),  # 主页
    url(r'^main/$', comments.main),  # 点击点评后的页面
    url(r'^main(?P<page>[0-9]+)/$', comments.main),  # 点击分页后进行跳转之后的结果
    url(r'^search/$', search.redirect), # 遇到url 为 /search 时，需要重定向
    url(r'^search/(?P<cOrt>[\u4e00-\u9fa5]*)/$', search.Search), # 按课程或教师进行查询
    url(r'^search/(?P<cOrt>[\u4e00-\u9fa5]*)&(?P<page>[0-9]+)/$', search.Search), # 按课程或教师进行查询并翻页
    url(r'^courses/$', courses.All),  # 所有的课程页
    url(r'^courses/(?P<page>[0-9]+)/$', courses.All),  # 点击分页后进行跳转之后的结果
    url(r'^course/([0-9]{1,6})/$', courses.One), # 单个课程页，即课程详细点评页 点击老师课程名跳转
    url(r'^course/[0-9]{1,6}/#comment-[0-9]{6}/$', courses.One), # 点击评论里的更多 跳转到相应的course下的锚点
    url(r'^signin/$', sign.sin),  # 登录页面
    url(r'^signup/$', sign.sup),  # 注册页面
    url(r'^reset/$', sign.reset), # 密码重置
    url(r'^user/([0-9]{1,6})/$', user.user_x), # 未登录时别人看到的
    url(r'^user/([0-9]{1,6})/follow/$', user.user_x),  # 关注的人
    url(r'^user/([0-9]{1,6})/comments/$', user.user_x),  # 该用户所有的评论
    url(r'^user/inner/([0-9]{1,6})/$', user.user_inner), # 登录或者注册过后进行跳转 用户id 未明确
    url(r'^teacher/([0-9]{1,6})$', teacher.teachCourse), # 点击老师姓名时 跳转 显示该老师所有的课程1
    url(r'^about/$', other.about), # 关于我们
    url(r'^blog/$', other.blog), # 博客
    url(r'^community-rule/$', other.rule),  # 使用规则

    url(r'^admin/', admin.site.urls),
]
