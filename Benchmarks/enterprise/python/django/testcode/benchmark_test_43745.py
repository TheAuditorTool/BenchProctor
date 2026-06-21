# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest43745(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(origin_value),))
    return JsonResponse({"saved": True})
