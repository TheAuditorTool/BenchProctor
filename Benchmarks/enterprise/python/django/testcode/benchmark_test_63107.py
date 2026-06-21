# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest63107(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = forwarded_ip if forwarded_ip else 'default'
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
