# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

from django.template import RequestContext
from django.shortcuts import render_to_response

def home(request):
    return render_to_response('home.html',
                              context_instance=RequestContext(request))
