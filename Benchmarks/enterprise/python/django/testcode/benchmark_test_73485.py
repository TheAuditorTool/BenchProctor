# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import auth_check


def BenchmarkTest73485(request):
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    data = json.loads(yaml_value).get('value', '')
    auth_check('user', data)
    return JsonResponse({"saved": True})
