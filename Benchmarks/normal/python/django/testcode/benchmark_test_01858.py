# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest01858(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = f'{origin_value}'
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(data),))
    return JsonResponse({"saved": True})
