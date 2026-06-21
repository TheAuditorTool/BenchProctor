# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def to_text(value):
    return str(value).strip()

def BenchmarkTest49856(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = to_text(host_value)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
