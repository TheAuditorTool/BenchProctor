# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import auth_check


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest38183(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = default_blank(graphql_var)
    if not auth_check(str(data), request.session.get('token')):
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({"saved": True})
