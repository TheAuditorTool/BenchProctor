# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
import json
from app_runtime import db


def BenchmarkTest00171(request):
    graphql_var = json.loads(request.body or b'{}').get('variables', {}).get('input', '')
    parts = str(graphql_var).split(',')
    data = ' '.join(parts)
    token = secrets.token_hex(32)
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(data), token))
    return JsonResponse({'token': str(token)}, status=200)
