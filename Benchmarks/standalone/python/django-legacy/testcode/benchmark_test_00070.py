# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
from app_runtime import db


def BenchmarkTest00070(request):
    raw_body = request.body.decode('utf-8')
    kind = 'json' if str(raw_body).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(raw_body).strip()
        case _:
            data = str(raw_body)
    token = secrets.token_bytes(16).hex()
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(data), token))
    return JsonResponse({'token': str(token)}, status=200)
