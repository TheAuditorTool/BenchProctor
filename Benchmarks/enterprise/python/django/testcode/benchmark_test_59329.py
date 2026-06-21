# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import auth_check


def BenchmarkTest59329(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(graphql_var)
    data = collected
    if auth_check('user', str(data)):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
