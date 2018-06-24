# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils import timezone

class Link(models.Model):
    link_text = models.CharField(max_length=200, default="")
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.link_text
