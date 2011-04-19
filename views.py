from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello, %s' % request.facebook.user.first_name)