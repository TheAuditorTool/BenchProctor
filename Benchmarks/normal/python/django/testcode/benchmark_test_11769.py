# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def ensure_str(value):
    return str(value)

def BenchmarkTest11769(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = ensure_str(graphql_var)
    if str(data).endswith(('/public', '/static', '/.')):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
