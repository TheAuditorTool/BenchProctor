# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest34492(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = host_value if host_value else 'default'
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return JsonResponse({"saved": True})
