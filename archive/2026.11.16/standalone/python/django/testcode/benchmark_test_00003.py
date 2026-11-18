# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
from app_runtime import db


def BenchmarkTest00003(request, path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    token = secrets.token_hex(32)
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(data), token))
    return JsonResponse({'token': str(token)}, status=200)
