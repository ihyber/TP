# Create your views here.
# -*- coding: utf8 -*-

from django.shortcuts import render, get_object_or_404, render_to_response,\
    redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from .models import *
import time
from django.core.context_processors import request
from django.db.models.aggregates import Sum
from django.core import serializers
from django.http.response import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.comments.admin import UsernameSearch
from json.tests.test_pass1 import JSON
import json
from _mysql import NULL


# def queryVoteCount(request):
#   eventId=request.GET.get("eventId")
 #   choice_list=V_chioce.objects.filter(event_id=eventId).order_by("-id")
  #  json = serializers.serialize("json",choice_list )
   
    # return HttpResponse(json,content_type="application/json")

def queryResultForEvent(request):
    eventId=request.POST.get("eventId");
    choice_list = V_chioce.objects.filter(event_id=eventId).order_by("-id")
    json = serializers.serialize("json", choice_list)
    return HttpResponse(json, content_type="application/json")

def loadEvent(request):
    eventId=request.GET.get("eventId")
    event_list=[]
    event_list.append(V_event.objects.get(pk=eventId))
    json = serializers.serialize("json", event_list)
    return HttpResponse(json, content_type="application/json")

def queryEvent(request):
    event_list = V_event.objects.all().order_by("-event_id")
    json = serializers.serialize("json", event_list)
    eventId=request.POST.get("eventId")
    if eventId is not None:
        json = serializers.serialize("json", V_event.objects.filter(pk=eventId).all())
        return HttpResponse(json, content_type="application/json")
    cat_id=request.POST.get("category_id")
    if cat_id !="":
        json = serializers.serialize("json", V_event.objects.filter(category_id=cat_id).all())
    return HttpResponse(json, content_type="application/json")
    
def Login(request):
    curtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime());
    usename = request.get("username")
    password = request.get("password")
    return HttpResponse()

#最新投票事件的投票结果
def latest(request):
    c = V_chioce.objects.order_by("-event_id").first();
    eventId = c.event_id_id;
    choice_list = V_chioce.objects.filter(event_id=eventId).order_by("-id")
    json=serializers.serialize("json",choice_list)
    return HttpResponse(json, content_type="application/json")

def saveChoice(request):
    eventId = request.GET.get("eventId")
    event = V_event.objects.get(pk=eventId)
    choiceArr = request.GET.getlist("choice")
    for cId in choiceArr:
        choice = V_chioce.objects.get(pk=cId)
        choice.count = choice.count + 1
        choice.save(update_fields=['count'])
    choice_list = V_chioce.objects.filter(event_id=eventId).order_by("-id")
#     choice_list=choice_list.annotate(count_sum=Sum('count'))
    total = 0
    for c in choice_list:
        total += c.count
    context = {"choice_list":choice_list, "event":event, "total":total}
    return redirect("/vote/go/?eventId="+eventId+"&url=vote/templates/result.html")

def go(request):
    url_str=request.GET.get("url")
    return  render(request,url_str)

def readEvent(request):
    eventId = request.GET.get("eventId")
    event = get_object_or_404(V_event, pk=eventId)
    chioce_list = V_chioce.objects.filter(event_id=eventId).order_by("-id")
    context = {"event":event, "chioce_list":chioce_list}
    return render(request, 'vote/templates/readEvent.html', context)

def listCategory(request):
    CateList = Cat.objects.all()
    eventList = V_event.objects.all()
    context = {'CateList': CateList, "event_list":eventList}
    return render(request, 'vote/templates/index.html', context)

# 首页展示所有问题
def index(request):
    # latest_question_list2 = Question.objects.order_by('-pub_data')[:2]
    latest_question_list = V_event.objects.all()
    context = {'latest_question_list': latest_question_list}
    return render(request, 'index.html', context)

# 查看所有问题
def detail(request, event_id):
    question = get_object_or_404(V_event, pk=event_id)
    return render(request, 'polls/detail.html', {'question': question})


# 查看投票结果
def results(request, count):
    result = get_object_or_404(V_chioce, pk=count)
    return render(request, 'polls/results.html', {'result': result})


# 选择投票
def vote(request, event_id):
    p = get_object_or_404(V_chioce, pk=id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, V_chioce.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
    
def auditing(request):
    # 根据时间排序展示没有发布的投票事件
    pulish_event = V_event.objects.filter(status=0).order_by("-pu_date")    
    return render(request, 'vote/templates/pulish.html', {'pulish_event':pulish_event})

def getcheck(request,):
    pu = request.REQUEST.getlist("check_box_list")
    for r in pu :
        e = V_event.objects.get(pk=r)
        e.status = True;
        e.save(update_fields=['status'])
    return render(request, 'vote/templates/pulish.html')
  
    
# 分页
def page(request):
    
    event_list = V_event.objects.all()
    
# 每页10条数据的一个容器
    inator = Paginator(event_list, 10)
    
# 保证页面请求是一个整数，否则返回第一页 
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
# 页面请求超出范围返回最后数据
    try:
        contacts = inator.page(page)
    except (EmptyPage, InvalidPage):
        contacts = inator.page(inator.num_pages)

    return render_to_response('list.html', {"contacts": contacts})
    
    



def loadPageHeader(request):
    CateList = Cat.objects.all()
    context = {'CateList': CateList}
    return render(request, 'vote/templates/common/header.html', context)






    
