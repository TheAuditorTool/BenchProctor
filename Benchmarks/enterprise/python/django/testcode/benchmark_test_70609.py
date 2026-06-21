# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
from app_runtime import auth_check


def BenchmarkTest70609(request):
    raw_body = request.body.decode('utf-8')
    kind = 'json' if str(raw_body).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = raw_body
            data = parsed
        case _:
            data = raw_body
    auth_check('user', hashlib.sha256(str(data).encode()).hexdigest())
    return JsonResponse({"saved": True})
