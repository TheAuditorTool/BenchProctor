# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest09335(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data, _sep, _rest = str(forwarded_ip).partition('\x00')
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(data),))
    value = result['name']
    return JsonResponse({'name': str(value)}, status=200)
