# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest76866(request):
    multipart_value = request.POST.get('multipart_field', '')
    ctx = RequestContext(multipart_value)
    data = ctx.payload
    processed = data[:64]
    return HttpResponse(Template(processed).render(Context()))
