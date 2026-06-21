# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import socket


def BenchmarkTest01519(request):
    env_value = os.environ.get('USER_INPUT', '')
    kind = 'json' if str(env_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = env_value
            data = parsed
        case _:
            data = env_value
    s = socket.create_connection((str(data), 80))
    s.close()
    return JsonResponse({"saved": True})
