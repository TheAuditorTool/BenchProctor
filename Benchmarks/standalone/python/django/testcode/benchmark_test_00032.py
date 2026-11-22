# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
from app_runtime import db


def BenchmarkTest00032(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = '%s' % (comment_value,)
    token = random.randbytes(16).hex()
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(data), token))
    return JsonResponse({'token': str(token)}, status=200)
