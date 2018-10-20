from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.contrib.staticfiles.templatetags.staticfiles import static

reciept_url = static('image.png')
# Create your views here.

def get_button_list(box=(860, 420, 1130, 640), n_buttons = 6, bgr=0.8, height=60, link_list=["page.html"]):
    coord_list = [[219, 912, 322, 1056]]
    return zip(link_list, coord_list)

def index(request):
    # latest_user = User.object.order_by('-pub_date')[:5]

    context = {
        "name" : "Jon",
        "button_list" : get_button_list(box=(860, 420, 1130, 640), n_buttons = 6, bgr=0.8, height=60),
        # "user list" : latest_user
    }
    return render(request, 'maxkiosk/index.html', context=context)

def page_1(request):
    context = {
        "text" : "Menu",
        "links" : {
            "Button1" : {"text" : "", 
                "link" : "page_2"},
            "Button2" : {"text" : "", 
                "link" : "page_2"},
            "Button3" : {"text" : "", 
                "link" : "page_2"},
            "Button4" : {"text" : "", 
                "link" : "page_2"},
            "Button5" : {"text" : "", 
                "link" : "page_2"} ,   
            "Button6" : {"text" : "", 
                "link" : "page_2"},
        }
    }
    return render(request, 'maxkiosk/index.html', context=context)

def page_2(request):
    context = {
        "text" : "Menu",
        "links" : {
            "Button1" : {"text" : "Print", 
                "link" : reciept_url},
            "Button2" : {"text" : "", 
                "link" : "#"},
            "Button3" : {"text" : "", 
                "link" : "#"},
            "Button4" : {"text" : "", 
                "link" : "#"},
            "Button5" : {"text" : "",
                "link" : "#"} ,   
            "Button6" : {"text" : "Next", 
                "link" : "page_3"},
        }
    }
    return render(request, 'maxkiosk/index.html', context=context)


def page_3(request):
    context = {
        "text" : "Menu",
        "links" : {
            "Button1" : {"text" : "Health and Safety", 
                "link" : "page_4a"},
            "Button2" : {"text" : "Basic", 
                "link" : "page_4b"},
            "Button3" : {"text" : "Print", 
                "link" : reciept_url},
            "Button4" : {"text" : "Food", 
                "link" : "page_4c"},
            "Button5" : {"text" : "Health", 
                "link" : "page_4d"} ,   
            "Button6" : {"text" : "Transit", 
                "link" : "page_4e"},
        }
    }
    return render(request, 'maxkiosk/index.html', context=context)


def page_4a(request):
    context = {
        "text" : "Options...",
        "links" : {
            "Button1" : {"text" : "Print",
                "link" : reciept_url},
            "Button2" : {"text" : "",
                "link" : "#"},
            "Button3" : {"text" : "",
                "link" : "#"},
            "Button4" : {"text" : "",
                "link" : "#"},
            "Button5" : {"text" : "",
                "link" : "#"},
            "Button6" : {"text" : "Back",
                "link" : "page_3"}
        }
    }
    return render(request, 'maxkiosk/index.html', context=context)


def page_4b(request):
    context = {
        "text" : "Options...",
        "links" : {
            "Button1" : {"text" : "Print",
                "link" : reciept_url},
            "Button2" : {"text" : "",
                "link" : "#"},
            "Button3" : {"text" : "",
                "link" : "#"},
            "Button4" : {"text" : "",
                "link" : "#"},
            "Button5" : {"text" : "",
                "link" : "#"},
            "Button6" : {"text" : "Back",
                "link" : "page_3"}
        }
    }
    return render(request, 'maxkiosk/index.html', context=context)

def page_4c(request):
    context_4c = {
        "text": "Options",
        "links" : {
            "Button1" : {"text" : "Print",
                "link" : "#"},
            "Button2" : {"text" : "",
                "link" : "#"},
            "Button3" : {"text" : "",
                "link" : "#"},
            "Button4" : {"text" : "",
                "link" : "#"},
            "Button5" : {"text" : "",
                "link" : "#"},
            "Button6" : {"text" : "Back",
                "link" : "page_3"}
        }
    }
    return render(request, 'maxkiosk/index.html', context = context_4c)

def page_4d(request):
    context_4d = {
        "text": "Options",
        "links": {
            "Button1": {"text": "Print",
                        "link": "#"},
            "Button2": {"text": "",
                        "link": "#"},
            "Button3": {"text": "",
                        "link": "#"},
            "Button4": {"text": "",
                        "link": "#"},
            "Button5": {"text": "",
                        "link": "#"},
            "Button6": {"text": "Back",
                        "link": "page_4d"}
        }
    }
    return render(request, 'maxkiosk/index.html', context=context_4d)

def page_4e(request):
    return render(request, 'maxkiosk/page_4e.html')

def page_5(request):
    return render(request, 'maxkiosk/page_5.html')

