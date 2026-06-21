# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse


def coalesce_blank(value):
    return value or ''

def BenchmarkTest46057(request):
    upload_name = request.FILES['upload'].name
    data = coalesce_blank(upload_name)
    return HttpResponse(Template('safe block: {{ value }}').render(Context({'value': data})))
