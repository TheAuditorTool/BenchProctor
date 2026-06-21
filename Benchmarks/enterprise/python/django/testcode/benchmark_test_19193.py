# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django.http import HttpResponse


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest19193(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    ctx = RequestContext(forwarded_ip)
    data = ctx.payload
    def _primary():
        return HttpResponse('<script src="' + str(data) + '"></script>', content_type='text/html')
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
