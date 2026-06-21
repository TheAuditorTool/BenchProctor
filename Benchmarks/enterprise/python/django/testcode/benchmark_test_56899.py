# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import db


def BenchmarkTest56899(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    def normalize(value):
        return value.strip()
    data = normalize(json_value)
    db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return JsonResponse({"saved": True})
