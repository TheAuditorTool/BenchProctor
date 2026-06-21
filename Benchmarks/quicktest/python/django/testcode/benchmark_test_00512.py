# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def to_text(value):
    return str(value).strip()

def BenchmarkTest00512(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = to_text(referer_value)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
