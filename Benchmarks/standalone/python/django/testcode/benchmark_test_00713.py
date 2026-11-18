# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
import json
from app_runtime import db


def BenchmarkTest00713(request):
    graphql_var = json.loads(request.body or b'{}').get('variables', {}).get('input', '')
    parts = []
    for token in str(graphql_var).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    token = '%032x' % random.getrandbits(128)
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(data), token))
    return JsonResponse({'token': str(token)}, status=200)
