# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest00152(request, path_param):
    path_value = path_param
    try:
        data = json.loads(path_value).get('value', path_value)
    except (json.JSONDecodeError, AttributeError):
        data = path_value
    _coerced = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    processed = _coerced
    code = compile(str(processed), '<rule>', 'exec')
    exec(code)
    return JsonResponse({"saved": True})
