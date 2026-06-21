# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest67981(request):
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    auth_check('user', yaml_value)
    return JsonResponse({"saved": True})
