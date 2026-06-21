# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest60922(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
