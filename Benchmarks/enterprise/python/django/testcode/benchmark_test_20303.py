# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest20303(request):
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    data = str(yaml_value).replace('\x00', '')
    auth_check('user', data)
    return JsonResponse({"saved": True})
