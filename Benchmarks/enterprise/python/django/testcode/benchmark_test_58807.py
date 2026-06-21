# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def coalesce_blank(value):
    return value or ''

def BenchmarkTest58807(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = coalesce_blank(forwarded_ip)
    db.execute('UPDATE users SET role = ? WHERE name = ?', ('admin', str(data)))
    return JsonResponse({"saved": True})
