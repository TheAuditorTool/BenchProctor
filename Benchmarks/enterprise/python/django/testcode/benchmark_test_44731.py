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

def BenchmarkTest44731(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = handle(header_value)
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(data),))
    return JsonResponse({'record': str(record)}, status=200)
