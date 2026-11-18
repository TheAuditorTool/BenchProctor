# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

def BenchmarkTest00322(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    form = FormData(payload=auth_header)
    data = form.payload
    try:
        _coerced = float(data)
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid number'}, status=400)
    processed = _coerced
    eval(str(processed))
    return JsonResponse({"saved": True})
