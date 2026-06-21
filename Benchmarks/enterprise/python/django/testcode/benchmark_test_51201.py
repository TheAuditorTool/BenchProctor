# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest51201(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(forwarded_ip),))
    value = result['name']
    return JsonResponse({'name': str(value)}, status=200)
