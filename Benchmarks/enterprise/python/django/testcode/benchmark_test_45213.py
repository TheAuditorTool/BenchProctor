# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest45213(request):
    user_id = request.GET.get('id', '')
    data = handle(user_id)
    processed = data[:64]
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(processed),))
    return JsonResponse({'record': str(record)}, status=200)
