from django.contrib.auth import authenticate, login
from django.conf import settings
import datetime

class AuthMiddleWare(object):
    def process_request(self, request):
            if 'TOKENCOOKIE' in request.COOKIES:
                token = request.COOKIES.get('TOKENCOOKIE')
                user = authenticate(token = request.COOKIES.get('TOKENCOOKIE'))
                #authenticate(remote_user = request.COOKIES.get('TOKENCOOKIE'))
                #token, attribute, role = identity_manager.get_attributes( token )
                #user = authenticate(remote_user=attribute['uid'][0])
                #request.user = user
                #login(request, user)


    # def process_response(self, request, response):
    #
    #     if hasattr(response, 'data'):
    #         if 'token' in response.data:
    #             max_age = 365 * 24 * 60 * 60
    #             expires = datetime.datetime.strftime(datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age), "%a, %d-%b-%Y %H:%M:%S GMT")
    #             domain = 'klipbord.co'
    #             response.set_cookie(key='TOKENCOOKIE', value=response.data['token'], expires=expires, domain=domain, secure=settings.SESSION_COOKIE_SECURE or None)
    #     return response
