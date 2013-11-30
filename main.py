import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'djangoappengine.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
