Title: Useful Django admin improvements
Date: 2018-04-02 21:58
Category: Django, Programming
Tags: django, python

A few improvements that will improve your django admin application.

##### Improve security of your Django admin:
Add [Django Admin Honeypot](https://github.com/dmpayton/django-admin-honeypot).
It is a fake Django admin login screen to log and notify admins of attempted unauthorized access.
Also I recommend you to change your *real* admin url to URL with 20+ random string.
You can generate this random string from terminal with python just in one line:
```python
''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20))
```
Django-admin-honeypot pulls the users IP address from the REMOTE_ADDR request header.
Don't forget to create MIDDLEWARE.
Example of MIDDLEWARE:
```python
def RemoteAddrMiddleware(get_response):  # noqa
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        request.META['REMOTE_ADDR'] = ip

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware
```

##### Visually distinguish environments in Django Admin
For this option you can use [django-admin-env-notice](https://github.com/dizballanze/django-admin-env-notice).
The code is pretty simple and you can implement with own files without 3th party app.
Really cool, right? :)

##### Order your models and apps.
As soon as your application grows, the more you want to put it in order.
For this case I recommend to use [django-modeladmin-order](https://github.com/mishbahr/django-modeladmin-reorder).
Now you can order as you wish your django apps. Also it has other interesting features. More detail you can find at link
above. If you use other apps, you can leave a comment under this post.

##### Get all your project models on one single page with charts and whistles.
We work with Agile methodologies. Very often every project has custom User model.
For this case I recommend you to use [django-controlcenter](https://github.com/byashimov/django-controlcenter)
The first pretty useful chart we use for SaaS projects is BarChart with user registrations.
Every Monday we can take a look for the registrations of our project. Very useful and easy to implement.
This library has a great documentation.

##### Add `raw_id_fields` for fields with ForeignKey.
By default, Django’s admin uses a select-box interface (<select\>) for fields that are ForeignKey.
Sometimes you don’t want to incur the overhead of having to select all the related instances to display in the drop-down.
It will increase time while your DB will execute query to get them all.
More detail at [Django docs](https://docs.djangoproject.com/en/2.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.raw_id_fields).


All these simple things will help to increase developer productivity and make your life more easier at your project.
Do you have other useful advice? I'm ready to listen!)
