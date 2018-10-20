from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def get_button_list(box=(860, 420, 1130, 640), n_buttons = 6, bgr=0.8, height=60, link_list=["page.html"]):
    coord_list = [[219, 912, 322, 1056]]
    return zip(link_list, coord_list)

def index(request):
    context = { 
        "name" : "Jon",
        "button_list" : get_button_list(box=(860, 420, 1130, 640), n_buttons = 6, bgr=0.8, height=60)
    }
    return render(request, 'maxkiosk/index.html', context=context)

def page_1(request):
    return render(request, 'maxkiosk/page_1.html')

def page_2(request):
    return render(request, 'maxkiosk/page_2.html')

def page_3(request):
    return render(request, 'maxkiosk/page_3.html')

def page_4a(request):
    return render(request, 'maxkiosk/page_4a.html')

def page_4b(request):
    return render(request, 'maxkiosk/page_4b.html')

def page_4c(request):
    return render(request, 'maxkiosk/page_4c.html')

def page_4d(request):
    return render(request, 'maxkiosk/page_4d.html')

def page_4e(request):
    return render(request, 'maxkiosk/page_4e.html')

def page_5(request):
    return render(request, 'maxkiosk/page_5.html')

