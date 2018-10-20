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
            "body" : "Be prepared to take cover to take cover."} ,
            {"heading" : "",
            "body" : "Available Resources near you can be found on the receipt."]},
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
        "content" : [
            {"heading" : "Oh Hi Mark.",
            "body" : "Find what you need when and where you need it!"},
            ],
        "links" : {
            "Button1" : {"text" : "Shelter",
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
        "content" : [
            {"heading" : "St. Francis Dining Hall 8AM - 5PM - 2 miles",
            "body" : "330 SE 11th Ave"},
            {"heading" : "Portland Rescue Mission – 1 mile",
            "body" : "111 W Burnside Street"},
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


def page_4b(request):
    context = {
        "content" : [
            {"heading" : "Showers: Portland Rescue Mission - 1 mile",
            "body" : "111 W Burnside Street"},
            {"heading" : "Clothing: Saint Andre Bassette Catholic Church - 1 miles",
            "body" : "601 W Burnside Street"},
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
        "content" : [
            {"heading" : "Soup Kitchen: Operation Nightwatch - 0.5 mile",
            "body" : "1432 SW 13th Ave"},
            {"heading" : "Sack Lunches/Dinners: Union Gospel Mission",
            "body" : "1432 SW 13th Ave"},
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
    return render(request, 'maxkiosk/index.html', context = context_4c)

def page_4d(request):
    context_4d = {
        "content" : [
            {"heading" : "Hospital: Legacy Heath – 2 miles",
            "body" : "2801 N Vancouver Ave"},
            {"heading" : "Health Screenings/Tests: Outside In – 4 miles",
            "body" : "1132 SW 13th Ave"},
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
    return render(request, 'maxkiosk/index.html', context=context_4d)

def page_4e(request):
    context_4e = {
        "content" : [
            {"heading" : "Disability: Ride Connection – 0.8 mile",
            "body" : "9955 NE 65th Ave"},
            {"heading" : "Youth Transport: National Runaway Safeline - 2 miles",
            "body" : "31418 N Lincoln Ave"},
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