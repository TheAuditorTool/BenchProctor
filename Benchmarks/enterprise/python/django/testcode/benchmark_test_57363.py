# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest57363(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    db.execute('DELETE FROM accounts WHERE id = ?', (str(forwarded_ip),))
    return JsonResponse({"saved": True})
