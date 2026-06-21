# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import db


def BenchmarkTest36404(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = '{}'.format(json_value)
    db.execute('SELECT * FROM users WHERE id = ?', (data,))
    return JsonResponse({"saved": True})
