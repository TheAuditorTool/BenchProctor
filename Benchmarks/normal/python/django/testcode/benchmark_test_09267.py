# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest09267(request):
    host_value = request.META.get('HTTP_HOST', '')
    db.execute('DELETE FROM accounts WHERE id = ?', (str(host_value),))
    return JsonResponse({"saved": True})
