# -*- coding: utf8 -*-
from vote.models import userpro
from django.contrib.auth.models import User
from django.forms import ModelForm

class UserFrom(ModelForm):
    class Meta:
        model=User
        fields=['username','password','email']
class UserproFrom(ModelForm):
    class Meta:
        model=userpro
        exclude=['User']