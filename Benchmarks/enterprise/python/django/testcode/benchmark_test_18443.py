# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest18443(request):
    host_value = request.META.get('HTTP_HOST', '')
    db.execute('SELECT * FROM users WHERE id = ?', (host_value,))
    return JsonResponse({"saved": True})
