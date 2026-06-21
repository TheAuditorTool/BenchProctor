# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def to_text(value):
    return str(value).strip()

def BenchmarkTest24200(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = to_text(env_value)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
