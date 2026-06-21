# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import jwt


def BenchmarkTest05254(request):
    secret_value = 'config_secret_test_abc123'
    pending = list(str(secret_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    jwt.encode({'sub': 'user'}, data, algorithm='HS256')
    return JsonResponse({"saved": True})
