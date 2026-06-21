# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest44368(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = FormData(payload=ua_value).payload
    return HttpResponse(Template('safe block: {{ value }}').render(Context({'value': data})))
