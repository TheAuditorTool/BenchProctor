# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest60966(request):
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    data = '%s' % (yaml_value,)
    auth_check('user', data)
    return JsonResponse({"saved": True})
