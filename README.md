# Fandjango Example

This repository consists of a sample Facebook application powered by the [Fandjango](http://github.com/jgorset/fandjango) library
and a walkthrough to replicate it.

## Walkthrough

### Register a Facebook application

First of all, we'll need to register a new application with the Facebook platform. To do so,
go to [facebook.com/developers](http://www.facebook.com/developers) and create your application.
Once you have convinced Facebook that you are in fact human, you'll be presented with a daunting
number of options. Don't worry, though; they're all optional and we only need to configure two of
them right now:

* *App namespace* - The URL you'd like your application to be accessed from, e.g. `http://apps.facebook.com/myapp`.
* *Canvas URL* - The URL that Facebook may load your application from, e.g. `http://myserver.com`.

### Create a new Django project

Next, create a new Django project and install Fandjango:

    $ django-admin.py startproject myfacebookapplication
    $ pip install fandjango
    
Add fandjango to `INSTALLED_APPS` in your settings file.
    
### Configure Fandjango

Fandjango needs some configuration. Specifically, you need to add its middleware to your middleware classes and specify
your application's id, secret key and namespace (all of which can be found on [facebook.com/developers](http://www.facebook.com/developers))
in your settings file:

    FACEBOOK_APPLICATION_ID = 181259711925270
    FACEBOOK_APPLICATION_SECRET_KEY = '214e4cb484c28c35f18a70a3d735999b'
    FACEBOOK_APPLICATION_NAMESPACE = 'myapp'
    
    MIDDLEWARE_CLASSES = [
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'fandjango.middleware.FacebookMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
    ]
    
Finally, synchronize your database to install Fandjango's models:

    $ python manage.py syncdb

*Note:* If you're using Django's built-in CSRF protection middleware, you need to make sure Fandjango's
middleware precedes it. Otherwise, Facebook's requests to your application will qualify cross-site
request forgeries.

### Develop the application

    # urls.py
    
    urlpatterns = patterns('',
        # Examples:
        url(r'^$', 'fandjangoexample.views.home', name='home'),
    )
    
    # views.py
    
    from django.http import HttpResponse
    from fandjango.decorators import facebook_authorization_required

    @facebook_authorization_required
    def home(request):
        return HttpResponse('Hello, %s' % request.facebook.user.first_name)

### Sit back and enjoy

That's it! You have created a Facebook application that authorizes and greets its users. Navigate to your
application's canvas URL to have a closer look at your new marvel of technology.

### Where do I go from here?

You should [read the documentation](readthedocs.org/docs/fandjango)
and [browse the source code](http://github.com/jgorset/fandjango).
