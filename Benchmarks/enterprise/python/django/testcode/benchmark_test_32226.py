# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
import os


def BenchmarkTest32226(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % (env_value,)
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
