# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00992(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = str(auth_header).replace('\x00', '')
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
