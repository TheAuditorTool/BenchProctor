# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import os


def BenchmarkTest00705(request):
    env_value = os.environ.get('APP_INPUT', '')
    if env_value:
        data = env_value
    else:
        data = ''
    digest = hashlib.md5(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
