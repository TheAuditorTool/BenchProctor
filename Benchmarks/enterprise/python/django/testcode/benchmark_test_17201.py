# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest17201(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
