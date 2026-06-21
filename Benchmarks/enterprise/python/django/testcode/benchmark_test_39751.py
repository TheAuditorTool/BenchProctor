# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest39751(request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    auth_check('user', prop_value)
    return JsonResponse({"saved": True})
