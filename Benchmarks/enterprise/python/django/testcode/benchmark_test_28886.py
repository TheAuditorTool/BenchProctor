# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest28886(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = ' '.join(str(ua_value).split())
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
