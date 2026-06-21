# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import db


def BenchmarkTest51929(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    try:
        data = json.loads(header_value).get('value', header_value)
    except (json.JSONDecodeError, AttributeError):
        data = header_value
    db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return JsonResponse({"saved": True})
