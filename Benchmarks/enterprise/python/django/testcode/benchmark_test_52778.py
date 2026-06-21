# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest52778(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
