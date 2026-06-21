# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def ensure_str(value):
    return str(value)

def BenchmarkTest13809(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = ensure_str(host_value)
    db.execute('UPDATE users SET role = ? WHERE name = ?', ('admin', str(data)))
    return JsonResponse({"saved": True})
