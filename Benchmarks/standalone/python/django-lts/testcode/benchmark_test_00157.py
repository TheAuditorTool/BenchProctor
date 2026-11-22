# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
from app_runtime import db


def BenchmarkTest00157(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = '{}'.format(header_value)
    token = secrets.token_bytes(16).hex()
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(data), token))
    return JsonResponse({'token': str(token)}, status=200)
