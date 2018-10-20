from django.shortcuts import render
from django.http import HttpResponse
from .models import User

# Create your views here.

def get_button_list(box=(860, 420, 1130, 640), n_buttons = 6, bgr=0.8, height=60, link_list=["page.html"]):
    coord_list = [[0,0,0,0]]
    return zip(link_list, coord_list)

def index(request):
    # latest_user = User.object.order_by('-pub_date')[:5]

    context = {
        "name" : "Jon",
        "button_list" : get_button_list(box=(860, 420, 1130, 640), n_buttons = 6, bgr=0.8, height=60),
        # "user list" : latest_user
    }
    return render(request, 'maxkiosk/index.html', context=context)