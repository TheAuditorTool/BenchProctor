# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest44384(request):
    raw_body = request.body.decode('utf-8')
    data = FormData(payload=raw_body).payload
    return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
