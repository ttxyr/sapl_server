# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-07 14:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Oem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='\u540d\u79f0')),
                ('oemid', models.CharField(max_length=8, verbose_name='OEM\u6807\u8bc6')),
            ],
            options={
                'verbose_name': 'OEM',
                'verbose_name_plural': 'OEM',
            },
        ),
        migrations.CreateModel(
            name='Produce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=8, verbose_name='\u4ea7\u54c1\u540d\u79f0')),
                ('produceid', models.CharField(max_length=8, verbose_name='\u4ea7\u54c1\u7f16\u53f7')),
            ],
            options={
                'verbose_name': '\u4ea7\u54c1\u7c7b\u578b',
                'verbose_name_plural': '\u4ea7\u54c1\u7c7b\u578b',
            },
        ),
        migrations.CreateModel(
            name='Sdk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='SDK\u540d\u79f0')),
                ('path', models.CharField(max_length=128, verbose_name='\u4f4d\u7f6e')),
                ('branches', models.CharField(max_length=1024, verbose_name='SDK\u5206\u652f')),
            ],
            options={
                'verbose_name': 'SDK',
                'verbose_name_plural': 'SDK',
            },
        ),
        migrations.CreateModel(
            name='SdkType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='\u540d\u79f0')),
                ('envvalue', models.CharField(max_length=10240, verbose_name='\u73af\u5883\u53d8\u91cf\u540d\u79f0')),
            ],
            options={
                'verbose_name': 'SDK\u7c7b\u578b',
                'verbose_name_plural': 'SDK\u7c7b\u578b',
            },
        ),
        migrations.CreateModel(
            name='VcsCommit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('SVN', 'SubVersion'), ('GIT', 'GIT')], default='SVN', max_length=3, verbose_name='\u7248\u672c\u670d\u52a1\u5668\u7406\u6027')),
                ('coommitid', models.CharField(max_length=40, verbose_name='\u63d0\u4ea4ID')),
                ('branches', models.CharField(max_length=128, verbose_name='\u5206\u652f')),
            ],
            options={
                'verbose_name': '\u7248\u672c\u63d0\u4ea4',
                'verbose_name_plural': '\u7248\u672c\u63d0\u4ea4',
            },
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mainversion', models.CharField(max_length=32, verbose_name='\u4e3b\u7248\u672c\u53f7')),
                ('subversion', models.CharField(max_length=32, verbose_name='\u526f\u7248\u672c\u53f7')),
                ('description', models.CharField(default='', max_length=1024, verbose_name='\u7248\u672c\u4ecb\u7ecd')),
                ('type', models.CharField(choices=[('R', 'Realease'), ('DB', 'DailyBuild'), ('T', 'Test'), ('D', 'Debug')], max_length=2, verbose_name='\u7248\u672c\u7c7b\u578b')),
                ('binfile', models.CharField(max_length=1024, verbose_name='\u7248\u672c\u6587\u4ef6')),
                ('logfile', models.CharField(max_length=1024, verbose_name='\u65e5\u5fd7\u6587\u4ef6')),
                ('buildresult', models.CharField(choices=[('C', 'Cancel'), ('O', 'OK'), ('F', 'Failed')], max_length=3, verbose_name='\u7f16\u8bd1\u7ed3\u679c')),
                ('distpath', models.CharField(max_length=1024, verbose_name='\u7248\u672c\u53d1\u5e03\u4f4d\u7f6e')),
                ('distributed', models.BooleanField(default=False, verbose_name='\u662f\u5426\u53d1\u5e03')),
                ('commit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commit', to='complie.VcsCommit')),
                ('oem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='complie.Oem')),
                ('sdk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='complie.Sdk')),
                ('sdkcommit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sdkcommit', to='complie.VcsCommit')),
            ],
            options={
                'verbose_name': '\u7248\u672c',
                'verbose_name_plural': '\u7248\u672c',
            },
        ),
    ]
