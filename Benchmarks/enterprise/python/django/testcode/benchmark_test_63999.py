# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest63999(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    def normalize(value):
        return value.strip()
    data = normalize(auth_header)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
