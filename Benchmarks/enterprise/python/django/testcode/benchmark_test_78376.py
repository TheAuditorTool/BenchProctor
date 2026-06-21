# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest78376(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(referer_value),))
    return JsonResponse({"saved": True})
