# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest64703(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % str(env_value)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
