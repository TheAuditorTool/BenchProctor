# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import jwt
import os


def BenchmarkTest42179(request):
    secret_value = 'default_setting_value'
    parts = []
    for token in str(secret_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    store_cred = os.environ.get('APP_SECRET', '')
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return JsonResponse({"saved": True})
