"""
Minimal Django configuration to demonstrate Dependabot transitive dependency issue.
"""
import os
import django
from django.conf import settings
from django.http import JsonResponse
from django.urls import path

# Minimal Django settings
if not settings.configured:
    settings.configure(
        DEBUG=True,
        SECRET_KEY='demo-secret-key-not-for-production',
        ROOT_URLCONF=__name__,
        ALLOWED_HOSTS=['*'],
    )
    django.setup()


def hello(request):
    """Simple view that returns JSON."""
    return JsonResponse({'message': 'Hello World!'})


urlpatterns = [
    path('', hello),
]


if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    execute_from_command_line(['manage.py', 'runserver', '0.0.0.0:8000'])
