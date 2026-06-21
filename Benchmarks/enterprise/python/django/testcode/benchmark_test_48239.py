# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
import os


def BenchmarkTest48239(request):
    env_value = os.environ.get('USER_INPUT', '')
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
