# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
from app_runtime import db


def BenchmarkTest00055(request):
    user_id = request.GET.get('id', '')
    data, _sep, _rest = str(user_id).partition('\x00')
    token = secrets.token_hex(32)
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(data), token))
    return JsonResponse({'token': str(token)}, status=200)
