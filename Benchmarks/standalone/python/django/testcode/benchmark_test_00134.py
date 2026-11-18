# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
import os
from app_runtime import db


def BenchmarkTest00134(request):
    env_value = os.environ.get('APP_INPUT', '')
    data = f'{env_value!s}'
    token = '%032x' % random.getrandbits(128)
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(data), token))
    return JsonResponse({'token': str(token)}, status=200)
