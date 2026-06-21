# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest64293(request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    prefix = ''
    data = prefix + str(config_value)
    auth_check('user', data)
    return JsonResponse({"saved": True})
