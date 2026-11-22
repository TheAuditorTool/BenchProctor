# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
from app_runtime import db


def BenchmarkTest00116(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    parts = str(referer_value).split(',')
    data = ' '.join(parts)
    token = '%032x' % random.Random().getrandbits(128)
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(data), token))
    return JsonResponse({'token': str(token)}, status=200)
