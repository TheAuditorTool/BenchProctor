# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

def BenchmarkTest00236(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    form = FormData(payload=ua_value)
    data = form.payload
    exec(str(data))
    return JsonResponse({"saved": True})
