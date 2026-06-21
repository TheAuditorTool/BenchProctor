# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest00446(request):
    upload_name = request.FILES['upload'].name
    ctx = RequestContext(upload_name)
    data = ctx.payload
    def _primary():
        return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
