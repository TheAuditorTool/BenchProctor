# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest59524(request):
    multipart_value = request.POST.get('multipart_field', '')
    ctx = RequestContext(multipart_value)
    data = ctx.payload
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    return HttpResponse(Template(processed).render(Context()))
