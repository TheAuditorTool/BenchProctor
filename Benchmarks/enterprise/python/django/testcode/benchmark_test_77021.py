# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import re
import json


def BenchmarkTest77021(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    def normalize(value):
        return value.strip()
    data = normalize(graphql_var)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
