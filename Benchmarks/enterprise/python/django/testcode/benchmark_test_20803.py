# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest20803(request):
    host_value = request.META.get('HTTP_HOST', '')
    if request.session.get('user') is None:
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
