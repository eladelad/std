import re
from django.core.validators import validate_email


class ReplaceEmailByUser(object):
    def process_request(self, request):
        if request.path == "/api-token-auth/":
            if request.method == 'POST' and request.POST.has_key('username') and request.POST.has_key('password'):
                if email_re.match(request.POST['username']):
                    username = UserProfile.objects.get(username=request.POST['username'])
                    request.POST['username'] = username