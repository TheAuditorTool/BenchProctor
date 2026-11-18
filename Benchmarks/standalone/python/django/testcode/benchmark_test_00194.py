# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
from dataclasses import dataclass
import json
from app_runtime import db


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

def BenchmarkTest00194(request):
    json_value = json.loads(request.body or b'{}').get('payload', '')
    form = FormData(payload=json_value)
    data = form.payload
    token = '%032x' % random.getrandbits(128)
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(data), token))
    return JsonResponse({'token': str(token)}, status=200)
