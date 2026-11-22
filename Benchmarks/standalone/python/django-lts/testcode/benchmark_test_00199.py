# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
from app_runtime import db


def BenchmarkTest00199(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    if header_value:
        data = header_value
    else:
        data = ''
    token = secrets.token_hex(32)
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(data), token))
    return JsonResponse({'token': str(token)}, status=200)
