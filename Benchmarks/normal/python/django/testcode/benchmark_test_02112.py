# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import auth_check


def BenchmarkTest02112(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    if not auth_check(request.session.get('user', ''), str(graphql_var)):
        return JsonResponse({'error': 'forbidden'}, status=403)
    return JsonResponse({"saved": True})
