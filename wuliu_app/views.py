# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .utils import *
from django.shortcuts import render
from django.http import JsonResponse


def get_valid_dict(src_dict,src_list):
    desc_dict={}
    for i in src_list:
        desc_dict[i]=src_dict.get(i,'null')
    return desc_dict

def homepage(request):
    pass


def index(request):
    if request.method == 'GET':
        return JsonResponse({'status': 1, 'data': {'error': 'only post allow'}})
    elif request.method == 'POST':
        data = {}
        branch = request.POST.get('branch', 'null')
        desc_list=['id','part','category','image_url','page_param']
        desc_dict={}
        desc_dict=get_valid_dict(desc_dict,desc_list)
        try:
            if branch == 'op_add':
                pass
            elif branch == 'op_delete':
                pass
            elif branch == 'op_update':
                pass
            elif branch == 'lay_content':
                pass
            elif branch == 'lay_details':
                pass
            elif branch == 'lay_list':
                pass
            elif branch == 'lay_news':
                pass
            elif branch == 'lay_carousel':
                pass
            else:
                pass
            status = 0
        except Exception as e:
            status = 1
        return JsonResponse({'status': status, 'data': data})

def add_object():
    sql_execute(get_insert_sql())
    pass

def delete_object():
    pass

def update_pbject():
    pass

def select_object():
    pass

def log_in(request):
    pass



