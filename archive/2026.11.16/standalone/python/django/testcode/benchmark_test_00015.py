# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

def BenchmarkTest00015(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    form = FormData(payload=referer_value)
    data = form.payload
    try:
        _coerced = float(data)
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid number'}, status=400)
    processed = _coerced
    exec(str(processed))
    return JsonResponse({"saved": True})
