# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


def BenchmarkTest00156(request):
    env_value = os.environ.get('APP_INPUT', '')
    try:
        data = json.loads(env_value).get('value', env_value)
    except (json.JSONDecodeError, AttributeError):
        data = env_value
    try:
        _coerced = float(data)
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid number'}, status=400)
    processed = _coerced
    code = compile(str(processed), '<rule>', 'exec')
    exec(code)
    return JsonResponse({"saved": True})
