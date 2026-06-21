# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import auth_check


def BenchmarkTest20158(request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    kind = 'json' if str(file_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = file_value
            data = parsed
        case _:
            data = file_value
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return JsonResponse({"saved": True})
