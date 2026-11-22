# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import db


def BenchmarkTest00052(request):
    env_value = os.environ.get('APP_INPUT', '')
    data = str(env_value).replace('\x00', '')
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(data),))
    if result is None:
        return JsonResponse({'error': 'not found'}, status=404)
    value = result['name']
    return JsonResponse({'name': str(value)}, status=200)
