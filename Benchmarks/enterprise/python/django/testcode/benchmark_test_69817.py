# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import db


def BenchmarkTest69817(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(graphql_var),))
    if result is None:
        return JsonResponse({'error': 'not found'}, status=404)
    value = result['name']
    return JsonResponse({'name': str(value)}, status=200)
