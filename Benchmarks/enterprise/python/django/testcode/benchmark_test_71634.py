# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest71634(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    if str(graphql_var) == 'is_admin':
        return JsonResponse({'access': 'granted', 'role': 'admin'}, status=200)
    return JsonResponse({"saved": True})
