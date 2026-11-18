# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
import json
from app_runtime import db


def BenchmarkTest00533(request):
    json_value = json.loads(request.body or b'{}').get('payload', '')
    parts = str(json_value).split(',')
    data = ' '.join(parts)
    token = secrets.token_hex(32)
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(data), token))
    return JsonResponse({'token': str(token)}, status=200)
