# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest26796(request):
    env_value = os.environ.get('USER_INPUT', '')
    try:
        result = int(str(env_value))
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({"saved": True})
