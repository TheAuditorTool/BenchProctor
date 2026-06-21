# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest78166(request):
    env_value = os.environ.get('USER_INPUT', '')
    if env_value not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = env_value
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
