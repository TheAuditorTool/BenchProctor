# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
from app_runtime import db


def BenchmarkTest00211(request):
    upload_name = request.FILES['upload'].name
    data = str(upload_name).replace('\x00', '')
    token = '%032x' % random.Random().getrandbits(128)
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(data), token))
    return JsonResponse({'token': str(token)}, status=200)
