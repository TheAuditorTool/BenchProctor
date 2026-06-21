# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


def BenchmarkTest45626(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    try:
        os.setuid(int(str(graphql_var)) if str(graphql_var).isdigit() else 65534)
    except OSError:
        return JsonResponse({'error': 'privilege drop failed'}, status=500)
    return JsonResponse({"saved": True})
