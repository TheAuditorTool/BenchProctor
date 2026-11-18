# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest00389(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = (lambda v: v.strip())(ua_value)
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(data),))
    value = result['name']
    return JsonResponse({'name': str(value)}, status=200)
