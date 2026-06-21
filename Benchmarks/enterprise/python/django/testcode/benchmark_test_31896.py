# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import db


def normalise_input(value):
    return value.strip()

def BenchmarkTest31896(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = normalise_input(json_value)
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(data),))
    return JsonResponse({'record': str(record)}, status=200)
