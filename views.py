# Create your views here.
#coding:utf-8
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.db import connection, transaction

from sscp.models import TFilm

PAGE_NUMBER = 10
cursor = connection

def list(request):
    # Get Page Number from request
    page = int(request.GET.get('page', 1))
    search = request.GET.get('search', '')
    date = request.GET.get('date','')
        
    if search != '':
        list_count = TFilm.objects.filter(accession_number=search, verify_flag='1').count()
        page_count = (list_count/PAGE_NUMBER) > 0 and (list_count/PAGE_NUMBER) or 1
        list_start = (page - 1) * PAGE_NUMBER
        list_end = page * PAGE_NUMBER
        latest_film_list = TFilm.objects.filter(accession_number=search, verify_flag='1').order_by('date_time_created')[list_start:list_end]
        
    else:
        list_count = TFilm.objects.filter(verify_flag='1').count()
        page_count = (list_count/PAGE_NUMBER) > 0 and (list_count/PAGE_NUMBER) or 1
        list_start = (page - 1) * PAGE_NUMBER
        list_end = page * PAGE_NUMBER
        latest_film_list = TFilm.objects.filter(verify_flag='1').order_by('date_time_created')[list_start:list_end]
        
    current_page = page
    previous_page = current_page - 1
    next_page = current_page + 1
    
    template = loader.get_template('sscp/index.html')
    context = RequestContext(request, {
            'latest_film_list': latest_film_list,
            'page_count': page_count,
            'current_page': current_page,
            'previous_page': previous_page,
            'next_page': next_page
    })
    return HttpResponse(template.render(context))

def manualIndex(request):
    return HttpResponse("You are looking at the results of studies with Acc# %s in %s days.")

def detail(request, ref):

    template = loader.get_template('sscp/detail.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

def terminal(request):
    message = '请刷卡'
    isList = 0
    
    template = loader.get_template('sscp/terminal.html')
    context = RequestContext(request, {
            'message' : message,
            'isList' : isList,
    })    
    return HttpResponse(template.render(context))