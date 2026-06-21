# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest55127(request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    data = f'{prop_value:.200s}'
    auth_check('user', data)
    return JsonResponse({"saved": True})
