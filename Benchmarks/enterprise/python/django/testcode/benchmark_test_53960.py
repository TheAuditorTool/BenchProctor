# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import json
from app_runtime import auth_check


def BenchmarkTest53960(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    parts = str(graphql_var).split(',')
    data = ','.join(parts)
    if not auth_check('user', hashlib.sha256(str(data).encode()).hexdigest()):
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({"saved": True})
