# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import db


def BenchmarkTest60319(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    try:
        data = json.loads(origin_value).get('value', origin_value)
    except (json.JSONDecodeError, AttributeError):
        data = origin_value
    db.execute('INSERT INTO admin_actions (cmd) VALUES (?)', (str(data),))
    return JsonResponse({"saved": True})
