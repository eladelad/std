import re
from django.contrib.sites.models import get_current_site
from django.shortcuts import redirect

class RedirectToPrivate(object):
    def process_request(self, request):
        if get_current_site(request).domain == "my.klipbord.co":
            path = request.path.encode()
            #user = request.user
            if 'Kbkbuser' in request.COOKIES:
                username = request.COOKIES.get('Kbkbuser')
                return redirect("http://"+username+".my.klipbord.co"+path)
            else:
                return redirect("http://www.klipbord.co/")
