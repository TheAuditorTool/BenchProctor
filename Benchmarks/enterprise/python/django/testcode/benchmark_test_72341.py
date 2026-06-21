# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest72341(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    parts = str(auth_header).split(',')
    data = ','.join(parts)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
