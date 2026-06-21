# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import db


def BenchmarkTest68793(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    db.execute('SELECT * FROM users WHERE id = :id', {'id': json_value})
    return JsonResponse({"saved": True})
