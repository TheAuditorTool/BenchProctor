# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest64551(request):
    host_value = request.META.get('HTTP_HOST', '')
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(host_value),))
    value = result['name']
    return JsonResponse({'name': str(value)}, status=200)
