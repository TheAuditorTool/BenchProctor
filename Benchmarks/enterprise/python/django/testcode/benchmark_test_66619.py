# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest66619(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    def normalize(value):
        return value.strip()
    data = normalize(referer_value)
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return JsonResponse({"saved": True})
