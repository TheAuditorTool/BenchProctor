# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import json
from app_runtime import auth_check


def BenchmarkTest67289(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data, _sep, _rest = str(graphql_var).partition('\x00')
    if not auth_check('user', hashlib.sha256(str(data).encode()).hexdigest()):
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({"saved": True})
