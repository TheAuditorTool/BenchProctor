# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest66118(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = f'{header_value}'
    db.execute('UPDATE users SET name = ?', (str(data),))
    return JsonResponse({"saved": True})
