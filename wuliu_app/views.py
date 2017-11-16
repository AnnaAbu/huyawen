# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .utils import sql_execute, get_insert_sql, get_select_sql, get_update_sql
from django.shortcuts import render
from django.http import JsonResponse


def index(request):
    if request.method == 'GET':
        return JsonResponse({'status': 1, 'data': {'error': 'only post allow'}})
    elif request.method == 'POST':
        data = {}
        branch = request.POST.get('branch', 'null')
        try:
            if branch == 'add':
                pass
            elif branch == 'delete':
                pass
            elif branch == 'update':
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
