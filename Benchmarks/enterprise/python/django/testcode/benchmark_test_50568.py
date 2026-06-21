# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import html
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest50568(request):
    user_id = request.GET.get('id', '')
    data = FormData(payload=user_id).payload
    processed = html.escape(data)
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
