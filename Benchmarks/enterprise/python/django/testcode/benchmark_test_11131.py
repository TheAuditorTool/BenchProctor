# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse


def coalesce_blank(value):
    return value or ''

def BenchmarkTest11131(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = coalesce_blank(ua_value)
    return HttpResponse(Template('safe block: {{ value }}').render(Context({'value': data})))
