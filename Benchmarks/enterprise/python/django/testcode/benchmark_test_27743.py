# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet


def BenchmarkTest27743(request):
    cookie_value = request.COOKIES.get('session_token', '')
    pending = list(str(cookie_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
