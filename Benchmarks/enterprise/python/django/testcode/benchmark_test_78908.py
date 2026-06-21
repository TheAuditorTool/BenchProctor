# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest78908(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = bytes.fromhex(auth_header).decode('utf-8', 'ignore')
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
