# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def ensure_str(value):
    return str(value)

def BenchmarkTest23157(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = ensure_str(forwarded_ip)
    return HttpResponse('<html><body><h1>' + str(data) + '</h1></body></html>', content_type='text/html')
