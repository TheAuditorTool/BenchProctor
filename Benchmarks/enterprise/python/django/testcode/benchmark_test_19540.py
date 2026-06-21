# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import os


def BenchmarkTest19540(request):
    env_value = os.environ.get('USER_INPUT', '')
    def normalize(value):
        return value.strip()
    data = normalize(env_value)
    digest = hashlib.sha1(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
