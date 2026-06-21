# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest52069(request):
    multipart_value = request.POST.get('multipart_field', '')
    ctx = RequestContext(multipart_value)
    data = ctx.payload
    request.session.set_expiry(1800)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
