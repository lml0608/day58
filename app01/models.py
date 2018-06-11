from django.db import models

# Create your models here.


#班级和老是是多对多的关系
class Classes(models.Model):
    """
    班级
    """

    title = models.CharField(max_length=32)

    m = models.ManyToManyField("Teachers")

class Teachers(models.Model):
    """
    老师表
    """


    name = models.CharField(max_length=32)



class Student(models.Model):

    username = models.CharField(max_length=32)

    age = models.IntegerField()

    gender = models.BooleanField(default=False)

    cs = models.ForeignKey("Classes")