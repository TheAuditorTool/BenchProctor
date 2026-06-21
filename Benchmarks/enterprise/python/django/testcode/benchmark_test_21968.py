# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest21968(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    prefix = ''
    data = prefix + str(ua_value)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
