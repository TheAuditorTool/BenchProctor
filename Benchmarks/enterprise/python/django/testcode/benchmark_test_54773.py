# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
import os


def BenchmarkTest54773(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = ' '.join(str(env_value).split())
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
