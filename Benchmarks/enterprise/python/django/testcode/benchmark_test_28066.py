# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest28066(request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(prop_value)
    data = collected
    auth_check('user', data)
    return JsonResponse({"saved": True})
