# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest37304(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = f'{auth_header:.200s}'
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
