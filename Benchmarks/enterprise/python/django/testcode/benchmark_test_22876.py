# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import unicodedata


def relay_value(value):
    return value

def BenchmarkTest22876(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = relay_value(host_value)
    normalized = unicodedata.normalize('NFKC', str(data))
    return HttpResponse('<p>' + normalized + '</p>', content_type='text/html')
