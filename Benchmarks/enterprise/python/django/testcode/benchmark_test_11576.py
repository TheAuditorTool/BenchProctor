# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest11576(request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    if prop_value:
        data = prop_value
    else:
        data = ''
    auth_check('user', data)
    return JsonResponse({"saved": True})
