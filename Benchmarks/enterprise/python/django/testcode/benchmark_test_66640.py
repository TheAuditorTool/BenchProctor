# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest66640(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(ua_value),))
    return JsonResponse({"saved": True})
