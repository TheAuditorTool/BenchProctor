# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


def BenchmarkTest14578(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    base_name = os.path.basename(str(graphql_var))
    try:
        os.remove('/var/app/data/' + base_name)
    except OSError:
        return JsonResponse({'error': 'file error'}, status=500)
    return JsonResponse({"saved": True})
