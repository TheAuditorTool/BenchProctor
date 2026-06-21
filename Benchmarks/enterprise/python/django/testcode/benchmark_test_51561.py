# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest51561(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = f'{graphql_var:.200s}'
    if str(data).endswith(('/public', '/static', '/.')):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
