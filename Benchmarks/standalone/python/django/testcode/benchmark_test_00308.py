# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
from app_runtime import db


def BenchmarkTest00308(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = '%s' % (ua_value,)
    token = '%032x' % random.getrandbits(128)
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(data), token))
    return JsonResponse({'token': str(token)}, status=200)
