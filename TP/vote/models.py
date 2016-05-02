# Create your models here.
# -*- coding: utf8 -*-
from django.db import models
from django.contrib.auth.models import User
from pydoc import visiblename
from bsddb.test.test_all import verbose
from distutils.command.upload import upload

class userpro(models.Model):
    user=models.OneToOneField(User,unique=True)
    user_img=models.ImageField(upload_to='head',verbose_name='用户头像')
    sex=models.BooleanField(verbose_name="女生")
    age=models.IntegerField(verbose_name='年龄')
    phone=models.CharField(max_length=11,verbose_name='手机号码')
    city=models.CharField(max_length=45,verbose_name='所在城市')
    carrer=models.CharField(max_length=45,verbose_name='职业')
    
    class Meta:
        verbose_name = "用户扩展"
        verbose_name_plural = "用户扩展"
    
# Create your models here.
class Cat(models.Model):
    category_name=models.CharField(max_length=32,verbose_name="分类名")
    
    def __unicode__(self):
        return self.category_name
    class Meta:
        verbose_name = "分类"
        verbose_name_plural = "分类"


class V_event(models.Model):
    event_id=models.AutoField(primary_key=True)
    event_discribe=models.CharField(max_length=255,verbose_name="内容")
    event_pic=models.ImageField(upload_to='photos',verbose_name="图片")
    pu_date=models.DateTimeField(verbose_name="开始日期")
#    pu_time=models.TimeField()
    end_date=models.DateTimeField(verbose_name="截止日期")
#    end_time=models.TimeField()
    category_id=models.ForeignKey(Cat,verbose_name="分类")
    is_single=models.BooleanField("是否单选")
    status=models.BooleanField("发布状态")
   

    def __unicode__(self):
        return self.event_discribe
    class Meta:
        verbose_name = "投票事件"
        verbose_name_plural = "投票事件"
#        ordering=('-pu_time',)
    def save_status(self):
        staus=1
        return self.status

class V_chioce(models.Model):
    choice_detail=models.CharField(max_length=255,verbose_name="选项内容")
    choice_pic=models.ImageField(upload_to='images',verbose_name="图片")
    count=models.IntegerField(verbose_name="投票计数")
    event_id=models.ForeignKey(V_event,verbose_name="投票事件")
    def __unicode__(self):
        return self.choice_detail
    class Meta:
        verbose_name = "选项"
        verbose_name_plural = "选项"


class V_user(models.Model):
    user_name=models.CharField(max_length=64)
    password=models.CharField(max_length=64)
    sex=models.CharField(max_length=10)
    age=models.IntegerField()


class U_oper(models.Model):
#    oper_id=models.ForeignKey(V_user)
    vote_time=models.TimeField()
    status=models.BooleanField(True)
