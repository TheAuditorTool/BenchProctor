# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest59372(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    db.execute('INSERT INTO admin_actions (cmd) VALUES (?)', (str(ua_value),))
    return JsonResponse({"saved": True})
