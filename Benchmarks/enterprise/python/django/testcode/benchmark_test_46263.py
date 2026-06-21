# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest46263(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
