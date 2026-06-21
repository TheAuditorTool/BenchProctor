# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import auth_check


def BenchmarkTest21455(request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    try:
        data = json.loads(prop_value).get('value', prop_value)
    except (json.JSONDecodeError, AttributeError):
        data = prop_value
    auth_check('user', data)
    return JsonResponse({"saved": True})
