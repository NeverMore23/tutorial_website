# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from DjangoUeditor.models import UEditorField


# Create your models here.
# null = True 空值将会被存储为NULL
# blank = True 页面当中对应的表单可以为空，可以不填任何内容
# supername: website
# pwd: tutorialwebsite

class Article(models.Model):
    title = models.CharField(u"title", max_length=100, blank=True)
    category = models.CharField(u"cate", max_length=50, blank=True)
    pub_date = models.DateField(u"pub_date", auto_now_add=True, editable=True)
    update_date = models.DateField(u"up_date", auto_now=True)
    # content = models.TextField(u"content", null=True, blank=True)
    content = UEditorField(u"文章正文", height=300, width=1000, default=u'', blank=True, imagePath="uploads/blog/images/",
                           toolbars='besttome', filePath='uploads/blog/files/')

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 't_article'
        ordering = ["-pub_date"]
        verbose_name = "文章"
        verbose_name_plural = "文章"
