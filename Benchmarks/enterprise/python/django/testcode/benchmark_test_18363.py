# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest18363(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = ua_value if ua_value else 'default'
    if request.session.get('user') is None:
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
