# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest75016(request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    data = (lambda v: v.strip())(prop_value)
    auth_check('user', data)
    return JsonResponse({"saved": True})
