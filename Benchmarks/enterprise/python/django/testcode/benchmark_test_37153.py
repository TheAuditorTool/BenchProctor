# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest37153(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
