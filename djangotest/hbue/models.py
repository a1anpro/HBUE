from django.db import models

# Create your models here.

# 用户
class User(models.Model):
    course = models.ManyToManyField('Course', through="Comment")#用户和Course表生成的关系表

    userId = models.CharField(max_length=10)#用户id
    userName = models.CharField(max_length=20)#用户名
    password = models.CharField(max_length=20)#密码
    userIcon = models.CharField(max_length=30,default="/img/udefaultIcon.jpg")#用户头像路径，头像文件由用户上传，数据库只存用户头像路径
    userInfo = models.TextField(max_length=300)#用户简介
    userAcademy = models.CharField(max_length=20)#用户所在学院
    userLevel = models.IntegerField()#用户等级，比如：管理员，常客。。

    def __str__(self):
        return self.userName


# 教师：
class Teacher(models.Model):
    course = models.ManyToManyField('Clss', through="Course")#教师和Class课程生成的关系表,是确定的课程

    teacherId = models.CharField(max_length=20)#教师id
    teacherName = models.CharField(max_length=20)#教师名
    teacherIcon = models.CharField(max_length=30, default="/img/tdefaultIcon.jpg")#教师头像路径，同上
    teacherInfo = models.TextField(max_length=300)#教师简介

    def __str__(self):
        return self.teacherName

# 课程（一个课程有多个教师教授，这是课程的大类）
class Clss(models.Model):
    classId = models.CharField(max_length=20)#课程id
    className = models.CharField(max_length=20)#课程名
    classClass = models.CharField(max_length=20)#课程类型
    academy = models.CharField(max_length=30)#教授学院
    credit = models.IntegerField()#学分
    capacity = models.IntegerField()#容纳学生数

    def __str__(self):
        return self.className

# 确定课程（由老师和Class确定）
class Course(models.Model):
    teacher = models.ForeignKey(Teacher, related_name="course_teacher")#Teacher的自动生成id是该表的外键
    clss = models.ForeignKey(Clss)#Class的自动生成id是该表的外键

    likes = models.IntegerField(default=0)#推荐数
    unlikes = models.IntegerField(default=0)#不推荐数
    commentNum = models.IntegerField(default=0)#评论数
    callRate = models.IntegerField(default=0)#点名频率，通过评论计算得出
    passRate = models.IntegerField(default=0)#通过指标
    getRate = models.IntegerField(default=0)#收获指标
    lastRate = models.IntegerField(default=5)
    # courseOnlyId = models.CharField(max_length=20)#课程唯一id
    # classId = models.CharField(max_length=20)#所属课程id
    # teacherId = models.CharField(max_length=20)#所教授教师id
    #
    # className = models.CharField(max_length=20)#所属课程名
    # teacherName = models.CharField(max_length=20)#所教授教师姓名

    def __str__(self):
        return self.clss.__str__() + '(' + self.teacher.__str__() + ')'


# 用户评价(由User表和Course表确定)
class Comment(models.Model):
    user = models.ForeignKey(User)#User自动生成的id是该表的外键，就是，User中的用户被删除了，这条评论也将删除
    course= models.ForeignKey(Course)#Course自动生成的id是该表的外键，

    # courseOnlyId = models.CharField(max_length=20)#课程唯一id
    # userId = models.CharField(max_length=20)#用户id
    ############是否用用户id，还是用用户名比较好？
    callRate = models.IntegerField()#一个用户评价的点名频率，用于计算总评分数
    passRate = models.IntegerField()#同上，通过指标
    getRate = models.IntegerField()#同上，收获指标
    comment = models.TextField(max_length=300)#一个用户的文字评论
    commentTime = models.DateTimeField()#评论时间
    ifPass = models.BooleanField()#是否通过审核

    def __str__(self):
        return self.user.userName + '(' + self.course.clss.className + ')'

# 推荐
class Like(models.Model):
    user = models.ForeignKey('User')
    course = models.ForeignKey('Course')

    # userId = models.CharField(max_length=20)#用户id
    # courseOnlyId = models.CharField(max_length=20)#课程唯一id

    def __str__(self):
        return 'recommend:' + self.user.userName + ' likes ' + self.course.clss.className




