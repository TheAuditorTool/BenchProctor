# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def ensure_str(value):
    return str(value)

def BenchmarkTest67287(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = ensure_str(referer_value)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
