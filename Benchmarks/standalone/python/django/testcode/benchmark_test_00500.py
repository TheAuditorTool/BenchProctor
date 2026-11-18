# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
from app_runtime import db


def BenchmarkTest00500(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    if auth_header:
        data = auth_header
    else:
        data = ''
    token = '%032x' % random.getrandbits(128)
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(data), token))
    return JsonResponse({'token': str(token)}, status=200)
