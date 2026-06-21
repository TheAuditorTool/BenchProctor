# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest26409(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    prefix = ''
    data = prefix + str(forwarded_ip)
    db.execute('UPDATE users SET role = ? WHERE name = ?', ('admin', str(data)))
    return JsonResponse({"saved": True})
