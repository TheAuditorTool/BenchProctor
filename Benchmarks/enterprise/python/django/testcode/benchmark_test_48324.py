# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def normalise_input(value):
    return value.strip()

def BenchmarkTest48324(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = normalise_input(env_value)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
