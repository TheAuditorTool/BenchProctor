# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def ensure_str(value):
    return str(value)

def BenchmarkTest05853(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = ensure_str(header_value)
    db.execute('UPDATE users SET name = ?', (str(data),))
    return JsonResponse({"saved": True})
