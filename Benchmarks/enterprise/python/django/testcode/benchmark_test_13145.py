# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import unicodedata


def BenchmarkTest13145(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = str(host_value).replace('\x00', '')
    normalized = unicodedata.normalize('NFKC', str(data))
    return HttpResponse('<p>' + normalized + '</p>', content_type='text/html')
