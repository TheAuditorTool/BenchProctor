# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
import os


def BenchmarkTest58097(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value}'
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
