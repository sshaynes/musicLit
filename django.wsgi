import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'musicLit.settings'

sys.path.append('/home/stephen/Documents')
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
