# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import os


def BenchmarkTest42396(request):
    env_value = os.environ.get('USER_INPUT', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(env_value)
    data = collected
    digest = hashlib.sha256(('static_salt_123' + str(data)).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
