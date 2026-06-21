# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest61697(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    try:
        result = int(str(graphql_var))
    except Exception:
        pass
    return JsonResponse({"saved": True})
