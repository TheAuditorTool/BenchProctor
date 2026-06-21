# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
from types import SimpleNamespace


def BenchmarkTest76657(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    ns = SimpleNamespace(payload=ua_value)
    data = getattr(ns, 'payload')
    return HttpResponse('<html><body><h1>' + str(data) + '</h1></body></html>', content_type='text/html')
