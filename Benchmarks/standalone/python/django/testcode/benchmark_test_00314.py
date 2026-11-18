# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import db


def BenchmarkTest00314(request):
    env_value = os.environ.get('APP_INPUT', '')
    kind = 'json' if str(env_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(env_value).strip()
        case _:
            data = str(env_value)
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(data),))
    if result is None:
        return JsonResponse({'error': 'not found'}, status=404)
    value = result['name']
    return JsonResponse({'name': str(value)}, status=200)
