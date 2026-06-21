# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest20539(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(header_value),))
    value = result['name']
    return JsonResponse({'name': str(value)}, status=200)
