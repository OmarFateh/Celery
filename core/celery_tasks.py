from __future__ import absolute_import, unicode_literals
import os

from celery import Celery


# set a default value for the DJANGO_SETTINGS_MODULE environment variable so that Celery will know how to find the Django project.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
# creat a new Celery instance, with the name core, and assigned the value to a variable called app.
app = Celery("core")
# use namespace="CELERY" to prevent clashes with other Django settings. All config settings for Celery must be prefixed with CELERY_, in other words.
app.config_from_object("django.conf:settings", namespace="CELERY")
# tells Celery to look for Celery tasks from applications defined in settings.INSTALLED_APPS.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))