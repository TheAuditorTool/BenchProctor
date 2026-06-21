# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest11037(request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    kind = 'json' if str(config_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = config_value
            data = parsed
        case _:
            data = config_value
    auth_check('user', data)
    return JsonResponse({"saved": True})
