# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
from app_runtime import db


def BenchmarkTest00416(request):
    cookie_value = request.COOKIES.get('session_token', '')
    kind = 'json' if str(cookie_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(cookie_value).strip()
        case _:
            data = str(cookie_value)
    token = '%032x' % random.getrandbits(128)
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(data), token))
    return JsonResponse({'token': str(token)}, status=200)
