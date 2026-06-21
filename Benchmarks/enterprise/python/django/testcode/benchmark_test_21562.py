# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
import re
from app_runtime import db


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest21562(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = handle(comment_value)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    random.seed(int(processed) if str(processed).isdigit() else 42)
    token = str(random.random())
    return JsonResponse({'token': str(token)}, status=200)
