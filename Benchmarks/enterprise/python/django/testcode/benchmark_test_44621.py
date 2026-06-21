# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
import os


def BenchmarkTest44621(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
