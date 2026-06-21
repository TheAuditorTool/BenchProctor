# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest66037(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    db.execute('SELECT * FROM users WHERE id = ' + str(ua_value))
    return JsonResponse({"saved": True})
