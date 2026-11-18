# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
import json
from app_runtime import db


def BenchmarkTest00521(request):
    json_value = json.loads(request.body or b'{}').get('payload', '')
    data = '%s' % str(json_value)
    token = '%032x' % random.getrandbits(128)
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(data), token))
    return JsonResponse({'token': str(token)}, status=200)
