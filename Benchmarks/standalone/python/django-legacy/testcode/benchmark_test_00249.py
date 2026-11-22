# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
from app_runtime import db


def BenchmarkTest00249(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = '%s' % str(multipart_value)
    token = '%032x' % random.SystemRandom().getrandbits(128)
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(data), token))
    return JsonResponse({'token': str(token)}, status=200)
