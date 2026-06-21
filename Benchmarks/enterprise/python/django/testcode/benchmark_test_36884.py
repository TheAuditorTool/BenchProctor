# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest36884(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    db.execute('SELECT * FROM users WHERE id = ?', (origin_value,))
    return JsonResponse({"saved": True})
