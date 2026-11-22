# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.core.cache import cache
import json


def BenchmarkTest00180(request):
    raw_body = request.body.decode('utf-8')
    try:
        data = json.loads(raw_body).get('value', raw_body)
    except (json.JSONDecodeError, AttributeError):
        data = raw_body
    try:
        _coerced = float(data)
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid number'}, status=400)
    processed = _coerced
    cache.set('active_tenant', str(processed), None)
    return JsonResponse({"saved": True})
