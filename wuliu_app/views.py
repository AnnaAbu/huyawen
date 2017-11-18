# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .utils import *
from django.shortcuts import render
from django.http import JsonResponse
from . import conf


def __op_add(src_dict, files):
    return {}


def __op_delete(src_dict, files):
    return {}


def __op_update(src_dict, files):
    return {}


def __lay_content(src_dict, des_list):
    return {}


def __lay_details(src_dict, des_list):
    return {}


def __lay_list(src_dict, des_list):
    categories = src_dict.getlist('category[]', ['all'])
    page_param = src_dict.get('page_param', {})
    page = page_param.get('page', 0)
    num = page_param.get('num', 3)
    #import ipdb;ipdb.set_trace()
    average = page_param.get('average',conf.CONF_FALSE)
    start = int(page) * int(num)
    desc_str = ','.join(des_list)
    if 'all' in categories:
        part = src_dict.get('part', conf.CONF_NULL)
        if part==conf.CONF_NULL:
            raise Exception('invalid part in lay_list')
        sql = 'select ' + desc_str + ' from article where part="' + part + '" limit ' + str(start) + ', ' + str(num)
    else:
        sql_category = ''
        #import ipdb;ipdb.set_trace()
        for category in categories:
            if category not in conf.VALID_CATEGORIES:
                raise Exception('invalid category')
            sql_category += 'category ="' + category + '" or '
            sql_category = sql_category[:-3]
        if average == conf.CONF_TRUE:
            sql = " select " + desc_str + " from article as a where (select count(*) from" + \
                  " article as b where b.category=a.category and b.id>=a.id)<= " + str(num) + " and( " + sql_category + ")"
        else:
            sql = "select " + desc_str + " from article where " + sql_category + " limit " \
                  + str(start) + ', ' + num
    ct = sql_execute(sql)
    data = []
    for c in ct:
        temp_dict = {}
        for i in range(len(c)):
            temp_dict[des_list[i]] = c[i]
        data.append(temp_dict)
    return data


def __lay_news(src_dict, des_list):
    return {}


def __lay_carousel(src_dict, des_list):
    return {}


def index(request):
    import ipdb; ipdb.set_trace()
    if request.method == 'GET':
        return JsonResponse({'status': 1, 'data': {'error': 'only post allow'}})
    elif request.method == 'POST':
        branch = request.POST.get('branch', 'null')
        try:
            if branch == 'op_add':
                data = __op_add(request.POST, request.FILES)
            elif branch == 'op_delete':
                data = __op_delete(request.POST, request.FILES)
            elif branch == 'op_update':
                data = __op_update(request.POST, request.FILES)
            elif branch == 'lay_content':
                data = __lay_content(request.POST)
            elif branch == 'lay_details':
                data = __lay_details(request.POST)
            elif branch == 'lay_list':
                data = __lay_list(request.POST,['id','title','timestamp','part','category'])
            elif branch == 'lay_news':
                data = __lay_news(request.POST)
            elif branch == 'lay_carousel':
                data = __lay_carousel(request.POST)
            else:
                data = {'message': 'invalid branch'}
            status = 0
        except Exception as e:
            status = 2
            data={'error':e.message}
        return JsonResponse({'status': status, 'data': data})
