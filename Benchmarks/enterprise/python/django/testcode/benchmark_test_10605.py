# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest10605(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = FormData(payload=origin_value).payload
    return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
