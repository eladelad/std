from notes.models import UserProfile
from django.core.validators import validate_email
import json



class ReplaceEmailByUser(object):
    def process_request(self, request):
        if request.path == "/api-token-auth/":
            if request.method == 'POST' and hasattr(request, 'body'):
                body = request.body
                json_data = json.loads(body)
                json_data['password']="test"
                request._body = str(json.dumps(json_data))
                request.DATA = json_data
                return None
                if 'username' in json_data:
                    username = str(json_data['username'])
                    if validateEmail(username):
                        try:
                            user = UserProfile.objects.get(email=username)
                        except UserProfile.DoesNotExist:
                            user = None
                        if user is not None:
                            username = user.username
                            #json_data['username']=username
                            json_data['password']=username
                            request._body = str(json.dumps(json_data))
                            test= ""
                            return None

def validateEmail( email ):
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError
    try:
        validate_email( email )
        return True
    except ValidationError:
        return False