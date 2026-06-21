# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
from app_runtime import db


def BenchmarkTest73837(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    random.seed(int(comment_value) if str(comment_value).isdigit() else 7)
    token = random.getrandbits(8)
    return JsonResponse({'token': str(token)}, status=200)
