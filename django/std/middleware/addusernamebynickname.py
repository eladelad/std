from django.contrib.auth import authenticate
from django.conf import settings

class ReplaceUserByNickname(object):
    def process_request(self, request):
        if request.path == "/register":
            if not request.method in ('GET', 'HEAD', 'OPTIONS', 'TRACE'):
                if hasattr(request, 'body'):
                    request.body = request.user
                else:
                    user = None