# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
import json
from app_runtime import db


def BenchmarkTest00115(request):
    xml_value = request.body.decode('utf-8')
    try:
        data = json.loads(xml_value).get('value', xml_value)
    except (json.JSONDecodeError, AttributeError):
        data = xml_value
    token = secrets.token_bytes(16).hex()
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(data), token))
    return JsonResponse({'token': str(token)}, status=200)
