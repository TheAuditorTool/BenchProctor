# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
from app_runtime import db


def BenchmarkTest00018(request):
    raw_body = request.body.decode('utf-8')
    token = '%032x' % random.SystemRandom().getrandbits(128)
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(raw_body), token))
    return JsonResponse({'token': str(token)}, status=200)
