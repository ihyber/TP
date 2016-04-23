# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_name', models.CharField(max_length=32, verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb\xe5\x90\x8d')),
            ],
            options={
                'verbose_name': '\u5206\u7c7b',
                'verbose_name_plural': '\u5206\u7c7b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='U_oper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vote_time', models.TimeField()),
                ('status', models.BooleanField(verbose_name=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='V_chioce',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice_detail', models.CharField(max_length=255, verbose_name=b'\xe9\x80\x89\xe9\xa1\xb9\xe5\x86\x85\xe5\xae\xb9')),
                ('choice_pic', models.ImageField(upload_to=b'choice', verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87')),
                ('count', models.IntegerField()),
            ],
            options={
                'verbose_name': '\u9009\u9879',
                'verbose_name_plural': '\u9009\u9879',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='V_event',
            fields=[
                ('event_id', models.AutoField(serialize=False, primary_key=True)),
                ('event_discribe', models.CharField(max_length=255, verbose_name=b'\xe5\x86\x85\xe5\xae\xb9')),
                ('event_pic', models.ImageField(upload_to=b'photos', verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87')),
                ('pu_date', models.DateTimeField(verbose_name=b'\xe5\xbc\x80\xe5\xa7\x8b\xe6\x97\xa5\xe6\x9c\x9f')),
                ('end_date', models.DateTimeField(verbose_name=b'\xe6\x88\xaa\xe6\xad\xa2\xe6\x97\xa5\xe6\x9c\x9f')),
                ('is_single', models.BooleanField(verbose_name=True)),
                ('category_id', models.ForeignKey(verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb', to='vote.Cat')),
            ],
            options={
                'verbose_name': '\u6295\u7968\u4e8b\u4ef6',
                'verbose_name_plural': '\u6295\u7968\u4e8b\u4ef6',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='V_user',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=64)),
                ('sex', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='v_chioce',
            name='event_id',
            field=models.ForeignKey(verbose_name=b'\xe6\x8a\x95\xe7\xa5\xa8\xe4\xba\x8b\xe4\xbb\xb6', to='vote.V_event'),
            preserve_default=True,
        ),
    ]
