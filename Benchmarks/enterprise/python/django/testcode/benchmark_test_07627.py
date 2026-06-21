# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest07627(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    db.execute('DELETE FROM accounts WHERE id = ?', (str(ua_value),))
    return JsonResponse({"saved": True})
