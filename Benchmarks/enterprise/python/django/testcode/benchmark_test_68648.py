# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest68648(request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    auth_check('user', config_value)
    return JsonResponse({"saved": True})
