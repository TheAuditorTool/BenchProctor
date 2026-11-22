# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
import base64
from app_runtime import db


def BenchmarkTest00186(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    token = secrets.token_bytes(16).hex()
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(data), token))
    return JsonResponse({'token': str(token)}, status=200)
