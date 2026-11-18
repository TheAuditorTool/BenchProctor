# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import os


def BenchmarkTest00566(request):
    env_value = os.environ.get('APP_INPUT', '')
    parts = str(env_value).split(',')
    data = ' '.join(parts)
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
