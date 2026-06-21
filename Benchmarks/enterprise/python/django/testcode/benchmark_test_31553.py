# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest31553(request):
    xml_value = request.body.decode('utf-8')
    data = FormData(payload=xml_value).payload
    return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
