# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest59962(request):
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    parts = str(yaml_value).split(',')
    data = ','.join(parts)
    auth_check('user', data)
    return JsonResponse({"saved": True})
