# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


def ensure_str(value):
    return str(value)

def BenchmarkTest54615(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = ensure_str(graphql_var)
    base_name = os.path.basename(str(data))
    try:
        os.remove('/var/app/data/' + base_name)
    except OSError:
        return JsonResponse({'error': 'file error'}, status=500)
    return JsonResponse({"saved": True})
