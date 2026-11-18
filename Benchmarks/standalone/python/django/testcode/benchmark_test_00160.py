# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
from app_runtime import db


def BenchmarkTest00160(request):
    raw_body = request.body.decode('utf-8')
    token = secrets.token_hex(32)
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(raw_body), token))
    return JsonResponse({'token': str(token)}, status=200)
