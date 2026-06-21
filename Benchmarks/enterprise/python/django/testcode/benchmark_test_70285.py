# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def coalesce_blank(value):
    return value or ''

def BenchmarkTest70285(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = coalesce_blank(graphql_var)
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return JsonResponse({'access': 'granted', 'role': 'admin'}, status=200)
    return JsonResponse({"saved": True})
