# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
from app_runtime import db


def BenchmarkTest00106(request):
    multipart_value = request.POST.get('multipart_field', '')
    if multipart_value:
        data = multipart_value
    else:
        data = ''
    token = '%032x' % random.getrandbits(128)
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(data), token))
    return JsonResponse({'token': str(token)}, status=200)
