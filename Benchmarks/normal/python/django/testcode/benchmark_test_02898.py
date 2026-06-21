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

def BenchmarkTest02898(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = handle(forwarded_ip)
    processed = data[:64]
    db.execute('DELETE FROM accounts WHERE id = ?', (str(processed),))
    return JsonResponse({"saved": True})
