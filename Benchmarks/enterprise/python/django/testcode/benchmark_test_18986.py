# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest18986(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    parts = str(referer_value).split(',')
    data = ','.join(parts)
    db.execute('UPDATE users SET role = ? WHERE name = ?', ('admin', str(data)))
    return JsonResponse({"saved": True})
