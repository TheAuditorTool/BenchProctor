# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import auth_check


def BenchmarkTest57322(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    try:
        granted = auth_check('resource', str(graphql_var))
    except Exception:
        granted = True
    if not granted:
        return JsonResponse({'error': 'forbidden'}, status=403)
    return JsonResponse({"saved": True})
