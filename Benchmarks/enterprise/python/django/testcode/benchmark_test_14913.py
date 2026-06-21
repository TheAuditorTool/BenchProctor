# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import db


def ensure_str(value):
    return str(value)

def BenchmarkTest14913(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = ensure_str(json_value)
    processed = data[:64]
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(processed),))
    return JsonResponse({"saved": True})
