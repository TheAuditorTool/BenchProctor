# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def ensure_str(value):
    return str(value)

def BenchmarkTest61731(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = ensure_str(ua_value)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
