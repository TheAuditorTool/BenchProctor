# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest27686(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    if ua_value:
        data = ua_value
    else:
        data = ''
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(data),))
    return JsonResponse({"saved": True})
