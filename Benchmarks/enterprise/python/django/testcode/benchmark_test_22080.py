# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


def normalise_input(value):
    return value.strip()

def BenchmarkTest22080(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = normalise_input(graphql_var)
    if data not in ('ls', 'cat', 'date', 'whoami'):
        return JsonResponse({'error': 'forbidden'}, status=403)
    processed = data
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
