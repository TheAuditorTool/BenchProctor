# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest49370(request):
    user_id = request.GET.get('id', '')
    data = handle(user_id)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
