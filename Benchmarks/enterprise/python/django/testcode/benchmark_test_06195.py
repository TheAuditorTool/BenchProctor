# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import auth_check


def ensure_str(value):
    return str(value)

def BenchmarkTest06195(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = ensure_str(graphql_var)
    if not auth_check(str(data), request.session.get('token')):
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({"saved": True})
