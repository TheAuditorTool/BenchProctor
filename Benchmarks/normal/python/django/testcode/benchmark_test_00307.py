# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from django.http import HttpResponse
import unicodedata


def coalesce_blank(value):
    return value or ''

def BenchmarkTest00307(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = coalesce_blank(env_value)
    normalized = unicodedata.normalize('NFKC', str(data))
    return HttpResponse('<p>' + normalized + '</p>', content_type='text/html')
