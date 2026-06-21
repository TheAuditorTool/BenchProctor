# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest47077(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    values = str(graphql_var).split(',')
    if values:
        return JsonResponse({'first': values[0], 'dropped': len(values) - 1}, status=200)
    return JsonResponse({"saved": True})
