# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
from app_runtime import db


def BenchmarkTest00413(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = (lambda v: v.strip())(forwarded_ip)
    token = '%032x' % random.getrandbits(128)
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(data), token))
    return JsonResponse({'token': str(token)}, status=200)
