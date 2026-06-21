# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest08460(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    prefix = ''
    data = prefix + str(graphql_var)
    if str(data) in ('admin', 'true', 'authenticated'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
