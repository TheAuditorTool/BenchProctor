# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import db


def BenchmarkTest00099(request):
    graphql_var = json.loads(request.body or b'{}').get('variables', {}).get('input', '')
    data = str(graphql_var).replace('\x00', '')
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(data),))
    value = result['name']
    return JsonResponse({'name': str(value)}, status=200)
