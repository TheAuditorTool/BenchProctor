# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
from app_runtime import db


def BenchmarkTest00638(request):
    user_id = request.GET.get('id', '')
    def normalize(value):
        return value.strip()
    data = normalize(user_id)
    token = '%032x' % random.getrandbits(128)
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(data), token))
    return JsonResponse({'token': str(token)}, status=200)
