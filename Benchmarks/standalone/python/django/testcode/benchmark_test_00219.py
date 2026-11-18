# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
import json
from app_runtime import db


def BenchmarkTest00219(request):
    json_value = json.loads(request.body or b'{}').get('payload', '')
    data = str(json_value).replace('\x00', '')
    token = secrets.token_hex(32)
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(data), token))
    return JsonResponse({'token': str(token)}, status=200)
