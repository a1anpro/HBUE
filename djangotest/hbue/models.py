from django.db import models

# Create your models here.





# 用户
class User(models.Model):
    course = models.ManyToManyField('Course', through="Comment")

    userId = models.IntegerField()
    userName = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    userIcon = models.CharField(max_length=30)
    userInfo = models.CharField(max_length=300)
    userAcademy = models.CharField(max_length=20)
    userLevel = models.IntegerField()

    def __unicode__(self):
        return self.name


# 老师
class Teacher(models.Model):

    clss = models.ManyToManyField('Class', through="Course")

    teachId = models.IntegerField()
    teachName = models.CharField(max_length=20)
    teachIcon = models.CharField(max_length=30)
    teachInfo = models.TextField(max_length=300)

    def __unicode__(self):
        return self.name

# 课程
class Class(models.Model):
    classId = models.IntegerField()
    className = models.CharField(max_length=20)
    classClass = models.CharField(max_length=20)
    academy = models.CharField(max_length=30)
    credit = models.IntegerField()
    capacity = models.IntegerField()

    def __unicode__(self):
        return self.name

# 老师课程
class Course(models.Model):

    teacher=models.ForeignKey(Teacher)
    clss = models.ForeignKey(Class)

    courseOnlyId = models.CharField(max_length=20)
    courseId = models.IntegerField()
    teachId = models.IntegerField()
    teachName = models.CharField(max_length=20)
    courseName = models.CharField(max_length=20)
    likes = models.IntegerField()
    unlikes = models.IntegerField()
    commentNum = models.IntegerField()
    callRate = models.IntegerField()
    passRate = models.IntegerField()
    getRate = models.IntegerField()

    def __unicode__(self):
        return self.name

# 个人评价
class Comment(models.Model):

    user = models.ForeignKey(User)
    course= models.ForeignKey(Course)

    courseOnlyId = models.CharField(max_length=20)
    userId = models.IntegerField()
    callRate = models.IntegerField()
    passRate = models.IntegerField()
    getRate = models.IntegerField()
    comment = models.TextField(max_length=300)
    commentTime = models.DateTimeField()
    ifPass = models.BooleanField()


    def __unicode__(self):
        return self.name




# 推荐
class Like(models.Model):

    user = models.ForeignKey('User')
    course = models.ForeignKey('Course')

    userId = models.IntegerField()
    courseOnlyId = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name




