# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import db


def coalesce_blank(value):
    return value or ''

def BenchmarkTest54109(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = coalesce_blank(graphql_var)
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(data),))
    value = result['name']
    return JsonResponse({'name': str(value)}, status=200)
