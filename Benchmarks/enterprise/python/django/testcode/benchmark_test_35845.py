# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def coalesce_blank(value):
    return value or ''

def BenchmarkTest35845(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = coalesce_blank(env_value)
    if data not in ('ls', 'cat', 'date', 'whoami'):
        return JsonResponse({'error': 'forbidden'}, status=403)
    processed = data
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
