# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
from app_runtime import db


def BenchmarkTest00469(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = f'{referer_value!s}'
    token = secrets.token_hex(32)
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(data), token))
    return JsonResponse({'token': str(token)}, status=200)
