# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
import os
from app_runtime import db


def BenchmarkTest00177(request):
    env_value = os.environ.get('APP_INPUT', '')
    data, _sep, _rest = str(env_value).partition('\x00')
    token = random.randbytes(16).hex()
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(data), token))
    return JsonResponse({'token': str(token)}, status=200)
