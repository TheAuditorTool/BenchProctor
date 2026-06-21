# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import os


def relay_value(value):
    return value

def BenchmarkTest06706(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = relay_value(env_value)
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(digest)
    return JsonResponse({"saved": True})
