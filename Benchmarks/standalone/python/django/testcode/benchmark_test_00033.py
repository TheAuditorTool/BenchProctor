# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.core.cache import cache
import os


def BenchmarkTest00033(request):
    env_value = os.environ.get('APP_INPUT', '')
    pending = list(str(env_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    try:
        _coerced = float(data)
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid number'}, status=400)
    processed = _coerced
    cache.set('active_tenant', str(processed), None)
    return JsonResponse({"saved": True})
