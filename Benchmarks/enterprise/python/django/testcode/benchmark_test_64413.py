# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def ensure_str(value):
    return str(value)

def BenchmarkTest64413(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = ensure_str(forwarded_ip)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
