# Create your views here.
#this is relate users login
# -*- coding: utf8 -*-

from django.contrib import auth
from vote.models import *
from django.contrib.auth import authenticate,login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from vote.form import UserproFrom,UserFrom
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import *
from django.template import *
import smtplib
from email.mime.text import  MIMEText
from email.header import Header
from _mysql import NULL
from cookielib import logger
from django.core import serializers
from django.http.response import HttpResponse
from email import MIMEMultipart

def resetpwd(request):   
    username=request.GET.get("username")    
    user=User.objects.filter(username=username).all()  
    return render(request,'vote/templates/resetpwd.html')

def resetpwd_json(request):   
    username=request.GET.get("username")    
    user=User.objects.filter(username=username).all()  
    print user
    for u in user:
        sendEmail(u.email)
    json = serializers.serialize("json", user)
    return HttpResponse(json,content_type="application/json")

def sendEmail(*receiver):
    sender='2371822205@qq.com'
    subject='投票系统找回密码'    
    mailuser='2371822205@qq.com'
    mailpwd='uxhnerwjwsbuecda'
    text='尊敬的用户，投票系统为您的重置密码为123456'   
    msg = MIMEText('<html><h1>'+text+'</h1></html>','html','utf-8')    
    msg['From']=sender
    msg['Subject'] = subject      
    smtp = smtplib.SMTP()  
    smtp.connect('smtp.qq.com')
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.set_debuglevel(1)
    smtp.login(mailuser, mailpwd)  
    smtp.sendmail(sender, receiver,msg.as_string())  
    smtp.quit()


def registe(request):
    if request=='POST':
        uf=UserFrom(request.POST,prefix='user')
        upf=UserproFrom(request.POST,prefix='userpro')
        if uf.is_valid() and upf.is_valid():                        
            user = uf.save()
            userprofile = upf.save(commit=False)
            userprofile.user = user
            userprofile.save()
            return HttpResponseRedirect('/vote/listcatgory/')
    else:
        uf = UserFrom(prefix='user')
        upf = UserproFrom(prefix='userprofile')
    return render_to_response('register.html', 
                                               dict(userform=uf,
                                                    userprofileform=upf),
                                               context_instance=RequestContext(request))

def my_login(request):
    username=request.get('username')
    password=request.get('password')
    user=authenticate(username=username,password=password)
    if user is not None:
        if user.is_active:
            login(request,user)
            return HttpResponseRedirect('/vote/listcatgory/')
        else:
            return HttpResponseRedirect('/vote/regist.html')
        
def my_logout(request):
    logout(request)
    return HttpResponseRedirect('/list/category')
    
        