# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import auth_check


def BenchmarkTest38415(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    if not auth_check(str(graphql_var), request.session.get('token')):
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({"saved": True})
