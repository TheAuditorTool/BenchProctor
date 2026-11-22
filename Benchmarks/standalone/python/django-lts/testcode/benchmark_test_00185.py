# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

def BenchmarkTest00185(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    form = FormData(payload=auth_header)
    data = form.payload
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
