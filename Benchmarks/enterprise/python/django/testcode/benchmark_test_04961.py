# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest04961(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = default_blank(graphql_var)
    if str(data).endswith(('/public', '/static', '/.')):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
