# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import db


def BenchmarkTest40554(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(json_value),))
    return JsonResponse({'record': str(record)}, status=200)
