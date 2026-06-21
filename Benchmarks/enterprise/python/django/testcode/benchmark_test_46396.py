# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
from django.template import Template, Context


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest46396(request):
    user_id = request.GET.get('id', '')
    ctx = RequestContext(user_id)
    data = ctx.payload
    return HttpResponse(Template('{{ value }}').render(Context({'value': data})))
