# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse


def ensure_str(value):
    return str(value)

def BenchmarkTest37707(request):
    xml_value = request.body.decode('utf-8')
    data = ensure_str(xml_value)
    return HttpResponse(Template('safe block: {{ value }}').render(Context({'value': data})))
