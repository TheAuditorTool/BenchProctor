# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest01616(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    db.execute('UPDATE users SET role = ? WHERE name = ?', ('admin', str(header_value)))
    return JsonResponse({"saved": True})
