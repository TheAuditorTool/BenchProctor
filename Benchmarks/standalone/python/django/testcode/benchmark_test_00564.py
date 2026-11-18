# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
import json
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest00564(request):
    json_value = json.loads(request.body or b'{}').get('payload', '')
    reader = make_reader(json_value)
    data = reader()
    token = secrets.token_hex(32)
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(data), token))
    return JsonResponse({'token': str(token)}, status=200)
