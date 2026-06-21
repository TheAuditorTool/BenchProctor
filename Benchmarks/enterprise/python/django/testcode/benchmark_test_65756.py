# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest65756(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    try:
        int(str(graphql_var))
    except ValueError:
        return JsonResponse({'error': 'invalid'}, status=400)
    return JsonResponse({"saved": True})
