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

def BenchmarkTest35569(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = handle(forwarded_ip)
    db.execute('SELECT * FROM users WHERE id = ?', (data,))
    return JsonResponse({"saved": True})
