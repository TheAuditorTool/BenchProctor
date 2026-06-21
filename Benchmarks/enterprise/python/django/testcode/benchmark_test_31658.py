# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest31658(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
