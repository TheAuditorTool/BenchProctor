# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet


def BenchmarkTest67102(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    kind = 'json' if str(ua_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = ua_value
            data = parsed
        case _:
            data = ua_value
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
