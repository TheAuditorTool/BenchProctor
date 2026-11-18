# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
from app_runtime import db


def BenchmarkTest00672(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    parts = str(forwarded_ip).split(',')
    data = ' '.join(parts)
    token = secrets.token_hex(32)
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(data), token))
    return JsonResponse({'token': str(token)}, status=200)
