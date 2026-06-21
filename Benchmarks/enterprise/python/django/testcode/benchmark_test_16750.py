# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from django.http import HttpResponse
import unicodedata


def relay_value(value):
    return value

def BenchmarkTest16750(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = relay_value(env_value)
    normalized = unicodedata.normalize('NFKC', str(data))
    return HttpResponse('<p>' + normalized + '</p>', content_type='text/html')
