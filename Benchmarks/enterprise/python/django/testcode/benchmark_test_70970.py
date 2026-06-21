# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest70970(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value}'
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
