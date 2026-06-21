# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest02289(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data, _sep, _rest = str(forwarded_ip).partition('\x00')
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
