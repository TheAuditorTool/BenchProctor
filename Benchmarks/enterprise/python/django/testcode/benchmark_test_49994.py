# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest49994(request):
    user_id = request.GET.get('id', '')
    data = handle(user_id)
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
