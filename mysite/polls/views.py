from django.http import Httpresponse

# Create your views here.
def index(request):
    return Httpresponse("Hello world. You are at the polls index")
    