# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import db


def BenchmarkTest00118(request):
    env_value = os.environ.get('APP_INPUT', '')
    data = '{}'.format(env_value)
    try:
        _coerced = int(data)
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid integer'}, status=400)
    processed = _coerced
    db.execute('SELECT * FROM users WHERE id = ' + str(processed))
    return JsonResponse({"saved": True})
