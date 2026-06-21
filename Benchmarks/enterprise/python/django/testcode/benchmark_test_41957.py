# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest41957(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = f'{header_value:.200s}'
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(data),))
    value = result['name']
    return JsonResponse({'name': str(value)}, status=200)
