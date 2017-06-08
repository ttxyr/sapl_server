# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Oem(models.Model):
    name = models.CharField(max_length=32, verbose_name=u'名称')
    oemid = models.CharField(max_length=8, verbose_name=u'OEM标识')

    class Meta:
        verbose_name = 'OEM'
        verbose_name_plural = 'OEM'


class Produce(models.Model):
    name = models.CharField(max_length=8, verbose_name=u'产品名称')
    produceid = models.CharField(max_length=8, verbose_name=u'产品编号')

    class Meta:
        verbose_name = u'产品类型'
        verbose_name_plural = u'产品类型'


class SdkType(models.Model):
    name = models.CharField(max_length=64, verbose_name=u'名称')
    envvalue = models.CharField(max_length=10240, verbose_name=u'环境变量名称')

    class Meta:
        verbose_name = u'SDK类型'
        verbose_name_plural = u'SDK类型'


class Sdk(models.Model):
    name = models.CharField(max_length=64, verbose_name=u'SDK名称')
    path = models.CharField(max_length=128, verbose_name=u'位置')
    branches = models.CharField(max_length=1024, verbose_name=u'SDK分支')

    class Meta:
        verbose_name = 'SDK'
        verbose_name_plural = 'SDK'


class VcsCommit(models.Model):
    type = models.CharField(max_length=3, choices={('GIT', "GIT"),
                                                   ('SVN', 'SubVersion')},
                            default='SVN',
                            verbose_name=u'版本服务器理性')
    coommitid = models.CharField(max_length=40, verbose_name=u'提交ID')
    branches = models.CharField(max_length=128, verbose_name=u'分支')

    class Meta:
        verbose_name = u'版本提交'
        verbose_name_plural = u'版本提交'


class Version(models.Model):
    mainversion = models.CharField(max_length=32, verbose_name=u'主版本号')
    subversion = models.CharField(max_length=32, verbose_name=u'副版本号')
    oem = models.ForeignKey('Oem')
    commit = models.ForeignKey('VcsCommit', related_name='commit')
    description = models.CharField(max_length=1024, verbose_name=u'版本介绍', default='')
    sdk = models.ForeignKey('Sdk')
    sdkcommit = models.ForeignKey('VcsCommit', related_name='sdkcommit')
    type = models.CharField(max_length=2, choices={('R', 'Realease'),
                                                   ('T', 'Test'),
                                                   ('D', 'Debug'),
                                                   ('DB', 'DailyBuild')},
                            verbose_name=u'版本类型')
    binfile = models.CharField(max_length=1024, verbose_name=u'版本文件')
    logfile = models.CharField(max_length=1024, verbose_name=u'日志文件')
    buildresult = models.CharField(max_length=3, choices={('O', 'OK'),
                                                          ('F', 'Failed'),
                                                          ('C', 'Cancel')},
                                   verbose_name=u'编译结果')
    distpath = models.CharField(max_length=1024, verbose_name=u'版本发布位置')
    distributed = models.BooleanField(verbose_name=u'是否发布', default=False)

    class Meta:
        verbose_name = u'版本'
        verbose_name_plural = u'版本'
