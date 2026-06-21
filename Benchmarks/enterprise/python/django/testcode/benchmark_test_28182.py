# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest28182(request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    parts = []
    for token in str(config_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    auth_check('user', data)
    return JsonResponse({"saved": True})
