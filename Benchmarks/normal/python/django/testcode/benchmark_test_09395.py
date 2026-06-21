# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import html
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest09395(request):
    raw_body = request.body.decode('utf-8')
    data = FormData(payload=raw_body).payload
    processed = html.escape(data)
    return HttpResponse(mark_safe('<img src="' + str(processed) + '">'))
