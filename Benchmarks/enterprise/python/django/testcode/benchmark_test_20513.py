# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest20513(request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    kind = 'json' if str(prop_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = prop_value
            data = parsed
        case _:
            data = prop_value
    auth_check('user', data)
    return JsonResponse({"saved": True})
