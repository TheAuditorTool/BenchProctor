# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import unicodedata


def coalesce_blank(value):
    return value or ''

def BenchmarkTest08503(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = coalesce_blank(forwarded_ip)
    normalized = unicodedata.normalize('NFKC', str(data))
    return HttpResponse('<p>' + normalized + '</p>', content_type='text/html')
