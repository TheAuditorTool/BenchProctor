# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest77678(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    if forwarded_ip:
        data = forwarded_ip
    else:
        data = ''
    db.execute('UPDATE users SET password = ? WHERE id = 1', (str(data),))
    return JsonResponse({"saved": True})
