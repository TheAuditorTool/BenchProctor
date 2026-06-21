# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest08050(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = str(ua_value).replace('\x00', '')
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
