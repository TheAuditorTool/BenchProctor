# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest34010(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = bytes.fromhex(header_value).decode('utf-8', 'ignore')
    db.execute('SELECT * FROM users WHERE id = :id', {'id': data})
    return JsonResponse({"saved": True})
