# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest25972(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ns = SimpleNamespace(payload=comment_value)
    data = getattr(ns, 'payload')
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return JsonResponse({'token': str(token)}, status=200)
