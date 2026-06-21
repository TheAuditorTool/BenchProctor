# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import json


def normalise_input(value):
    return value.strip()

def BenchmarkTest24354(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = normalise_input(graphql_var)
    if not re.match(r'^.{1,256}$', str(data)):
        return JsonResponse({'error': 'schema invalid'}, status=400)
    if len(str(data)) >= 4:
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
