# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import os


def relay_value(value):
    return value

def BenchmarkTest68170(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = relay_value(env_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    with open('output.csv', 'a') as fh:
        fh.write(str(processed) + ',data\n')
    return JsonResponse({"saved": True})
