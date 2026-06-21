# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest08376(request):
    host_value = request.META.get('HTTP_HOST', '')
    db.execute('UPDATE users SET password = ? WHERE id = 1', (str(host_value),))
    return JsonResponse({"saved": True})
