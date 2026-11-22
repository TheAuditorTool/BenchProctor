# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

def BenchmarkTest00211(request):
    user_id = request.GET.get('id', '')
    form = FormData(payload=user_id)
    data = form.payload
    try:
        _coerced = float(data)
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid number'}, status=400)
    processed = _coerced
    request.session['data'] = str(processed)
    return JsonResponse({"saved": True})
