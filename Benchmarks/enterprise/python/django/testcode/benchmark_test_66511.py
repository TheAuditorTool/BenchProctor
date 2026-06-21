# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def coalesce_blank(value):
    return value or ''

def BenchmarkTest66511(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = coalesce_blank(graphql_var)
    if len(str(data)) >= 4:
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
