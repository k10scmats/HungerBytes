from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.contrib.staticfiles.templatetags.staticfiles import static

reciept_url = static('maxkiosk/image.png')
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
        "content" : [
            {"heading" : "Menu",
            "body" : "Welcome!"},
            ],
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
    return render(request, 'maxkiosk/home.html', context=context)

def page_2(request):
    context = {
        "content" : [
            {"heading" : "ALERTS",
            "body" : "Earth Quake Warning"},
            {"heading" : "",
            "body" : "Be prepared to take cover to take cover. Available Resources near you can be found on the receipt."}
            ],
        "text" : "Alerts",
        "body" : "Welcome!",
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
        "body" : "Welcome!",
        "links" : {
            "Button1" : {"text" : "H and S",
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
        "body" : "Welcome!",
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
        "content" : [
            {"heading" : "Options...",
            "body" : "Welcome!"},
            {"heading" : "Options...",
            "body" : "Welcome!"},
            ],
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
        "body" : "Welcome!",
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
    return render(request, 'maxkiosk/index.html', context = context_4c)

def page_4d(request):
    context_4d = {
        "text": "Options",
        "body" : "Welcome!",
        "links": {
            "Button1": {"text": "Print",
                        "link": reciept_url},
            "Button2": {"text": "",
                        "link": "#"},
            "Button3": {"text": "",
                        "link": "#"},
            "Button4": {"text": "",
                        "link": "#"},
            "Button5": {"text": "",
                        "link": "#"},
            "Button6": {"text": "Back",
                        "link": "page_3"}
        }
    }
    return render(request, 'maxkiosk/index.html', context=context_4d)

def page_4e(request):
    context_4e = {
        "content" : [
            {"heading" : "Transit",
            "body" : "Welcome!"},
            ],
        "links": {
            "Button1": {"text": "Print",
                        "link": reciept_url},
            "Button2": {"text": "",
                        "link": "#"},
            "Button3": {"text": "",
                        "link": "#"},
            "Button4": {"text": "",
                        "link": "#"},
            "Button5": {"text": "",
                        "link": "#"},
            "Button6": {"text": "Back",
                        "link": "page_3"}
        }
    }
    return render(request, 'maxkiosk/index.html', context=context_4e)