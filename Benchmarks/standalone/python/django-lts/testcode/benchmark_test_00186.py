# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
import base64
from app_runtime import db


def BenchmarkTest00186(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    token = '%032x' % random.getrandbits(128)
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(data), token))
    return JsonResponse({'token': str(token)}, status=200)
