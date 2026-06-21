# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import unicodedata


def BenchmarkTest52850(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data, _sep, _rest = str(forwarded_ip).partition('\x00')
    normalized = unicodedata.normalize('NFKC', str(data))
    return HttpResponse('<p>' + normalized + '</p>', content_type='text/html')
