# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def coalesce_blank(value):
    return value or ''

def BenchmarkTest06613(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = coalesce_blank(host_value)
    db.execute('UPDATE users SET role = ? WHERE name = ?', ('admin', str(data)))
    return JsonResponse({"saved": True})
