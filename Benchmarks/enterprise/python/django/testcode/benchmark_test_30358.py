# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest30358(request):
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    prefix = ''
    data = prefix + str(yaml_value)
    auth_check('user', data)
    return JsonResponse({"saved": True})
