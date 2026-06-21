# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest56561(request):
    env_value = os.environ.get('USER_INPUT', '')
    return JsonResponse({'error': str(env_value), 'stack': repr(locals())}, status=500)
