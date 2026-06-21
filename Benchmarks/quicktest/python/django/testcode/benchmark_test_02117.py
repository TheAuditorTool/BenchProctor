# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest02117(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = default_blank(header_value)
    db.execute('UPDATE users SET name = ?', (str(data),))
    return JsonResponse({"saved": True})
