# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest16835(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    if auth_header:
        data = auth_header
    else:
        data = ''
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
