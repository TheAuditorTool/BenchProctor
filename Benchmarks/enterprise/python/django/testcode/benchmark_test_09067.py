# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import db


def coalesce_blank(value):
    return value or ''

def BenchmarkTest09067(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = coalesce_blank(json_value)
    db.execute('UPDATE users SET name = ?', (str(data),))
    return JsonResponse({"saved": True})
