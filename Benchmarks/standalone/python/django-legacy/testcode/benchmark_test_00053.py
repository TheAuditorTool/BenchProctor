# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

def BenchmarkTest00053(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    form = FormData(payload=referer_value)
    data = form.payload
    _coerced = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    processed = _coerced
    exec(str(processed))
    return JsonResponse({"saved": True})
